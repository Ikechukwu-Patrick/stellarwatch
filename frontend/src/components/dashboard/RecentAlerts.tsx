import { AlertTriangle, CheckCircle2 } from "lucide-react";

export default function RecentAlerts() {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-gray-900">
          Recent Alerts
        </h2>

        <p className="mt-1 text-sm text-gray-500">
          Latest service incidents and notifications.
        </p>
      </div>

      <div className="space-y-4">
        <div className="flex items-start gap-3 rounded-lg border border-red-100 bg-red-50 p-4">
          <AlertTriangle className="mt-0.5 text-red-600" size={20} />

          <div>
            <p className="font-medium text-red-800">
              Service unavailable
            </p>

            <p className="mt-1 text-sm text-red-600">
              A monitored service is currently down.
            </p>

            <p className="mt-2 text-xs text-red-500">
              Recent alert
            </p>
          </div>
        </div>

        <div className="flex items-start gap-3 rounded-lg border border-gray-100 bg-gray-50 p-4">
          <CheckCircle2
            className="mt-0.5 text-green-600"
            size={20}
          />

          <div>
            <p className="font-medium text-gray-800">
              Alert monitoring active
            </p>

            <p className="mt-1 text-sm text-gray-500">
              StellerWatch is monitoring your configured services.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
