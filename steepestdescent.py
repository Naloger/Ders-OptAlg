import numpy
import sympy


x0_start = 2
iteration = 100
step_size = 0.01

x = x0_start


for i in range(iteration):
    f = x**2 + 2*x -1 
    f_grad = 2*x + 2 
    x = x - step_size*f_grad

    print(f"Iteration:{i+1} , x: {x}, f: {f}")