import numpy as np
import csv

np.random.seed(seed=1338)
names = ['low_correlation', 'high_correlation', 'no_correlation']


def get_random_correlation(correlation, n_items):
    cov = [[1, correlation], [correlation, 1]]
    L = np.linalg.cholesky(cov)
    uncorrelated = [np.random.rand(n_items), np.random.rand(n_items)]
    value, weight = np.dot(L, uncorrelated)
    return zip(value, weight)


def get_random(n_items):
    return zip(np.random.rand(n_items), np.random.rand(n_items))


def save_to_file(data, filename):
    with open(filename, mode='w') as file:
        fieldnames = ['value', 'weight']
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\r')
        writer.writeheader()
        for weight, value in data:
            writer.writerow({'value': value, 'weight': weight})


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        weights = []
        values = []
        is_first_line = True
        for row in reader:
            if not is_first_line:
                values.append(row[0])
                weights.append(row[1])
            else:
                is_first_line = False
    return np.array(weights, dtype='float64'), np.array(values, dtype='float64')
