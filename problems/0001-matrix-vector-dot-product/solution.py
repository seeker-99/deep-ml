import numpy as np


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
    # Return a list where each element is the dot
    # product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match
    # the length of 'b', return -1.
    if len(a[0]) == len(b):
        req_len = len(b)
        vectr = [0] * req_len
        lim = len(a[0])
        for i in range(lim):
            # if i != lim - 1:
                j = 0
                while j < lim:
                    vectr[i] += a[i][j] * b[j]
                    j += 1
            # else:
            #     j = 0
            #     while j < lim:
            #         vectr[i] += a[i][j] * b[j]
            #         j += 1
        return vectr
    else:
        return -1