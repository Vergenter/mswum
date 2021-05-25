import random
import numpy as np
import matplotlib.pyplot as plt


def plot_best_of_all(scores):
    best_value_index = np.argmax(scores)
    plt.figure(figsize=(16, 12), dpi=80)
    plt.scatter(best_value_index, scores[
                best_value_index], color="r", s=200, zorder=2)
    plt.plot(range(len(scores)), scores, color="b", zorder=1)
    plt.title('Value changes')
    plt.ylabel('Value')
    plt.xlabel('Iteration')
    plt.show()


def plot_best_changes(scores):
    best_scores_table = np.array(scores)
    previousMax = scores[0]
    for i in range(best_scores_table.size):
        if best_scores_table[i] > previousMax:
            previousMax = best_scores_table[i]
        else:
            best_scores_table[i] = previousMax
    plt.figure(figsize=(16, 12), dpi=80)
    plt.plot(range(len(scores)),
             np.array(best_scores_table), color="b")
    plt.title('Best results changes')
    plt.ylabel('Value')
    plt.xlabel('Iteration')
    plt.show()


def drop_or_add_items(next_state, weights, min_weight, max_weight):
    while np.sum(weights[next_state]) < min_weight:
        idx = random.choice(np.where(next_state == False)[0])
        next_state[idx] = True

    while np.sum(weights[next_state]) > max_weight:
        idx = random.choice(np.where(next_state == True)[0])
        next_state[idx] = False

    return next_state


def fitness_of_individual(individual, values, weights):
    return np.sum(values[individual])


def simulatedAnnealing(initial_temp=1000, alpha=0.999, frozen_level=0.1, n_items=16, values=[], weights=[], max_weight=3, min_weight=None, starting_state=None):
    min_weight = max_weight - 1 if min_weight is None else min_weight
    fitness= lambda individual: fitness_of_individual(individual, values, weights)
    initial_state = np.zeros(n_items).astype(bool) 
    current_state = initial_state if starting_state is None else starting_state
    best_state = current_state
    temperature = initial_temp
    scores_table = [np.sum(values[initial_state])]
    it = 0
    while temperature > frozen_level:
        it += 1
        next_state = np.copy(current_state)
        next_state ^= np.array(
            [np.random.uniform() < temperature/initial_temp for _ in range(n_items)])
        next_state = drop_or_add_items(
            next_state, weights, min_weight, max_weight)

        scores_table.append(fitness(next_state))

        if fitness(next_state) > fitness(current_state):
            # If next state is better than current - set this state as current
            current_state = np.copy(next_state)
            if fitness(current_state) > fitness(best_state):
                    best_state = current_state
        else:
            # If the new solution is not better, accept it with a probability of e^(-delta/temp)
            acceptance_function = np.exp(-(1.0/np.sum(values[next_state]) - 1.0/np.sum(
                values[current_state])) / temperature)
            if acceptance_function > random.uniform(0, 1):
                current_state = np.copy(next_state)
        temperature = initial_temp*pow(alpha, it)
    return scores_table, best_state
