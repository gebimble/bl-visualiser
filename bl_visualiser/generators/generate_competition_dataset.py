import polars as pd
from faker import Faker

from bl_visualiser.generators.generate_scorecard import create_scorecard, scorecard_to_dataframe

fake = Faker()


def create_competition_dataset():
    first_comp_date = fake.date()
    first_scores = [
        create_scorecard(date=first_comp_date)
        for _ in range(100)
    ]

    second_comp_date = fake.date()
    second_scores = [
        create_scorecard(
            name=sc.name,
            age=sc.age,
            sex=sc.sex,
            date=second_comp_date
        )
        for sc in first_scores
    ]

    return pd.concat(
        items=[
            scorecard_to_dataframe(sc)
            for sc in first_scores + second_scores
        ],
        how="vertical"
    )
