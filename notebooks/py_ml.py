import numpy as np


class PyML:

    def __init__(self):
        pass

    def simple_ols(X, y):
        """Function to perform simple OLS regression using basic python

        Parameters:
        X - single feature np array or list
        y - target np array or list
        """

        X_bar = np.mean(X)
        y_bar = np.mean(y)

        num_list = [(X[i] - X_bar) * (y[i] - y_bar) for i in range(len(X))]
        denom_list = [(X[i] - X_bar)**2 for i in range(len(X))]

        # slope
        b1 = sum(num_list) / sum(denom_list)

        # intercept
        b0 = y_bar - b1 * X_bar

        return b0, b1
