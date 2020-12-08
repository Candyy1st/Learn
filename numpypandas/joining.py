import numpy as np
import pandas as pd

x1 = {'a':[1,2,3], 'b':[5,6,7]}
y1 = {'c':[3,4,5], 'd':[6,7,8]}

x = pd.DataFrame(x1, index=['p1', 'p2', 'p3'])
y = pd.DataFrame(y1, index=['p1', 'p2', 'p3'])
z = pd.DataFrame(y1, index=['p1', 'p4', 'p5'])

print(x)
print()
print(y)

xj = x.join(y)
xj1 = x.join(y, how='left')
xj2 = x.join(z, how='outer')
print(xj)
print(xj1)
print(xj2)