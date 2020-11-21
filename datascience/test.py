import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = [[1,2,3],[4,5,6],[7,8,9]]

a = np.array(x)
print(a)

x = np.linspace(0,10,100)
y = x ** 2
z = plt.plot(x,y)
z = plt.show()
print(z)