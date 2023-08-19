import numpy as np

from bl_visualiser.distribution_functions import bin_scores


class TestBinScores:
    def test_expected_behaviour(self):
        scores = np.random.randint(
            0, 10, size=np.random.randint(1000)).astype(float)
        binned_scores = bin_scores(scores)

        assert binned_scores.dtype is np.dtype('uint8')
        assert not set(binned_scores).difference({0, 1, 4, 7, 10})
