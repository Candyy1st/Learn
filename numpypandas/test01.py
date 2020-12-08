import numpy as np
import pandas as pd

a = {'a':[1,2,3,4,5],
     'b':[6,7,8,9,np.nan],
     'c':[0,1,2,np.nan,np.nan],
     'd':[3,4,np.nan,np.nan,np.nan],
     'e':[5,np.nan,np.nan,np.nan,np.nan]
     }

df = pd.DataFrame(a)
print(df)
print()
df1 = df.dropna(axis=0)
df2 = df.dropna(axis=1)
df3 = df.dropna(thresh = 3)
print()
#to replace NaN with the value
df4 = df.fillna(1)
df5 = df['b'].fillna(value=1) #only replace row b
df6 = df['b'].fillna(value= df['b'].mean()) #only replace NaN in row b with average on row b

print(df1)
print(df2)
print(df3)
print(df4)