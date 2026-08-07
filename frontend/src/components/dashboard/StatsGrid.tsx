import {
  Server,
  CheckCircle,
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
    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
      <StatCard
        title="Total Services"
        value={stats.total_services}
        icon={<Server size={28} />}
      />

      <StatCard
        title="Healthy"
        value={stats.healthy_services}
        icon={<CheckCircle size={28} />}
      />

      <StatCard
        title="Down"
        value={stats.down_services}
        icon={<XCircle size={28} />}
      />

      <StatCard
        title="Alerts"
        value={stats.total_alerts}
        icon={<Bell size={28} />}
      />
    </div>
  );
}