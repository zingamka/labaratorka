import numpy as np


def neville(x, y, t):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            Q[i][j] = ((t - x[i + j]) * Q[i][j - 1] + (x[i] - t) * Q[i + 1][j - 1]) / (x[i] - x[i + j])

    return Q[0][n - 1]


# Пример использования
x = np.linspace(-3, 3, 4)
y = 1 / np.arctan(1 + x ** 2)

print("n = 4")
print("f(1.5) =", neville(x, y, 1.5))
print("f(2.5) =", neville(x, y, 2.5))

x = np.linspace(-3, 3, 6)
y = 1 / np.arctan(1 + x ** 2)

print("n = 6")
print("f(1.5) =", neville(x, y, 1.5))
print("f(2.5) =", neville(x, y, 2.5))

x = np.linspace(-3, 3, 10)
y = 1 / np.arctan(1 + x ** 2)

print("n = 10")
print("f(1.5) =", neville(x, y, 1.5))
print("f(2.5) =", neville(x, y, 2.5))