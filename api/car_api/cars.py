from fastapi import APIRouter
from database.carservice import get_category_db, get_cars_db, add_category_db, add_car_db

car_router = APIRouter(prefix='/car', tags=['API for cars'])


@car_router.get('/all-categories')
async def all_categories():
    return get_category_db()


@car_router.get('/all-cars')
async def all_cars():
    return get_cars_db()


@car_router.post('/add-category')
async def add_category(name: str):
    return add_category_db(name)


@car_router.post('/add-car')
async def add_car(name: str, year: int):
    return add_car_db(name, year)

