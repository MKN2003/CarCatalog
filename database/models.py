from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class CarsCategory(Base):
    __tablename__ = 'category'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    datetime = Column(DateTime)


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    model_name = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)

    category_fk = relationship(CarsCategory, foreign_keys=[category_id], lazy='subquery')

