import { api } from "./api";

export async function getAlerts() {
  const { data } = await api.get("/api/v1/alerts");
  return data;
}