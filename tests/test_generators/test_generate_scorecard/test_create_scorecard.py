from bl_visualiser.generators.generate_scorecard import create_scorecard, Sex

from tests.test_generators.test_generate_scores.test_create_scores import TestCreateScores


tcs = TestCreateScores()


class TestCreateScorecard:
    def test_expected_behaviour(self):
        scorecard_1 = create_scorecard()
        scorecard_2 = create_scorecard()
        scorecards = (scorecard_1, scorecard_2)

        assert all(
            [
                (name := sc.name) is not None
                and isinstance(name, str)
                for sc in scorecards
            ]
        )
        # cannot have the same name
        assert scorecard_1.name != scorecard_2.name

        assert all(
            [
                (age := sc.age) is not None
                and isinstance(age, int)
                for sc in scorecards
            ]
        )

        # ages can be the same, so no test for that

        assert all(
            [

                (sex := sc.sex) is not None
                and sex in Sex
                for sc in scorecards
            ]
        )

        # sexes can be the same, so no test for that

        for sc in scorecards:
            tcs.test_expected_behaviour(sc.scores)

        for sc in scorecards:
            assert sc.routes is not None
