import numpy as np

def to_categorical(x, n_col=None):
    x = np.asarray(x)
    if n_col is None:
        n_col = np.amax(x) + 1
    output = np.zeros((x.shape[0], n_col))
    output[np.arange(x.shape[0]), x] = 1
    return output