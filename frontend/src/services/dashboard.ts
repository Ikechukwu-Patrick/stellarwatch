import api from "./api";

export interface DashboardStats {
  total_services: number;
  healthy_services: number;
  down_services: number;
  total_alerts: number;
}

export async function getDashboardStats(): Promise<DashboardStats> {
  const response = await api.get("/dashboard/stats");
  return response.data;
}