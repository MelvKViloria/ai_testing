import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing data
dataset_path = "C:\\Users\\Mkbv2\\Downloads\\ai_testing\\Car_Purchasing_Data.xlsx"
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



# Create a pairplot of the 'Age' column seaborn pairplot
sns.pairplot(df, vars=['Age', 'Annual Salary'])
plt.suptitle('Pair Plot of Age and Annual Salary', y=1.02)
plt.show()


# Create a lineplot of the 'Age' column seaborn lineplot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Age', y='Annual Salary', color='green', marker='o', markersize=6)
plt.xlabel('Age')
plt.ylabel('Annual Salary')
plt.title('Line Plot of Age vs. Annual Salary')
plt.grid(True)
plt.show()

# Create a histogram of the 'Age' column seaborn
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=20, color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')
plt.show()