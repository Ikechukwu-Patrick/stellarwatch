import {
  Server,
  CheckCircle2,
  XCircle,
  Bell,
} from "lucide-react";

import StatCard from "./StatCard";

interface Props {
  stats: {
    total_services: number;
    healthy_services: number;
    down_services: number;
    total_alerts: number;
  };
}

export default function StatsGrid({ stats }: Props) {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <StatCard
        title="Total Services"
        value={stats.total_services}
        description="Services being monitored"
        icon={<Server size={22} />}
        iconClassName="bg-blue-50 text-blue-600"
      />

      <StatCard
        title="Healthy"
        value={stats.healthy_services}
        description="Currently operational"
        icon={<CheckCircle2 size={22} />}
        iconClassName="bg-green-50 text-green-600"
      />

      <StatCard
        title="Down"
        value={stats.down_services}
        description="Currently unavailable"
        icon={<XCircle size={22} />}
        iconClassName="bg-red-50 text-red-600"
      />

      <StatCard
        title="Alerts"
        value={stats.total_alerts}
        description="Total recorded alerts"
        icon={<Bell size={22} />}
        iconClassName="bg-amber-50 text-amber-600"
      />
    </div>
  );
}
