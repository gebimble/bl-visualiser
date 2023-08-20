from typing import Any, Optional
from enum import StrEnum
from datetime import date

import numpy as np

from pydantic import BaseModel, field_validator, ConfigDict, PrivateAttr

import polars as pd

from faker import Faker

from bl_visualiser.generators.generate_scores import create_scores


fake = Faker()


Sex = StrEnum('Sex', ['Male', 'Female', 'Other'])

DataFrameSchema = {
    "name": str,
    "age": pd.UInt8,
    "sex": str,
    "date": pd.Date,
    "scores": pd.UInt8,
    "routes": pd.UInt8,
}


class ScoreCard(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str
    age: int
    sex: Sex
    date: date
    scores: np.ndarray
    routes: Optional[np.ndarray] = None

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.routes = np.array(
            [x for x in range(1, len(self.scores)+1)], dtype='uint8')
        return None


def create_scorecard(name=None, age=None, sex=None, date=None) -> dict[str, Any]:
    return ScoreCard(
        name=name if name is not None else fake.name(),
        age=age if age is not None else np.random.randint(100),
        sex=sex if sex is not None else np.random.choice(
            [x.value for x in Sex]),
        date=date if date is not None else fake.date(),
        scores=create_scores()
    )


def scorecard_to_dataframe(scorecard: ScoreCard) -> pd.DataFrame:
    return pd.DataFrame(dict(scorecard), schema=DataFrameSchema).rename({'scores': 'score', 'routes': 'route'})
