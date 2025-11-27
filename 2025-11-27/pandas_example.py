import pandas as pd
import numpy as np
"""

file_path = './sales.csv'
data_frame = pd.read_csv(file_path)

print(data_frame.head()) """

data = {
    'Name':['Alice','Bob','Charlie','Elle','Bob','Bob'],
    'Age':[25,30,17,np.nan, 25,16],
    'City':['Rome','Milan','Naples','Rome','Rome','Milan']
}

df = pd.DataFrame(data)

print('OG dataframe:\n',df)

df_older = df[df['Age']>23]

print("Older than 23:\n",df_older)
df['State'] = ['Adult' if age > 18 else 'Child' for age in df['Age']]

print(df)

df_clean = df.dropna() # deletes nan
print(df_clean)

df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)
df_unique = df.drop_duplicates()
print(df_unique)

