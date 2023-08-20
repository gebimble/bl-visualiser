import polars as pd
from bl_visualiser.generators.generate_competition_dataset import create_competition_dataset


class TestCreateCompetitionDataset:
    def test_expected_behaviour(self):
        df = create_competition_dataset()
        assert isinstance(df, pd.DataFrame)
        assert df['date'].unique_counts().len() == 2
        assert df['name'].unique_counts().len() == 100
