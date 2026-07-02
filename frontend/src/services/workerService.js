import api from "./api";

export const getWorkers = () => api.get("/workers/");