import { Routes, Route } from "react-router-dom";

import Layout from "./components/layout/Layout";

import Dashboard from "./pages/Dashboard/Dashboard";
import Projects from "./pages/Projects/Projects";
import Queues from "./pages/Queues/Queues";
import Jobs from "./pages/Jobs/Jobs";
import Workers from "./pages/Workers/Workers";
import Metrics from "./pages/Metrics/Metrics";
import Login from "./pages/Login/Login";

function App() {
  return (
    <Routes>

      <Route path="/login" element={<Login />} />

      <Route path="/" element={<Layout />}>

        <Route index element={<Dashboard />} />

        <Route
          path="projects"
          element={<Projects />}
        />

        <Route
          path="queues"
          element={<Queues />}
        />

        <Route
          path="jobs"
          element={<Jobs />}
        />

        <Route
          path="workers"
          element={<Workers />}
        />

        <Route
          path="metrics"
          element={<Metrics />}
        />

      </Route>

    </Routes>
  );
}

export default App;