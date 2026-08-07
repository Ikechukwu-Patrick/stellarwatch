import { api } from "./api";

export async function getHealthChecks() {
  const { data } = await api.get("/api/v1/health-checks");
  return data;
}