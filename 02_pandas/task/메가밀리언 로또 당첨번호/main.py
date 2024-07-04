import pandas as pd

df = pd.read_csv('data/mega_millions.csv')
df = pd.DataFrame(df.values, columns=['DataFrame', 'Winning Numbers', 'Mega Ball', 'Multiplier'])

df = pd.read_csv('data/mega_millions.csv', index_col=0)

print(df)