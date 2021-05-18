import numpy as np

np.random.seed(seed=1338)


def get_random_correlation(correlation, n_items):
    values = []
    weights = []
    cov = [[1, correlation], [correlation, 1]]
    L = np.linalg.cholesky(cov)
    uncorrelated = [np.random.rand(n_items), np.random.rand(n_items)]
    print(uncorrelated)
    value, weight = np.dot(L, uncorrelated)
    values.append(value)
    weights.append(weight)
    return values, weights


def get_random(n_items):
    return np.random.rand(n_items), np.random.rand(n_items)
