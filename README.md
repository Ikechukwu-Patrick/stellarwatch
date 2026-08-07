# 🚀 PulseForge

> An open-source API and service monitoring platform built with **FastAPI** and **React** for monitoring service availability, tracking uptime, measuring response times, and managing alerts.

---

## 📖 Overview

PulseForge helps developers and teams monitor APIs and web services from a centralized dashboard.

The platform continuously tracks service health, records response times, stores historical health checks, and provides actionable alerts whenever a monitored service becomes unavailable.

The goal of PulseForge is to provide a lightweight, extensible, and developer-friendly monitoring solution similar to lightweight versions of UptimeRobot or Better Stack.

---

# ✨ Features

## Backend

- RESTful API built with FastAPI
- Create and manage monitored services
- Run health checks
- Record response times
- Store health check history
- Alert generation
- Dashboard statistics endpoint
- SQLAlchemy ORM
- Alembic migrations
- SQLite database (development)

---

## Frontend

- Modern React dashboard
- Responsive sidebar navigation
- Dashboard overview
- Service statistics
- Health monitoring pages
- Alerts page
- Health Checks page
- API integration with Axios
- React Router navigation
- Tailwind CSS UI

---

# 📊 Dashboard

The dashboard provides:

- Total monitored services
- Healthy services
- Down services
- Total alerts
- Recent alerts
- Recent health checks
- Response time visualization

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Python

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Axios
- React Router
- Lucide React

---

# 📁 Project Structure

```
pulseforge/

├── backend/
│   ├── app/
│   ├── alembic/
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── router/
│   │   └── hooks/
│   └── package.json
│
└── README.md
```

---

# ⚙️ Getting Started

## Clone the repository

```bash
git clone https://github.com/WideForgeLabs/pulseforge.git

cd pulseforge
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🔗 API Endpoints

## Services

```
GET    /api/v1/services
POST   /api/v1/services
GET    /api/v1/services/{id}
DELETE /api/v1/services/{id}
POST   /api/v1/services/{id}/check
```

---

## Health Checks

```
GET /api/v1/health-checks
GET /api/v1/services/{id}/history
```

---

## Alerts

```
GET /api/v1/alerts
```

---

## Statistics

```
GET /dashboard/stats
GET /api/v1/services/{id}/stats
```

---

# 🚧 Current Status

## Completed

- Backend API
- Database models
- CRUD operations
- Health check engine
- Dashboard statistics
- Alerts API
- React frontend
- Dashboard layout
- Sidebar navigation
- API integration

## In Progress

- Dashboard charts
- Deployment
- Authentication
- Email notifications
- Background workers

---

# 🔮 Roadmap

- JWT Authentication
- PostgreSQL support
- Redis caching
- Celery background workers
- Email alerts
- SMS alerts
- Docker support
- Kubernetes deployment
- Prometheus metrics
- Grafana integration
- WebSocket live updates
- Dark mode
- User accounts
- Role-based access control

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve PulseForge:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

MIT License.

---

# 👨‍💻 Author

Built by **Ikechukwu Patrick**

GitHub:
https://github.com/WideForgeLabs/pulseforge

---

# ⭐ Vision

PulseForge aims to become an open-source, developer-first monitoring platform that enables teams to monitor services, visualize uptime, detect failures quickly, and respond proactively using modern cloud-native tooling.