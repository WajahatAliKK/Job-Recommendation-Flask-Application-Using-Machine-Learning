import pandas as pd


df = pd.read_csv("Questions.csv")
df = df.sample(10)
for index, row in df.iterrows():
    print(row['Correct'])
