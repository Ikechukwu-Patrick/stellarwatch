import api from "./api";

export interface HealthCheck {
  id: number;
  service_id: number;
  status_code: number | null;
  response_time_ms: number;
  is_healthy: boolean;
  checked_at: string;
}

export async function getHealthChecks(): Promise<HealthCheck[]> {
  const response = await api.get("/api/v1/health-checks");
  return response.data;
}