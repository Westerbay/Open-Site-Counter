from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import init_db
from api.routes import router

class Application:
    def __init__(self) -> None:
        self.app = FastAPI(
            title="Websites Registry API",
            version="1.0.0",
            lifespan=self.lifespan
        )
        self._include_routes()

    def _include_routes(self) -> None:
        self.app.include_router(router)

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        # Startup
        init_db()
        yield
        # Shutdown
        # (ex: close db connections if needed)

    def get_app(self) -> FastAPI:
        return self.app
