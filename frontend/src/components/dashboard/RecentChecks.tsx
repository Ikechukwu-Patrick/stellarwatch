import {
  CheckCircle2,
  XCircle,
  Activity,
} from "lucide-react";

export default function RecentChecks() {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-gray-900">
          Recent Health Checks
        </h2>

        <p className="mt-1 text-sm text-gray-500">
          Latest monitoring activity across your services.
        </p>
      </div>

      <div className="space-y-3">
        <div className="flex items-center justify-between rounded-lg border border-gray-100 p-4">
          <div className="flex items-center gap-3">
            <CheckCircle2
              className="text-green-600"
              size={20}
            />

            <div>
              <p className="font-medium text-gray-800">
                Service check
              </p>

              <p className="text-xs text-gray-500">
                HTTP 200
              </p>
            </div>
          </div>

          <span className="text-sm font-medium text-green-600">
            Healthy
          </span>
        </div>

        <div className="flex items-center justify-between rounded-lg border border-gray-100 p-4">
          <div className="flex items-center gap-3">
            <XCircle
              className="text-red-600"
              size={20}
            />

            <div>
              <p className="font-medium text-gray-800">
                Service check
              </p>

              <p className="text-xs text-gray-500">
                Service unavailable
              </p>
            </div>
          </div>

          <span className="text-sm font-medium text-red-600">
            Failed
          </span>
        </div>

        <div className="flex items-center gap-3 rounded-lg border border-dashed border-gray-200 p-4 text-gray-500">
          <Activity size={20} />

          <span className="text-sm">
            More health checks will appear as monitoring runs.
          </span>
        </div>
      </div>
    </div>
  );
}
