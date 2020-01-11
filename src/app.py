# Import Libraries
import matplotlib.pyplot as plt
import numpy as np


# Cost Function
def f(x):
    return x ** 2 + x + 1


# Make Data
x_1 = np.linspace(start=-3, stop=3, num=100)


# Plot Data

# plt.xlim([-3, 3])
# plt.ylim([0, 8])
# plt.xlabel('X', fontsize=16)
# plt.ylabel('f(x)', fontsize=16)
# plt.plot(x_1, f(x_1))
# plt.show()


# Slope and Derivatives
def df(x):
    return 2 * x + 1


# Plot Derivative Along Side Actual Data

plt.figure(figsize=[12, 15])

# GRAPH 1
plt.subplot(2, 1, 1)
plt.xlim([-3, 3])
plt.ylim([0, 8])
plt.title('Cost Function', fontsize=17)
plt.xlabel('X', fontsize=16)
plt.ylabel('f(x)', fontsize=16)
plt.plot(x_1, f(x_1), color='blue', linewidth=3)

# GRAPH 2
plt.subplot(2, 1, 2)
plt.xlim([-2, 3])
plt.ylim([-3, 6])
plt.title('Derivative', fontsize=17)
plt.xlabel('X', fontsize=16)
plt.ylabel('df(x)', fontsize=16)
plt.grid()
plt.plot(x_1, df(x_1), color='skyblue', linewidth=5)

plt.show()
