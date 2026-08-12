interface Service {
  id: number;
  name: string;
  url: string;
  method: string;
  is_active: boolean;
}

interface ServiceCardProps {
  service: Service;
  onCheck: (id: number) => void;
  onDelete: (id: number) => void;
  checking: boolean;
}

export default function ServiceCard({
  service,
  onCheck,
  onDelete,
  checking,
}: ServiceCardProps) {
  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0">
          <h2 className="text-lg font-semibold text-gray-900">
            {service.name}
          </h2>

          <p className="text-sm text-gray-500 mt-1 break-all">
            {service.url}
          </p>
        </div>

        <span
          className={`shrink-0 px-3 py-1 rounded-full text-xs font-medium ${
            service.is_active
              ? "bg-green-100 text-green-700"
              : "bg-gray-100 text-gray-600"
          }`}
        >
          {service.is_active ? "Active" : "Inactive"}
        </span>
      </div>

      <div className="mt-5 flex items-center justify-between">
        <span className="text-sm text-gray-500">
          Method:{" "}
          <span className="font-semibold text-gray-700">
            {service.method}
          </span>
        </span>

        <div className="flex gap-2">
          <button
            onClick={() => onCheck(service.id)}
            disabled={checking}
            className="px-4 py-2 text-sm font-medium text-blue-600 border border-blue-200 rounded-lg hover:bg-blue-50 disabled:opacity-50"
          >
            {checking ? "Checking..." : "Run Check"}
          </button>

          <button
            onClick={() => onDelete(service.id)}
            className="px-4 py-2 text-sm font-medium text-red-600 border border-red-200 rounded-lg hover:bg-red-50"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}
