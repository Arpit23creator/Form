import pandas as pd

df = pd.read_csv('career_choices_2026.csv')


# These are students expecting more than 20 LPA
# print(df[df['Expected_Salary_LPA'] > 20])

# These are the students interested in Generative AI
# print(df[df['Interested_in_Generative_AI'] == "Yes"])

# print(df[df['Preferred_Career_2026'] == "Data Scientist"])

print(df['Expected_Salary_LPA'].mean())