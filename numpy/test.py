import numpy as np
import pandas as pd

x = ['a', 'b', 'c', 'd', 'e']
x2 = ['a', 'b', 'c', 'd', 'f']
y = [1, 2, 3, 4, 5]
z = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

a = pd.Series(y, x)
b = pd.Series(y, x2)

A = ['😊','😂','🤣','❤']
B = ['😊','😂','🤣','❤']
C = ['😊','😂','🤣','❤']
D = ['😊','😂','🤣','❤']
E = ['😊','😂','🤣','❤']

df = pd.DataFrame([A,B,C,D,E], ['a','b','c','d','e'], ['W','X','Y','Z'])
# Create Row and Coloumn
df['Other'] = df['Y'] + df['Z']
# Use inplace=True if you want delete permanent
df.drop('e')

#Accessing element in dataframe
df.loc['a']