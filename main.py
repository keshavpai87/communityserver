from fastapi import FastAPI

from controllers.temple_controller import router

app = FastAPI()

app.include_router(router)