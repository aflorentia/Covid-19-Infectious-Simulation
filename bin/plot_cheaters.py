import numpy as np
from matplotlib import pyplot as plt
from compute_cheaters import compute_cheaters


def plot_cheaters(A, B, C, P, I, D1, D2, S):
    X = np.linspace(A, B, C)
    # print(X)
    Y = list()
    for M in X:
        # print(M)
        Ni = compute_cheaters(M, P, I, D1, D2, S)
        Y.append(Ni)
        print(Y)
    fig, ax = plt.subplots()
    ax.set(xlabel='Cheaters (N)', ylabel='Max Infectious inhabitants (M)',
           title='Max Infectious inhabitants (M)/Cheaters (N)')
    ax.grid()
    ax.plot(X, Y)
    plt.show()