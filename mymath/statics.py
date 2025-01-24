import numpy as np
import math

def mean(data):
    return sum(data) / len(data)

def variance(data):
    return mean(data**2) - mean(data)**2

def sample_variance(data):
    return sum((data - mean(data))**2) / (len(data) - 1)

def binom(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def Gamma(k):
    ## gamma function
    # Gamma(k) = \int_0^\infty x^{k-1} e^{-x} dx
    # if k is an integer, then Gamma(k) = (k-1)!
    if k % 1 == 0:
        return math.factorial(k - 1)
    value = 0
    x = 0
    dx = 0.001
    while x < 100: # exp(-100) = 3.720075976020836e-44 is small enough
        value += x ** (k - 1) * math.exp(-x) * dx
        x += dx
    return value

def Covariance(X, Y):
    n = len(X)
    return sum((X - mean(X)) * (Y - mean(Y))) / (n - 1)

if __name__ == '__main__':
    # D = np.array([125, 250, 0, 100, -50, -75, 150, 300, 125, 200])
    # mu = mean(D)
    # print(D - mu)
    # print((D - mu) ** 2)
    # print(sum((D - mu) ** 2))
    # print(sum((D - mu) ** 2) / (len(D)-1))
    # print(mean(D))
    # print(sample_variance(D))
    # print(sample_variance(D) ** 0.5)
    x = np.array([10,12,14,15,18,19,23])
    y = np.array([25,30,36,37,42,50,55])
    xy = x @ y
    x_bar = mean(x)
    y_bar = mean(y)
    x_square = x @ x
    y_square = y @ y
    n = len(x)
    r = (xy - n * x_bar * y_bar) / (math.sqrt(x_square - n * x_bar ** 2) * math.sqrt(y_square - n * y_bar ** 2))
    # print(r)
    t = r * math.sqrt(n - 2) / math.sqrt(1 - r ** 2)
    # print(t)
    beta = (n * np.sum(x @ y) - np.sum(x) * np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2)
    # print(beta)
    alpha = y_bar - beta * x_bar
    # print(alpha)
    # print(alpha + beta * 8)
    SSE = np.sum(y ** 2) - alpha * np.sum(y) - beta * np.sum(x @ y)
    # print(SSE)
    var = SSE / (n - 2)
    # print(var)
    sigma = math.sqrt(var)
    # print(sigma)
    t = 2.571
    SXX = np.sum(x ** 2) - np.sum(x) ** 2 / n
    # print(beta - t * sigma / math.sqrt(SXX), beta + t * sigma / math.sqrt(SXX))
    print(alpha + beta * 20)
    print(alpha + beta * 20 - math.sqrt(1 + 1/n + (20 - x_bar) ** 2 / SXX) * sigma * t)
    print(alpha + beta * 20 + math.sqrt(1 + 1/n + (20 - x_bar) ** 2 / SXX) * sigma * t)
    SST = np.sum(y ** 2) - n * y_bar ** 2
    print(SST)