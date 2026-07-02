import { useEffect, useState } from "react";
import { getJobs, createJob } from "../../services/jobService";

function Jobs() {
  const [jobs, setJobs] = useState([]);

  const [form, setForm] = useState({
    name: "",
    payload: "{}",
    priority: 1,
    queue_id: "",
    scheduled_at: "",
  });

  useEffect(() => {
    loadJobs();
  }, []);

  const loadJobs = async () => {
    try {
      const response = await getJobs();
      setJobs(response.data);
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
      const job = {
        ...form,
        payload: JSON.parse(form.payload),
        scheduled_at: form.scheduled_at || null,
      };

      await createJob(job);

      setForm({
        name: "",
        payload: "{}",
        priority: 1,
        queue_id: "",
        scheduled_at: "",
      });

      loadJobs();
    } catch (error) {
      console.error(error);
      alert("Unable to create job");
    }
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Jobs</h1>

      <div className="bg-white shadow rounded-xl p-6 mb-8">

        <div className="grid grid-cols-2 gap-4">

          <input
            name="name"
            placeholder="Job Name"
            value={form.name}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

          <input
            type="number"
            name="priority"
            placeholder="Priority"
            value={form.priority}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

          <input
            type="number"
            name="queue_id"
            placeholder="Queue ID"
            value={form.queue_id}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

          <input
            type="datetime-local"
            name="scheduled_at"
            value={form.scheduled_at}
            onChange={handleChange}
            className="border rounded-lg p-3"
          />

          <textarea
            name="payload"
            value={form.payload}
            onChange={handleChange}
            className="border rounded-lg p-3 col-span-2"
            rows="5"
            placeholder='{"email":"abc@gmail.com"}'
          />

        </div>

        <button
          onClick={handleSubmit}
          className="mt-5 bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          Create Job
        </button>

      </div>

      <div className="bg-white rounded-xl shadow">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>
              <th className="p-4 text-left">ID</th>
              <th className="p-4 text-left">Name</th>
              <th className="p-4 text-left">Status</th>
              <th className="p-4 text-left">Priority</th>
              <th className="p-4 text-left">Retry</th>
              <th className="p-4 text-left">Queue</th>
            </tr>

          </thead>

          <tbody>

            {jobs.map((job) => (

              <tr key={job.id} className="border-t">

                <td className="p-4">{job.id}</td>

                <td className="p-4">{job.name}</td>

                <td className="p-4">{job.status}</td>

                <td className="p-4">{job.priority}</td>

                <td className="p-4">{job.retry_count}</td>

                <td className="p-4">{job.queue_id}</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Jobs;