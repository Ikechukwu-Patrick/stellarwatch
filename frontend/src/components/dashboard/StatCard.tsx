import type { ReactNode } from "react";

interface StatCardProps {
  title: string;
  value: number | string;
  icon?: ReactNode;
  description?: string;
  iconClassName?: string;
}

export default function StatCard({
  title,
  value,
  icon,
  description,
  iconClassName = "bg-blue-50 text-blue-600",
}: StatCardProps) {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-5 shadow-sm transition hover:shadow-md">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-gray-500">
            {title}
          </p>

          <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900">
            {value}
          </p>

          {description && (
            <p className="mt-1 text-xs text-gray-500">
              {description}
            </p>
          )}
        </div>

        {icon && (
          <div
            className={`flex h-11 w-11 items-center justify-center rounded-lg ${iconClassName}`}
          >
            {icon}
          </div>
        )}
      </div>
    </div>
  );
}
