import { Bell, Search, UserCircle } from "lucide-react";

export default function Navbar() {
  return (
    <header className="flex justify-between items-center bg-white px-8 py-5 border-b">

      <div>
        <h2 className="text-2xl font-bold">
          Service Health Dashboard
        </h2>

        <p className="text-gray-500">
          Monitor your APIs in real time.
        </p>
      </div>

      <div className="flex items-center gap-6">

        <Search className="text-gray-500"/>

        <Bell className="text-gray-500"/>

        <UserCircle size={34}/>
      </div>

    </header>
  );
}