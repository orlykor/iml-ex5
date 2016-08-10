__author__ = 'orlykor12'

import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
def main():

    instances = np.load("X_poly.npy")
    labels = np.load("Y_poly.npy")

    train_x = instances[:99]
    train_y = labels[:99]
    validation_x = instances[100:199]
    validation_y = labels[100:199]
    test_x = instances[200:299]
    test_y = instances[200:299]
    num_deg = 15
    w = []
    for i in range(num_deg):
        vander_train = np.vander(train_x,i)
        vander_train_inverse = np.linalg.pinv(vander_train)

if __name__ == "__main__":
    main()