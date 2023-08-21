import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


#importing data
dataset_path = "C:\\Users\\Mkbv2\\Downloads\\ai_testing\\Car_Purchasing_Data.xlsx"
df = pd.read_excel(dataset_path)

print()

#list of irrelevant features
irrelevant = ['Customer Name', 'Customer e-mail', 'Country']
#new data without ^
input_df = df.drop(columns=irrelevant)

#prints the new data
print(input_df.head())

#output data
output_df = df[['Car Purchase Amount']]
#this outputs this only ^
print(output_df.head())