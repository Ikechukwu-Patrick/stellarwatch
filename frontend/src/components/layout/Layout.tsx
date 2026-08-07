import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

export default function Layout() {
  return (
    <div className="flex">

      <Sidebar/>

      <main className="flex-1 bg-gray-100 min-h-screen">

        <Navbar/>

        <div className="p-8">
          <Outlet/>
        </div>

      </main>

    </div>
  );
}