__author__ = 'orlykor12'

import numpy as np

class LeastSquare:
    def __init__(self, deg):
        self.deg = deg
        self.h = None

    def train(self, X, y):
        X_phi = self.phi(X)
        pass

    def error(self, X, y):
        pass

    #returns the vandermonde matrix
    def phi(self, X):
        pass