import numpy as np

from bl_visualiser.generators.generate_scores import create_distribution


class TestCreateDistribution:

    def test_expected_behaviour(self):
        scores = create_distribution()
        assert len(scores) == 30
        assert np.allclose(min(scores), 0)
        assert np.allclose(max(scores), 10)
