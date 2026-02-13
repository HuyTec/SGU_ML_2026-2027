import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
a = np.random.rand()
qty = 300
noise = 1.0
learning_rate = 0.1

x = np.linspace(-10, 10, qty)
noise_point = np.random.normal(0, noise, qty)
y = a*x + 1 + noise_point

def pointList(x,y):
    list = []
    for i, j in zip(x, y):
        list.append((i,j))
        pass
    return list

# Gradient Descedent
def cost_function(m, b, points):
    n = len(points)
    cost = 0.0
    for x, y in points:
        cost += (y - (m*x + b))**2
    return cost / n

def gradient_calc(m , b , points):
    n = len(points)
    gradient_m = 0.0
    for x, y in points:
        error = y - (m * x + b)
        gradient_m += x * error
        gradient_b += error
    return -2*gradient_m/n, -2*gradient_b/n 
    
def regression(points):
    for _ in range(len(points)):
        pass
    pass

if __name__ == "__main__":
    list = pointList(x,y)
    print(list)
    plt.figure(figsize=(6,6))
    plt.xlim(-10, 10)
    plt.scatter(x,y)
    plt.show()