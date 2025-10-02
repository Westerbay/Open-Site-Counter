from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.website_srv import WebsiteService
from repositories.website_repo import WebsiteRepository

router = APIRouter()

class RegisterIn(BaseModel):
    hostname: str

@router.post("/register")
async def register(payload: RegisterIn, request: Request):
    ip = request.headers.get("x-forwarded-for")
    if ip and "," in ip:
        ip = ip.split(",", 1)[0].strip()
    if not ip:
        ip = request.client.host if request.client else "unknown"

    service = WebsiteService(WebsiteRepository())
    service.register(payload.hostname, ip)

    return {"ok": True, "message": "registered"}

@router.get("/get")
async def get_placeholder():
    return {"ok": True, "message": "GET route à définir"}
