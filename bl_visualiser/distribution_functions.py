from copy import deepcopy
import numpy as np


def rescale(array: np.ndarray) -> np.ndarray:
    mi, ma = array.min(), array.max()
    return (array-mi)/(ma-mi)


def create_scores() -> np.ndarray:
    number_of_scores = 30
    scores = (rescale(np.random.exponential(size=number_of_scores).cumsum())*10
              + np.random.random(number_of_scores))
    return np.sort(scores)[::-1]


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

    return new_array.astype(int)
