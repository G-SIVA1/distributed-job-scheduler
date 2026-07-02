import { useEffect, useState } from "react";
import {
  getQueues,
  createQueue,
} from "../../services/queueService";

function Queues() {
  const [queues, setQueues] = useState([]);

  const [form, setForm] = useState({
    name: "",
    priority: 1,
    concurrency_limit: 1,
    project_id: "",
  });

  useEffect(() => {
    loadQueues();
  }, []);

  const loadQueues = async () => {
    try {
      const response = await getQueues();
      setQueues(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]:
        e.target.type === "number"
          ? Number(e.target.value)
          : e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      await createQueue(form);

      setForm({
        name: "",
        priority: 1,
        concurrency_limit: 1,
        project_id: "",
      });

      loadQueues();
    } catch (error) {
      console.error(error);
      alert("Unable to create queue");
    }
  };

  return (
    <div>

      <h1 className="text-3xl font-bold mb-6">
        Queues
      </h1>

      <div className="bg-white rounded-xl shadow p-6 mb-8">

        <div className="grid grid-cols-2 gap-4">

          <input
            name="name"
            placeholder="Queue Name"
            value={form.name}
            onChange={handleChange}
            className="border p-3 rounded-lg"
          />

          <input
            type="number"
            name="priority"
            placeholder="Priority"
            value={form.priority}
            onChange={handleChange}
            className="border p-3 rounded-lg"
          />

          <input
            type="number"
            name="concurrency_limit"
            placeholder="Concurrency"
            value={form.concurrency_limit}
            onChange={handleChange}
            className="border p-3 rounded-lg"
          />

          <input
            type="number"
            name="project_id"
            placeholder="Project ID"
            value={form.project_id}
            onChange={handleChange}
            className="border p-3 rounded-lg"
          />

        </div>

        <button
          onClick={handleSubmit}
          className="mt-5 bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          Create Queue
        </button>

      </div>

      <div className="bg-white rounded-xl shadow">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">ID</th>

              <th className="p-4 text-left">Name</th>

              <th className="p-4 text-left">Priority</th>

              <th className="p-4 text-left">Concurrency</th>

              <th className="p-4 text-left">Paused</th>

              <th className="p-4 text-left">Project</th>

            </tr>

          </thead>

          <tbody>

            {queues.map((queue) => (

              <tr key={queue.id} className="border-t">

                <td className="p-4">{queue.id}</td>

                <td className="p-4">{queue.name}</td>

                <td className="p-4">{queue.priority}</td>

                <td className="p-4">{queue.concurrency_limit}</td>

                <td className="p-4">
                  {queue.is_paused ? "Yes" : "No"}
                </td>

                <td className="p-4">{queue.project_id}</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Queues;