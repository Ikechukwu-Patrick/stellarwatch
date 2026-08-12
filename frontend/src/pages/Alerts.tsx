import { useEffect, useState } from "react";
import { getAlerts } from "../services/alerts";

interface Alert {
  id: number;
  service_id: number;
  title: string;
  message: string;
  severity: string;
  is_sent: boolean;
  created_at: string;
}

export default function Alerts() {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadAlerts() {
      try {
        const data = await getAlerts();
        setAlerts(data);
      } catch (err) {
        console.error(err);
        setError("Failed to load alerts.");
      } finally {
        setLoading(false);
      }
    }

    loadAlerts();
  }, []);

  if (loading) {
    return (
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Alerts</h1>
        <p className="mt-2 text-slate-500">Loading alerts...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Alerts</h1>
        <p className="mt-2 text-red-600">{error}</p>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-slate-900">Alerts</h1>

        <p className="mt-1 text-slate-500">
          Monitor service failures and recoveries.
        </p>
      </div>

      {alerts.length === 0 ? (
        <div className="rounded-xl border border-slate-200 bg-white p-8 text-center shadow-sm">
          <p className="text-slate-500">No alerts found.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {alerts.map((alert) => (
            <div
              key={alert.id}
              className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm"
            >
              <div className="flex items-start justify-between gap-4">
                <div>
                  <h2 className="text-lg font-semibold text-slate-900">
                    {alert.title}
                  </h2>

                  <p className="mt-1 text-slate-600">
                    {alert.message}
                  </p>

                  <p className="mt-3 text-sm text-slate-500">
                    Service ID: {alert.service_id}
                  </p>

                  <p className="text-sm text-slate-400">
                    {new Date(alert.created_at).toLocaleString()}
                  </p>
                </div>

                <span
                  className={`rounded-full px-3 py-1 text-xs font-semibold ${
                    alert.severity === "critical"
                      ? "bg-red-100 text-red-700"
                      : alert.severity === "warning"
                      ? "bg-yellow-100 text-yellow-700"
                      : "bg-green-100 text-green-700"
                  }`}
                >
                  {alert.severity.toUpperCase()}
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
