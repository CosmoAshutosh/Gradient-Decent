# Gradient Descent Implementation
This is a Python implementation of the gradient descent algorithm for optimizing a mathematical function. Gradient descent is an optimization technique commonly used in machine learning and mathematical optimization to find the minimum (or maximum) of a function.

# Prerequisites
## Before you begin, ensure you have met the following requirements:

- [Python 3.x]
- [NumPy]
- [SymPy]
## You can install NumPy and SymPy using pip:

```
pip install numpy
pip install sympy
```
## Usage
- Clone the repository to your local machine or download the code.

- Run the gradient_descent.py script in your Python environment.

- You will be prompted to enter the following inputs:

  - [Mathematical expression of the function you want to optimize.]
  - [Learning rate: The step size for each iteration.]
  - [Number of iterations: The number of times the gradient descent algorithm will run.]
  - [Starting point for x and y.]
- The program will execute the gradient descent algorithm and provide you with the optimal points and the optimal value of the function.

## Example
Here's an example of how to use the code:

```
Enter an expression: x**2 + y**2
Enter the learning rate: 0.1
Enter number of iterations: 100
Enter starting point of x: 2
Enter starting point of y: 2
```
Output:

```
Our learning rate is : 0.1
Our number of iterations is : 100
New points in  1 iteration is  1.60000000000000 1.60000000000000
...
New points in  100 iteration is  0.00000000000000 0.00000000000000
Optimal points are :  0.00000000000000 0.00000000000000 and optimal value of the function is :  0.00000000000000
```
