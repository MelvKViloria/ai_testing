import pandas as pd

#importing data
dataset_path = "C:\\Users\\GGPC\\Documents\\ai_learning\\Car_Purchasing_Data.xlsx"
df = pd.read_excel(dataset_path)

print()

#head and tail / first and last 5 rows of the data
print(df.head())
print(df.tail())

print()

#shape
shape = df.shape
print("Number of rows:", shape[0])
print("Number of columns:", shape[1])

print()

#summary
print(df.info())

print()

#isnull
null_counts = df.isnull().sum()
print(null_counts)

print()

#overall stats
statistics = df.describe()
print(statistics)
