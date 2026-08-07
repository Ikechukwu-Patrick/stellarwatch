import api from "./api";

export interface Alert {
  id: number;
  service_id: number;
  title: string;
  message: string;
  severity: string;
  is_sent: boolean;
  created_at: string;
}

export async function getAlerts(): Promise<Alert[]> {
  const response = await api.get("/api/v1/alerts");
  return response.data;
}