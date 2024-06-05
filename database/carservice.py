from .models import CarsCategory, Car
from database import get_db


def get_category_db():
    db = next(get_db())

    category = db.query(CarsCategory).all()


def get_cars_db():
    db = next(get_db())

    cars = db.query(CarsCategory).all()


def add_category_db(name):
    db = next(get_db())
    checker = db.query(CarsCategory).filter_by(name=name).first()
    if checker:
        return f'Такая категорея уже существует: {checker.id}'
    else:
        new_category = CarsCategory(name=name)
        db.add(new_category)
        db.commit()
        return f"Категория {new_category.name} успешна добавлена"


def add_car_db(model_name, year):
    db = next(get_db())
    checker = db.query(Car).filter_by(model_name=model_name, year=year).first()
    if checker:
        return f'Такая машина уже существует'
    else:
        new_car = Car(model_name=model_name, year=year)
        db.add(new_car)
        db.commit()
        return f"Новая машина успешно добавлена"
