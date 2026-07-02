import { useEffect, useState } from "react";
import {
  getProjects,
  createProject,
} from "../../services/projectService";

function Projects() {
  const [projects, setProjects] = useState([]);

  const [form, setForm] = useState({
    name: "",
    description: "",
  });

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      const response = await getProjects();
      setProjects(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    if (!form.name) {
      alert("Project name is required");
      return;
    }

    try {
      await createProject(form);

      setForm({
        name: "",
        description: "",
      });

      loadProjects();
    } catch (error) {
      console.error(error);
      alert("Unable to create project");
    }
  };

  return (
    <div>

      <h1 className="text-3xl font-bold mb-6">
        Projects
      </h1>

      <div className="bg-white shadow rounded-xl p-6 mb-8">

        <div className="grid grid-cols-2 gap-4">

          <input
            type="text"
            name="name"
            placeholder="Project Name"
            value={form.name}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

          <input
            type="text"
            name="description"
            placeholder="Description"
            value={form.description}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

        </div>

        <button
          onClick={handleSubmit}
          className="mt-4 bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          Create Project
        </button>

      </div>

      <div className="bg-white shadow rounded-xl">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="text-left p-4">ID</th>

              <th className="text-left p-4">Project Name</th>

              <th className="text-left p-4">Description</th>

            </tr>

          </thead>

          <tbody>

            {projects.map((project) => (

              <tr key={project.id} className="border-t">

                <td className="p-4">
                  {project.id}
                </td>

                <td className="p-4">
                  {project.name}
                </td>

                <td className="p-4">
                  {project.description}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Projects;