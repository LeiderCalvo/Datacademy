# a linear regression is the linear function that fits better all the known points
# this linear function y = m(x) + b must pass by the coordinates (mean of x, mean of y)

# we get x and y from the dataset provided, but we must find the slope (m) and the constant (b). To do that we use the the least squares formula to get (m) and then, use the linear function to find the constant value as shown here: https://i.stack.imgur.com/OjlaY.png

import numpy as np
import matplotlib.pyplot as plt

DATASET = {
    "x": (1,2,3,4,5),
    "y": (2,3,5,6,5)
}

def get_slope_and_constant(x,y):
    # least squares formula: m = Σ((x - x_mean) * (y - y_mean)) / Σ((x - x_mean)**2)
    x_mean, y_mean = np.mean(x), np.mean(y)
    m = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2)
    # linear function to get b: y = m(x) + b  =>  b = y - m(x)
    # y and x must be the mean of their values: b = y_mean - m(x_mean)
    b = y_mean - (m * x_mean)
    return (m, b)

def plot_regession(x, y, m, b):
    plt.scatter(x, y, marker = "o", color = 'g', s = 30)

    # linear function: y = m(x) + b
    y_pred = (m * x) + b
    plt.plot(x, y_pred, color = "b")

    plt.xlabel("x: independent var")
    plt.ylabel("y: dependent var")

    plt.show()

def run():
    x, y = np.array(DATASET["x"]), np.array(DATASET["y"])
    m_and_b = get_slope_and_constant(x, y)
    plot_regession(x, y, m_and_b[0], m_and_b[1])

if __name__ == "__main__":
    run()