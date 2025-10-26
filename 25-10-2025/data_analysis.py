import pandas as pd

df=pd.read_csv("D:\Chetan Pande\AI-ML-2025\Python_Practise\Python-Programming\data\sample.csv")

print(df)
print('************')
#calculate  means  for numeric  columns
print(df.describe())