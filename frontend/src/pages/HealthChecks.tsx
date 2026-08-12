import { useEffect, useState } from "react";
import { getHealthChecks } from "../services/health";
import { getServices } from "../services/services";

interface HealthCheck {
  id: number;
  service_id: number;
  status_code: number | null;
  response_time_ms: number;
  is_healthy: boolean;
  checked_at: string;
}

interface Service {
  id: number;
  name: string;
  url: string;
  method: string;
  is_active: boolean;
}

export default function HealthChecks() {
  const [healthChecks, setHealthChecks] = useState<HealthCheck[]>([]);
  const [services, setServices] = useState<Service[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const [checks, serviceList] = await Promise.all([
          getHealthChecks(),
          getServices(),
        ]);

        setHealthChecks(checks);
        setServices(serviceList);
      } catch (error) {
        console.error("Failed to load health checks:", error);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  function getServiceName(serviceId: number) {
    const service = services.find((service) => service.id === serviceId);

    return service ? service.name : `Service #${serviceId}`;
  }

  if (loading) {
    return (
      <div>
        <h1 className="text-4xl font-bold">Health Checks</h1>
        <p className="mt-2 text-gray-500">
          Loading health check history...
        </p>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-4xl font-bold">Health Checks</h1>
        <p className="mt-2 text-gray-500">
          View recent health checks and service response times.
        </p>
      </div>

      <div className="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
        <table className="w-full">
          <thead>
            <tr className="border-b bg-gray-50 text-left">
              <th className="px-5 py-4 text-sm font-semibold text-gray-700">
                Service
              </th>

              <th className="px-5 py-4 text-sm font-semibold text-gray-700">
                Status
              </th>

              <th className="px-5 py-4 text-sm font-semibold text-gray-700">
                HTTP Code
              </th>

              <th className="px-5 py-4 text-sm font-semibold text-gray-700">
                Response Time
              </th>

              <th className="px-5 py-4 text-sm font-semibold text-gray-700">
                Checked At
              </th>
            </tr>
          </thead>

          <tbody>
            {healthChecks.map((check) => (
              <tr
                key={check.id}
                className="border-b last:border-b-0 hover:bg-gray-50"
              >
                <td className="px-5 py-4 font-medium text-gray-900">
                  {getServiceName(check.service_id)}
                </td>

                <td className="px-5 py-4">
                  <span
                    className={`inline-flex rounded-full px-3 py-1 text-xs font-semibold ${
                      check.is_healthy
                        ? "bg-green-100 text-green-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {check.is_healthy ? "HEALTHY" : "FAILED"}
                  </span>
                </td>

                <td className="px-5 py-4 text-gray-600">
                  {check.status_code ?? "N/A"}
                </td>

                <td className="px-5 py-4 text-gray-600">
                  {check.response_time_ms.toFixed(2)} ms
                </td>

                <td className="px-5 py-4 text-gray-600">
                  {new Date(check.checked_at).toLocaleString()}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {healthChecks.length === 0 && (
          <div className="p-8 text-center text-gray-500">
            No health checks recorded yet.
          </div>
        )}
      </div>
    </div>
  );
}
