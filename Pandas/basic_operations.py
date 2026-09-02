import pandas as pd

df = pd.read_csv('career_choices_2026.csv')

# print(df['Preferred_Career_2026'])

# print(df[['Preferred_Career_2026', 'Age']])

#slicing - 2 ways (loc and iloc)
#loc

# print(df.loc[0:5,["Preferred_Career_2026","Age"]])

# print(df.iloc[0:5,[2, 5]])

print(df.iloc[0:5,2:5]) #using iloc , it does include upper limit of slicing