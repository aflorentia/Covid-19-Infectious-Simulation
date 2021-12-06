import numpy as np
import matplotlib.pyplot as plt

from compute_M import compute_M


def plot_initial(A, B, C, P, N, D1, D2, S):
    X = np.linspace(A, B, C)
    # print(P)
    Y = list()
    for I in X:
        Mi = compute_M(P, int(I), N, D1, D2, S)
        Y.append(Mi)
        print(Y)
    fig, ax = plt.subplots()
    # ax.set_xlim(A,B)
    # ax.set_ylim(Y)
    ax.set(xlabel='Initial Cases (I)', ylabel='Max Infectious inhabitants (M)',
           title='Max Infectious inhabitants (M)/Initial Cases (I)')
    ax.grid()
    ax.plot(X, Y)
    plt.show()
