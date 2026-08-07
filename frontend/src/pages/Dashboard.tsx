import { useEffect, useState } from "react";

import StatsGrid from "@/components/dashboard/StatsGrid";
import ResponseChart from "@/components/dashboard/ResponseChart";
import RecentAlerts from "@/components/dashboard/RecentAlerts";
import RecentChecks from "@/components/dashboard/RecentChecks";

import { getDashboardStats } from "@/services/dashboard";
import type { DashboardStats } from "@/services/dashboard";

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);

  useEffect(() => {
    getDashboardStats()
      .then(setStats)
      .catch(console.error);
  }, []);

  if (!stats) {
    return (
      <div className="p-6">
        Loading dashboard...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <StatsGrid stats={stats} />

      <ResponseChart />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <RecentAlerts />
        <RecentChecks />
      </div>
    </div>
  );
}