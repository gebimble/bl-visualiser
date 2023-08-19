import numpy as np
from bl_visualiser.distribution_functions import create_scores


class TestCreateScores:

    def test_expected_behaviour(self):
        scores = create_scores()
        assert len(scores) == 30
        assert np.allclose(min(scores), 0)
        assert np.allclose(max(scores), 10)
