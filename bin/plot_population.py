import numpy as np
import matplotlib.pyplot as plt
from compute_M import compute_M


def plot_population(A, B, C, I, N, D1, D2, S):
    X = np.linspace(A, B, C)
    # print(P)
    Y = list()
    for P in X:
        Mi = compute_M(int(P), I, N, D1, D2, S)
        Y.append(Mi)
        print(Y)
    fig, ax = plt.subplots()
    ax.set(xlabel='Population (P)', ylabel='Max Infectious inhabitants (M)',
           title='Max Infectious inhabitants (M)/Population(P)')
    ax.grid()
    ax.plot(X,Y)
    plt.show()