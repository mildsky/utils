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

if __name__ == '__main__':
    # p = 0
    # p  = p + binom(20, 17) * (0.8 ** 17) * (0.2 ** 3)
    # p  = p + binom(20, 18) * (0.8 ** 18) * (0.2 ** 2)
    # p  = p + binom(20, 19) * (0.8 ** 19) * (0.2 ** 1)
    # p  = p + binom(20, 20) * (0.8 ** 20) * (0.2 ** 0)
    # print(p)
    # print(1 - p)
    # p = 0
    # p = p + binom(12,10) * 0.788 ** 10 * 0.212 ** 2
    # p = p + binom(12,11) * 0.788 ** 11 * 0.212 ** 1
    # p = p + binom(12,12) * 0.788 ** 12 * 0.212 ** 0
    # print(p)
    # print(1-p)
    # p = 0
    # p = p + 6 ** 0 * math.exp(-6) / math.factorial(0)
    # p = p + 6 ** 1 * math.exp(-6) / math.factorial(1)
    # p = p + 6 ** 2 * math.exp(-6) / math.factorial(2)
    # p = p + 6 ** 3 * math.exp(-6) / math.factorial(3)
    # p = p + 6 ** 4 * math.exp(-6) / math.factorial(4)
    # print(p)
    # print(math.factorial(22)/(math.factorial(5)*math.factorial(5)*math.factorial(5)*math.factorial(7))*.08**5*.19**5*.42**5*.31**7)
    # print(Gamma(7.2))
    print(Gamma(7.2+2.3)/(Gamma(7.2)*Gamma(2.3)))
    print(97.34836052512742 * 0.008867)
    exit()