import pandas as pd

df = pd.read_csv('career_choices_2026.csv')

# print(df.groupby("Preferred_Career_2026")["Student_ID"].count())

# print(df["Preferred_Career_2026"].unique())

# print(df["Preferred_Career_2026"].value_counts())

#  Find the average expected salary for each career

print(df.groupby("Preferred_Career_2026")["Expected_Salary_LPA"].mean())