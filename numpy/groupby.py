# analysing data using groupby

import numpy as np
import pandas as pd

a = {
    'item':['apple','apple','orange','orange','guns','guns','guns'],
    'days':['mon','tue','wed','thu','fri','sat','sun'],
    'sales':[100,80,200,100,5,10,5]
}

df = pd.DataFrame(a)
print(df)

x = df.groupby('item').mean() #average item on days nd sales
x1 = df.groupby('item').count() #counting item on days nd sales
x2 = df.groupby('item').max() #showing max item on days nd sales
x3 = df.groupby('item').describe()
x4 = df.groupby('item').describe().transpose()
print(x)
print(x1)
print(x2)
print(x3)
print(x4)