import {
    createBrowserRouter,
} from "react-router-dom";

import Layout from "../components/layout/Layout";

import Dashboard from "../pages/Dashboard";
import Services from "../pages/Services";
import Alerts from "../pages/Alerts";
import HealthChecks from "../pages/HealthChecks";
import NotFound from "../pages/NotFound";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        children: [
            {
                index: true,
                element: <Dashboard />,
            },
            {
                path: "services",
                element: <Services />,
            },
            {
                path: "alerts",
                element: <Alerts />,
            },
            {
                path: "health-checks",
                element: <HealthChecks />,
            },
        ],
    },
    {
        path: "*",
        element: <NotFound />,
    },
]);