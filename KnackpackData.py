import random
import numpy as np
from numba.types import Omitted
from numba import jit,njit, prange,boolean,int32,float32

# Treated as constants by numba
np.random.seed(seed=1337)
max_weight = 3
n_items = 16
max_value = (2**n_items) 
weights =  np.random.rand(n_items)
values = np.random.rand(n_items)
items_size_threshold = 0.5

@njit([boolean[::1](int32)]) # return boolean array
def encodeNumber(number):
    return np.array([bool(number & (1<<(n_items-1-x))) for x in prange(n_items)],dtype=boolean)

@njit([float32(boolean[::1])])
def scoreFunction(mask):
    final_weight = 0
    score = 0 
    for i in range(weights.size):
        if mask[i]:
            final_weight+=weights[i]
            score+=values[i]
    return -1 if final_weight > max_weight else score

@njit([float32[::1]()]) # return float array
def getScores():
    return np.array([scoreFunction(encodeNumber(x)) for x in prange(max_value)],dtype=float32)

@njit([boolean[:,::1]()]) # return 2d boolean array
def getEncoded():
    return np.array([[boolean(number & (1<<(n_items-1-x))) for x in prange(n_items)] for number in prange(max_value)],dtype=boolean)
