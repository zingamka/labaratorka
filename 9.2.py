import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# функция
def f(x):
    return 1 / np.arctan(1 + x**2)

# Определение узлов интерполяции
a = -3
b = 3
n1 = 4
n2 = 6
n3 = 10
x1 = np.linspace(a, b, n1)
x2 = np.linspace(a, b, n2)
x3 = np.linspace(a, b, n3)
y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

# Создание объектов интерполяции для каждого числа узлов
f1 = interp1d(x1, y1, kind='linear')
f2 = interp1d(x2, y2, kind='linear')
f3 = interp1d(x3, y3, kind='linear')

# Определение интервалов, на которых будет вычисляться значение функции
x = np.linspace(a, b, 1000)

# графики
plt.plot(x, f(x), label='f(x)')
plt.plot(x1, y1, 'o', label='узлы (n=4)')
plt.plot(x2, y2, 'o', label='узлы (n=6)')
plt.plot(x3, y3, 'o', label='узлы (n=10)')
plt.plot(x, f1(x), label='интерп. полином (n=4)')
plt.plot(x, f2(x), label='интерп. полином (n=6)')
plt.plot(x, f3(x), label='интерп. полином (n=10)')
plt.legend()
plt.show()