import pandas as pd

file_path = "new_gdp.csv"

df = pd.read_csv(file_path,)

df['GDP Per Capita'] = df['GDP Per Capita'].str.replace(',','')
df.to_csv('finalGdp.csv', index=False)