from enum import StrEnum

from sqlalchemy import (Column, ForeignKey, Integer,
                        String, Date, Enum, CheckConstraint)
from sqlalchemy.orm import relationship

from bl_visualiser.database import Base


Sexes = StrEnum('Sex', ['Male', 'Female', 'Other'])


class Climber(Base):
    __tablename__ = "climbers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    sex = Column(Enum(Sexes), unique=False, index=True)
    date_of_birth = Column(Date, unique=False, index=True)

    scores = relationship("Score", back_populates="climber")


class Competition(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, primary_key=False, index=True)
    date = Column(Date, primary_key=False, index=True)

    routes = relationship("Route", back_populates="features_in")


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(
        Integer,
        CheckConstraint("number between 1 and 30"),
        primary_key=False,
        index=True
    )
    competition_id = Column(Integer, ForeignKey("competitions.id"))

    features_in = relationship("Competition", back_populates="routes")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(
        Integer,
        CheckConstraint("value in (0, 1, 4, 7, 10)"),
        index=True
    )

    climber_id = Column(Integer, ForeignKey("climbers.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))

    climber = relationship("Climber", back_populates="scores")
