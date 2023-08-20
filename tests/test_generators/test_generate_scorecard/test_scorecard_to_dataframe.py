import polars as pd

from bl_visualiser.generators.generate_scorecard import scorecard_to_dataframe, create_scorecard, ScoreCard


class TestScorecardToDataFrame:
    def test_expected_behaviour(self):
        scorecard = create_scorecard()
        df = scorecard_to_dataframe(scorecard)
        assert isinstance(df, pd.DataFrame)
