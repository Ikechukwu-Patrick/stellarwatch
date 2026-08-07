import { api } from "./api";

export async function getServices() {
  const { data } = await api.get("/api/v1/services");
  return data;
}