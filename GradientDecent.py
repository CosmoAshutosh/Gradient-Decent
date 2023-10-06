import numpy as np
import math
from sympy import *
import numdifftools as nd


def gradient(fcn, var, var_x, var_y):
     x = Symbol('x')
     y = Symbol('y')

     df = diff(fcn, var)
     df = lambdify([x,y], df)
     return df(var_x, var_y)

def function_value(fcn, varx, vary):
     x = Symbol('x')
     y = Symbol('y')
     fcn = lambdify([x,y], fcn)

     return fcn(varx, vary)

def gradient_decent(function, learning_rate, iteration, x_start, y_start):
     X = x_start
     Y = y_start
     x = Symbol('x')
     y = Symbol('y')
     print("Our learning rate is :", learningRate)
     print("Our number of iterations is :", iteration)

     for i in range(1, iteration+1):
          grad_x = gradient(function, x, X, Y)
          grad_y = gradient(function, y, X, Y)

          new_X = X - (learning_rate*grad_x)
          X = new_X
          new_Y = Y - (learning_rate*grad_y)
          Y = new_Y

          print("New points in ",i ,"iteration is ", X, Y)
          
     print("Optimal points are : ", X, Y ,"and optimal value of the function is : ", function_value(function, X, Y))

input_expr = input('Enter an expression: ')
learningRate = float(input('Enter the learning rate: '))
Iteration = int(input('Enter number of iteration: '))
X_Start = int(input('Enter starting point of x: '))
Y_Start = int(input('Enter starting point of y: '))

value = gradient_decent(input_expr, learningRate, Iteration, X_Start, Y_Start)
print(value)