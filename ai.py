import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing data
dataset_path = "C:\\Users\\GGPC\Documents\\ai_learning\\ai_testing\\Car_Purchasing_Data.xlsx"
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



# Create a histogram of the 'Age' column
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')
plt.show()
