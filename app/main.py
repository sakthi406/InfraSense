from fastapi import FastAPI, HTTPException
import time
import logging
import json
from datetime import datetime,timezone
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
start_time = time.time()

# Metrics
Instrumentator().instrument(app).expose(app)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

@app.get("/health")
def health():
    response = {
        "status": "ok",
        "uptime": time.time() - start_time,
        "version": "1.0"
    }

    logger.info(json.dumps({
        "timestamp": str(datetime.now(timezone.utc)),
        "endpoint": "/health",
        "status": 200
    }))

    return response

@app.post("/process")
def process(data: dict):
    time.sleep(0.05)

    logger.info(json.dumps({
        "endpoint": "/process",
        "status": 200
    }))

    return {"processed": data}

@app.get("/fail")
def fail():
    logger.error("Intentional failure triggered")
    raise HTTPException(status_code=500, detail="Simulated failure")