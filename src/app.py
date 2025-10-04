from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.session import init_db
from api.routes import router

class Application:
    def __init__(self) -> None:
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        init_db()
        self._include_routes()

    def _include_routes(self) -> None:
        self.app.include_router(router)

    def get_app(self) -> FastAPI:
        return self.app
