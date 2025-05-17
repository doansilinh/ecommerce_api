from fastapi import FastAPI

from app.api import router_v1

app = FastAPI(title="FastAPI Ecommerce", version="1.0.0")

app.include_router(router_v1, prefix="/api")


@app.api_route("/", methods=["GET", "HEAD"])
async def root():
    return {"message": "Hello from FastAPI!"}
