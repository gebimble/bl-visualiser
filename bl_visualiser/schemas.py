from datetime import date
from pydantic import BaseModel, ConfigDict

from bl_visualiser.models import Sexes


class ScoreBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    value: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreCreate):
    id: int
    climber_id: int
    route_id: int


class ClimberBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    sex: Sexes
    date_of_birth: date


class ClimberCreate(ClimberBase):
    pass


class Climber(ClimberBase):
    id: int
    scores: list[Score] = []


class RouteBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number: int


class RouteCreate(RouteBase):
    pass


class Route(RouteBase):
    id: int
    competition_id: int

    features_in: list = []


class CompetitionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    date: date


class CompetitionCreate(CompetitionBase):
    pass


class Competition(CompetitionBase):
    id: int
    routes: list[Route] = []
