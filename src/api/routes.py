from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.website_srv import WebsiteService
from repositories.website_repo import WebsiteRepository

router = APIRouter()

class Payload(BaseModel):
    hostname: str

@router.post("/register")
async def register(payload: Payload, request: Request):
    ip = request.headers.get("x-forwarded-for")
    if ip and "," in ip:
        ip = ip.split(",", 1)[0].strip()
    if not ip:
        ip = request.client.host if request.client else "unknown"

    service = WebsiteService(WebsiteRepository())
    service.register(payload.hostname, ip)

    return {"ok": True, "message": "registered"}

@router.post("/get")
async def get(payload: Payload):
    service = WebsiteService(WebsiteRepository())
    return service.get_stats(payload.hostname)
