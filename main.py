import uvicorn
from fastapi import FastAPI

from app.logs.router import router as logs_router
from core.database import Base, engine


def create_app() -> FastAPI:
    app = FastAPI()

    # initialize the database
    Base.metadata.create_all(bind=engine)

    # register routers
    app.include_router(logs_router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
