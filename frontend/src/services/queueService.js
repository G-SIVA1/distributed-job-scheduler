import api from "./api";

export const getQueues = async () => {
  return await api.get("/queues/");
};

export const createQueue = async (queue) => {
  return await api.post("/queues/", queue);
};