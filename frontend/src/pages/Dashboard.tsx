import { useEffect, useState } from "react";

import StatsGrid from "@/components/dashboard/StatsGrid";
import ResponseChart from "@/components/dashboard/ResponseChart";
import RecentAlerts from "@/components/dashboard/RecentAlerts";
import RecentChecks from "@/components/dashboard/RecentChecks";

import { getDashboardStats } from "@/services/dashboard";
import type { DashboardStats } from "@/services/dashboard";

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getDashboardStats()
      .then(setStats)
      .catch(() => {
        setError("Unable to load dashboard statistics.");
      });
  }, []);

  if (error) {
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-6">
        <h2 className="text-lg font-semibold text-red-700">
          Dashboard unavailable
        </h2>

        <p className="mt-1 text-sm text-red-600">
          {error} Make sure the PulseForge API is running.
        </p>
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="flex min-h-[300px] items-center justify-center">
        <div className="text-center">
          <div className="mx-auto mb-3 h-8 w-8 animate-spin rounded-full border-4 border-gray-200 border-t-blue-600" />

          <p className="text-sm text-gray-500">
            Loading dashboard...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-gray-900">
          Dashboard
        </h1>

        <p className="mt-1 text-sm text-gray-500">
          Monitor your services, health checks, response times, and alerts.
        </p>
      </div>

      <StatsGrid stats={stats} />

      <ResponseChart />

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
        <RecentAlerts />
        <RecentChecks />
      </div>
    </div>
  );
}
