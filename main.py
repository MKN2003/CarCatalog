from fastapi import FastAPI

from api.car_api.cars import car_router
from api.test_api.tests import test_router
from database import Base, engine

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(car_router)
app.include_router(test_router)
