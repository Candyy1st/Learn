import numpy as np
import pandas as pd

def inc(x):
    x = x + 100
    return x

x = pd.DataFrame ({'a':[3,4,1,5,2], 'b':[40,50,30,40,20]})
print(x)
print()


#sort values
x = x.sort_values('a')
print(x)
print()

#to search unique nd nunique values
x = x['a'].unique()
print(x)
pass
x = x['b'].nunique()
print(x)

#apply function to column 'b'
x = x['b'].apply(inc)
print(x)
print()