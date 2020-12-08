import pandas as pd
import seaborn as sb

x = pd.read_html('https://github.com/mwaskom/seaborn-data/blob/master/tips.csv')
y = sb.load_dataset('tips')
print(y)
