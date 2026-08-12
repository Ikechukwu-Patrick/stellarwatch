import { useEffect, useState } from "react";

import ServiceCard from "@/components/services/ServiceCard";
import { api } from "@/services/api";

interface Service {
  id: number;
  name: string;
  url: string;
  method: string;
  is_active: boolean;
}

export default function Services() {
  const [services, setServices] = useState<Service[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [method, setMethod] = useState("GET");

  const [submitting, setSubmitting] = useState(false);
  const [checkingId, setCheckingId] = useState<number | null>(null);

  async function loadServices() {
    try {
      setError("");

      const { data } = await api.get<Service[]>("/api/v1/services");

      setServices(data);
    } catch (err) {
      console.error(err);
      setError("Unable to load services. Make sure the PulseForge API is running.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadServices();
  }, []);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!name.trim() || !url.trim()) {
      setError("Service name and URL are required.");
      return;
    }

    try {
      setSubmitting(true);
      setError("");

      await api.post("/api/v1/services", {
        name: name.trim(),
        url: url.trim(),
        method,
      });

      setName("");
      setUrl("");
      setMethod("GET");

      await loadServices();
    } catch (err) {
      console.error(err);
      setError("Unable to create service. Please check the URL and try again.");
    } finally {
      setSubmitting(false);
    }
  }

  async function handleCheck(id: number) {
    try {
      setCheckingId(id);
      setError("");

      await api.post(`/api/v1/services/${id}/check`);

      await loadServices();
    } catch (err) {
      console.error(err);
      setError("Unable to run health check.");
    } finally {
      setCheckingId(null);
    }
  }

  async function handleDelete(id: number) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this service?"
    );

    if (!confirmed) {
      return;
    }

    try {
      setError("");

      await api.delete(`/api/v1/services/${id}`);

      await loadServices();
    } catch (err) {
      console.error(err);
      setError("Unable to delete service.");
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">
          Services
        </h1>

        <p className="mt-1 text-gray-500">
          Manage the APIs and services monitored by PulseForge.
        </p>
      </div>

      {error && (
        <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-700">
          {error}
        </div>
      )}

      <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
        <h2 className="text-xl font-semibold text-gray-900">
          Add Service
        </h2>

        <p className="text-sm text-gray-500 mt-1 mb-5">
          Add an API or service that PulseForge should monitor.
        </p>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-4"
        >
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Service Name
            </label>

            <input
              type="text"
              value={name}
              onChange={(event) => setName(event.target.value)}
              placeholder="My API"
              className="w-full rounded-lg border border-gray-300 px-4 py-2.5 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              HTTP Method
            </label>

            <select
              value={method}
              onChange={(event) => setMethod(event.target.value)}
              className="w-full rounded-lg border border-gray-300 px-4 py-2.5 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            >
              <option value="GET">GET</option>
              <option value="POST">POST</option>
              <option value="PUT">PUT</option>
              <option value="PATCH">PATCH</option>
              <option value="DELETE">DELETE</option>
            </select>
          </div>

          <div className="md:col-span-2">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Service URL
            </label>

            <input
              type="url"
              value={url}
              onChange={(event) => setUrl(event.target.value)}
              placeholder="https://api.example.com/health"
              className="w-full rounded-lg border border-gray-300 px-4 py-2.5 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />
          </div>

          <div className="md:col-span-2">
            <button
              type="submit"
              disabled={submitting}
              className="px-5 py-2.5 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 disabled:opacity-50"
            >
              {submitting ? "Adding..." : "Add Service"}
            </button>
          </div>
        </form>
      </div>

      <div>
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              Monitored Services
            </h2>

            <p className="text-sm text-gray-500">
              {services.length} service{services.length === 1 ? "" : "s"} configured
            </p>
          </div>
        </div>

        {loading ? (
          <div className="bg-white rounded-xl border border-gray-200 p-8 text-center text-gray-500">
            Loading services...
          </div>
        ) : services.length === 0 ? (
          <div className="bg-white rounded-xl border border-gray-200 p-8 text-center">
            <h3 className="font-semibold text-gray-900">
              No services yet
            </h3>

            <p className="mt-1 text-sm text-gray-500">
              Add your first service above to start monitoring it.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {services.map((service) => (
              <ServiceCard
                key={service.id}
                service={service}
                onCheck={handleCheck}
                onDelete={handleDelete}
                checking={checkingId === service.id}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
