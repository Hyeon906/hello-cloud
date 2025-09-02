from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/echo")
def echo(msg: Optional[str] = None):
    return {"echo": msg}
