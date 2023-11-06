import numpy as np


def f(x, a=12, b=-0.3, c=1.21, d=0.22):
    return a * x[0] + b * x[1] + np.exp(c * x[0]**2 * x[0] + d * x[1]**2)

def grad_f(x, a=12, b=-0.3, c=1.21, d=0.22):
    return np.array([a + 2 * 2.718281828 * c * x[0], b + d * x[1] * 2.718281828])

def steepest_descent(f, grad_f, x0, eps=1e-6, max_iter=1000, alpha=0.1):
    x = x0
    for i in range(max_iter):
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps:
            return x

        x = x - alpha * grad
    return x


x0 = np.array([0, 0])
x_min = steepest_descent(f, grad_f, x0)

print("Минимум функции:", f(x_min))
print("x, y, при которых достигается минимум: [", x_min[0],", " , x_min[1], "]")