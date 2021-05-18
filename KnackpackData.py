import random
import numpy as np
from numba.types import Omitted
from numba import jit, njit, prange, boolean, int32, float32
from DataGenerator import get_random_correlation

# Treated as constants by numba
max_weight = 3
n_items = 16
max_value = (2 ** n_items)
weights, values = get_random_correlation(n_items, 0.1)
items_size_threshold = 0.5


@njit([boolean[::1](int32)])  # return boolean array
def encodeNumber(number):
    return np.array([bool(number & (1 << (n_items - 1 - x))) for x in prange(n_items)], dtype=boolean)


@njit([float32(boolean[::1])])
def scoreFunction(mask):
    final_weight = 0
    score = 0
    for i in range(weights.size):
        if mask[i]:
            final_weight += weights[i]
            score += values[i]
    return -1 if final_weight > max_weight else score


@njit([float32[::1]()])  # return float array
def getScores():
    return np.array([scoreFunction(encodeNumber(x)) for x in prange(max_value)], dtype=float32)


@njit([boolean[:, ::1]()])  # return 2d boolean array
def getEncoded():
    return np.array(
        [[boolean(number & (1 << (n_items - 1 - x))) for x in prange(n_items)] for number in prange(max_value)],
        dtype=boolean)


def getDiff(items, value, weight):
    ''' Najlepsze wartości dla max_weight = 3 '''
    return {
        15: [5.49080145 - value, 2.9546001 - weight],
        16: [4.9966826 - value, 2.89531816 - weight],
        17: [5.52658400 - value, 2.73215318 - weight],
        18: [4.78183345 - value, 2.93022193 - weight],
        19: [6.75288864 - value, 2.86703331 - weight],
        20: [6.06210077 - value, 2.97760480 - weight],
        21: [4.74507627 - value, 2.93439350 - weight],
    }[items]
