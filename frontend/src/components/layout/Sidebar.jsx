import {
  LayoutDashboard,
  FolderKanban,
  Boxes,
  ClipboardList,
  Users,
  BarChart3,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menus = [
  {
    icon: <LayoutDashboard size={20} />,
    title: "Dashboard",
    path: "/",
  },
  {
    icon: <FolderKanban size={20} />,
    title: "Projects",
    path: "/projects",
  },
  {
    icon: <Boxes size={20} />,
    title: "Queues",
    path: "/queues",
  },
  {
    icon: <ClipboardList size={20} />,
    title: "Jobs",
    path: "/jobs",
  },
  {
    icon: <Users size={20} />,
    title: "Workers",
    path: "/workers",
  },
  {
    icon: <BarChart3 size={20} />,
    title: "Metrics",
    path: "/metrics",
  },
];

function Sidebar() {
  return (
    <div
      style={{
        width: "250px",
        background: "#111827",
        color: "white",
        padding: "20px",
        minHeight: "100vh",
      }}
    >
      <h2 style={{ marginBottom: "40px" }}>
        Scheduler
      </h2>

      {menus.map((item) => (
        <NavLink
          key={item.title}
          to={item.path}
          style={({ isActive }) => ({
            display: "flex",
            alignItems: "center",
            gap: "10px",
            padding: "12px",
            marginBottom: "10px",
            borderRadius: "8px",
            textDecoration: "none",
            color: "white",
            background: isActive ? "#2563eb" : "transparent",
          })}
        >
          {item.icon}
          {item.title}
        </NavLink>
      ))}
    </div>
  );
}

export default Sidebar;