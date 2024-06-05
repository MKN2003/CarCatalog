from fastapi import APIRouter
from database.carservice import get_category_db, get_cars_db, add_category_db, add_car_db

test_router = APIRouter(prefix='/car', tags=['API for cars'])
