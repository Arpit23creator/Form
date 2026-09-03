import pandas as pd

df1 = pd.read_csv('a.csv')
df2 = pd.read_csv('b.csv')

# print(df1.head(1))
# print(df1.head(2))

#concat function

print(pd.concat([df1, df2], axis=0)) #axis =0 -> stack rows(vertically)
print(pd.concat([df1, df2], axis=1))

# Merge function
#Data is related through a common column(joining two tables using a common ID)

'''
Types of merge(df1, df2, on="Student)



'''

df_inner_join = pd.merge(df1, df2, on="Student ID", how="inner")