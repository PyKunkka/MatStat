import numpy as np


def get_count_bins(num):
    if num < 100:
        if num % 2 == 0:
            num_b = np.sqrt(num)-1
        else:
            num_b = np.sqrt(num)
    else:
        if num % 2 == 0:
            num_b = np.cbrt(num)-1
        else:
            num_b = np.cbrt(num)
    return num_b


