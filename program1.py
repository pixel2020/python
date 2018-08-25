import pandas as pd
print('test')


url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c=pd.read_csv(url)
print(c)