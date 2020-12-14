import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

a = plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Testing Matplotlib')

b = plt.subplot(3,2,1)
plt.plot(x,x, label='example')       #line
plt.title('Line')
plt.legend(loc=8)                        #add .legend to show label

c = plt.subplot(3,2,2)
plt.scatter(x,z, label='more')    #dot
plt.title('Dot')
plt.legend()

d = plt.subplot(3,2,3)
plt.hist(x,y)       #histogram
plt.title('Histogram')
e = plt.subplot(3,2,4)
plt.bar(x,y)
plt.title('Bar Graph')
f = plt.subplot(3,2,5)
plt.fill(x,y)
plt.title('Fill')
plt.tight_layout()

print(b)
print(c)
print(d)
print(e)
print(f)
