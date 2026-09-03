import pandas as pd

df1 = pd.DataFrame({
"Student_ID":[1, 2, 3, 4],
"Name":["Anu", "Neha", "Zubin", "Rohit"],

}
)

df1.to_csv('a.csv')

df2 = pd.DataFrame({
"Student_ID":[2, 3, 4, 5],
"Project":["ML", "AI", "Web", "Data science"]

})

df2.to_csv('b.csv')