import pandas as pd

file1 = "C:/Users/nero.onose/OneDrive - Venture Garden Group/Desktop/dana-air/CSV 3-Nov-2023-9J332-QOW-LOS P.csv"
file2 = "C:/Users/nero.onose/OneDrive - Venture Garden Group/Desktop/dana-air/CSV 03-Nov-2023 9J332 QOW-LOS PART01 085615.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Ensure that column names and indices match
df1 = df1.sort_index(axis=1).sort_index()
df2 = df2.sort_index(axis=1).sort_index()

# Compare DataFrames
# differences = df1.compare(df2)

# print("Differences:")
# print(differences)
print(df1)
print(df2)