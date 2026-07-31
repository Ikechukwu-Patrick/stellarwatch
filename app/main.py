from fastapi import FastAPI

app = FastAPI(
    title="PulseForge",
    version="0.1.0",
    description="Open-source API health monitoring platform",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PulseForge 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }