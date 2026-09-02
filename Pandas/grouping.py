import pandas as pd

df = pd.read_csv('career_choices_2026.csv')

print(df.groupby("Preferred_Career_2026")["Student_ID"].count())

print(df["Preferred_Career_2026"].unique())