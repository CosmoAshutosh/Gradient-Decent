import numpy as np
from sympy import Symbol, diff, lambdify

def gradient(fcn, var, var_x, var_y):
    x, y = Symbol('x'), Symbol('y')
    df = diff(fcn, var)
    df = lambdify([x, y], df)
    return df(var_x, var_y)

def function_value(fcn, varx, vary):
    x, y = Symbol('x'), Symbol('y')
    fcn = lambdify([x, y], fcn)
    return fcn(varx, vary)

def gradient_descent(function, learning_rate, iteration, x_start, y_start):
    x, y = Symbol('x'), Symbol('y')
    X, Y = x_start, y_start

    for _ in range(iteration):
        grad_x = gradient(function, x, X, Y)
        grad_y = gradient(function, y, X, Y)

        X -= learning_rate * grad_x
        Y -= learning_rate * grad_y

    optimal_value = function_value(function, X, Y)
    return X, Y, optimal_value

input_expr = input('Enter an expression: ')
learning_rate = float(input('Enter the learning rate: '))
iteration = int(input('Enter number of iterations: '))
X_start = int(input('Enter starting point of x: '))
Y_start = int(input('Enter starting point of y: '))

optimal_points = gradient_descent(input_expr, learning_rate, iteration, X_start, Y_start)
print("Optimal points are:", optimal_points[:2], "and optimal value of the function is:", optimal_points[2])