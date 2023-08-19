from copy import deepcopy
import numpy as np

from sklearn.preprocessing import minmax_scale


def create_scores() -> np.ndarray:
    number_of_scores = 30
    scores = minmax_scale(
        np.random.exponential(
            size=number_of_scores
        ).cumsum() + np.random.random(number_of_scores)

    )
    return np.sort(scores)[::-1] * 10


def bin_scores(array: np.ndarray) -> np.ndarray:
    new_array = deepcopy(array)

    boundaries = [
        array.max()+1,
        8.5,
        5.5,
        2.5,
        0.5,
        array.min()-1
    ]

    scores = [10, 7, 4, 1, 0]

    for sc, st, ed in zip(scores, boundaries[:-1], boundaries[1:]):
        new_array[np.logical_and(st > array, array > ed)] = sc

    return new_array.astype('uint8')
