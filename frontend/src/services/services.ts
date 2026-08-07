import api from "./api";

export interface Service {
  id: number;
  name: string;
  url: string;
  method: string;
  is_active: boolean;
}

export async function getServices(): Promise<Service[]> {
  const response = await api.get("/api/v1/services");
  return response.data;
}