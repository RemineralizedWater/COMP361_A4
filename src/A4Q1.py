# Written by Michael Rowe 26101267
# COMP 361 A4

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

fxNum = 0
n = 2
M = 501

while fxNum <= 2:
    while n <= 16:
        # Graph points
        if fxNum == 0:
            x = np.linspace(-1, 1, n+1)
            for i in range(0, len(x)):
                x[i] = round(x[i], 4)
            y = np.sin(np.pi * x)
            maxInfNorm = round(y[0], 15)
            for i in range(0, len(y)):
                y[i] = round(y[i], 15)
                if maxInfNorm <= y[i]:
                    maxInfNorm = y[i]
        if fxNum == 1:
            x = np.linspace(-2, 2, n+1)
            for i in range(0, len(x)):
                x[i] = round(x[i], 4)
            y = 1 / (1 + pow(x, 2))
            for i in range(0, len(y)):
                y[i] = round(y[i], 15)
        if fxNum == 2:
            x = np.linspace(-5, 5, n+1)
            for i in range(0, len(x)):
                x[i] = round(x[i], 4)
            y = 1 / (1 + pow(x, 2))
            for i in range(0, len(y)):
                y[i] = round(y[i], 15)
        plt.figure()
        plt.plot(x, y, 'ro')

        # Graph p(x) Lagrange
        if fxNum == 0:
            comp = np.linspace(-1, 1, len(x))
        if fxNum == 1:
            comp = np.linspace(-2, 2, len(x))
        if fxNum == 2:
            comp = np.linspace(-5, 5, len(x))
        for i in range(0, len(x)):
            comp[i] = round(comp[i], 4)
        px = lagrange(comp, x)
        py = lagrange(comp, y)
        x = compLag = np.linspace(comp[0], comp[-1], M)
        for i in range(0, len(x)):
            x[i] = compLag[i] = round(compLag[i], 4)
        xLagCoord = px(compLag)
        yLagCoord = py(compLag)
        plt.plot(xLagCoord, yLagCoord)

        # Graph f(x)
        y = np.sin(np.pi * x)
        if fxNum == 0:
            y = np.sin(np.pi * x)
        if fxNum == 1:
            y = 1 / (1 + pow(x, 2))
        if fxNum == 2:
            y = 1 / (1 + pow(x, 2))
        plt.plot(x, y)

        plt.show()

        # Calculate approximate maximum interpolation error
        index = 0
        maximum = abs(y[index] - yLagCoord[index])
        for i in range(0, len(y)):
            if maximum < abs(y[i] - yLagCoord[i]):
                maximum = abs(y[i] - yLagCoord[i])
                index = i
        if fxNum == 0:
            print("For f(x) = sin(pi*x) on [-1,1] & n =", n, ", the approximate maximum interpolation error =", maximum, ", at x =", x[index], ", M =", index)
            if n == 2:
                maxW = 0.3849
                upper = maxInfNorm*maxW/np.math.factorial(n+1)
                print("For f(x) = sin(pi*x) on [-1,1] & n =", n, ", max|w(n+1)(x)|=", maxW, ", ||f^(",(n+1),")(x)||infinity =", maxInfNorm, ", Error Upper Bound =", upper)
            if n == 4:
                maxW = 0.11348
                upper = maxInfNorm*maxW/np.math.factorial(n+1)
                print("For f(x) = sin(pi*x) on [-1,1] & n =", n, ", max|w(n+1)(x)|=", maxW, ", ||f^(",(n+1),")(x)||infinity =", maxInfNorm, ", Error Upper Bound =", upper)
            if n == 8:
                maxW = 0.01877
                upper = maxInfNorm*maxW/np.math.factorial(n+1)
                print("For f(x) = sin(pi*x) on [-1,1] & n =", n, ", max|w(n+1)(x)|=", maxW, ", ||f^(",(n+1),")(x)||infinity =", maxInfNorm, ", Error Upper Bound =", upper)
            if n == 16:
                maxW = 0.00095
                upper = maxInfNorm*maxW/np.math.factorial(n+1)
                print("For f(x) = sin(pi*x) on [-1,1] & n =", n, ", max|w(n+1)(x)|=", maxW, ", ||f^(",(n+1),")(x)||infinity =", maxInfNorm, ", Error Upper Bound =", upper)
        if fxNum == 1:
            print("For f(x) = 1/(1+x^2) on [-2,2] & n =", n, ", the approximate maximum interpolation error =", maximum, ", at x =", x[index], ", M =", index)
        if fxNum == 2:
            print("For f(x) = 1/(1+x^2) on [-5,5] & n =", n, ", the approximate maximum interpolation error =", maximum, ", at x =", x[index], ", M =", index)

        n *= 2
    n = 2
    fxNum += 1
