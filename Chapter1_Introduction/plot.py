__author__ = 'Shalom Yiblet'

import matplotlib
import pymc
import numpy as np

np.array()


def random_tuple():
    d = np.random.random_integers(1, 5, (1))
    x = []
    for i in range(d):
        x.append(np.random.random_integers(1, 5))

    return tuple(x)

def random_dimensional_tuple():
    z = random_tuple()
    x = []
    for i in range(len(z)):
        x.append([])
        i = -1
        while (len(z)+ i) > 1:
            for c in range(z[i]):
                z[c]




