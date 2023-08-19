import numpy as np

from bl_visualiser.generate_data.generate_scores import create_scores


class TestCreateScores:

    def test_expected_behaviour(self):
        scores = create_scores()
        assert len(scores) == 30
        assert np.allclose(min(scores), 0)
        assert np.allclose(max(scores), 10)
        assert scores.dtype is np.dtype('uint8')
        assert not set(scores).difference({0, 1, 4, 7, 10})
