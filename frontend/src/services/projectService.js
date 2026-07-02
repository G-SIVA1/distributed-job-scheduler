import api from "./api";

export const getProjects = async () => {
    return await api.get("/projects/");
};

export const createProject = async (project) => {
    return await api.post("/projects/", project);
};