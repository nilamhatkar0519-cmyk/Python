import pandas as pd 

data = pd.read_csv("marks.csv")
series = pd.Series(data["Marks"])
print("Pandas Series : ")
print(series)


## DataFrame
df = pd.read_csv("marks.csv")
print("\nPandas DataFrame : ")
print(df)

