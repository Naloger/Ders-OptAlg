import numpy as np

# Initialize variables
x0_start = 2
iterations =50
step_size = 0.01

x = x0_start

# Compute initial gradient

r = 2 * x0_start + 2
d = -r  # Initial direction is the negative gradient

for i in range(iterations):
    f = x**2 + 2*x - 1  # Objective function
    f_grad = 2*x + 2  # Gradient
    
    # Update x
    x = x + step_size * d
    
    # New gradient
    r_new = 2*x + 2
    
    # Update direction (d)
    beta = (np.dot(r_new, r_new) / np.dot(r, r))
    d = -r_new + beta * d
    
    r = r_new  # Update residual
    
    print(f"Iteration:{i+1} , x: {x}, f: {f}")