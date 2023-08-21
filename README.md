# ai_testing
 python

Use the given dataset to perform the followings tasks:

Car_Purchasing_Data.csv
Analyze the dataset by implementing the following operations using pandas:

Import the dataset
Display the first 5 rows of the dataset (head)
Display the last 5 rows of the dataset (tail)
Determine the shape of the dataset (shape - Total number of rows and columns)
Display the concise summary of the dataset (info)
Check the null values in dataset (isnull)
Get overall statistics about dataset (describe)

Create the input dataset from the original dataset by dropping the irrelevant features
Create the output dataset from the original dataset.
Transform the input dataset into a percentage based weighted value between 0 and 1.
Transform the output dataset into a percentage based weighted value between 0 and 1.
(Hint: for output dataset it may require to reshape it first)
Split the dataset into the training set and test set
Print the shape of train and test set data set
Print the first few rows from the train and test data set

(To understand the relationships among various columns in your dataset and select independent variables, target variables, and irrelevant features, you can use various visualization libraries. One of the most commonly used libraries for this purpose is Seaborn, which is built on top of Matplotlib and provides more aesthetically pleasing and informative visualizations. Here are some Seaborn plots you can use for exploratory data analysis:)

1. **Pair Plot**: To visualize pairwise relationships among multiple variables.

2. **line Plot**: also known as a line chart or time series plot, is used to visualize the relationship between two continuous variables over time or another continuous dimension.

3. **Histogram**: To visualize the distribution of a single numeric variable.

Create the input dataset from the original dataset by dropping the irrelevant features:

In this step, you identify features (columns) in your original dataset that are not relevant to your analysis or machine learning task and remove them. Irrelevant features can include those that don't contribute much information, are redundant, or have no direct impact on the output.

Create the output dataset from the original dataset:

The output dataset, often referred to as the target or label dataset, contains the values you're trying to predict or classify. Depending on your task (regression, classification, etc.), this dataset might contain continuous values (regression) or discrete classes (classification).

Transform the input dataset into a percentage-based weighted value between 0 and 1:

To standardize and normalize the input data, you might use techniques like Min-Max Scaling. This process scales the features so that they fall within the range of 0 to 1, with 0 being the minimum value of the feature and 1 being the maximum value.

Transform the output dataset into a percentage-based weighted value between 0 and 1:

Similar to the input dataset, you'll need to scale the output data, especially if it's a regression task with continuous values. This ensures that the target values are also within the 0 to 1 range.

Reshape the output dataset (if needed):

If the output dataset was initially in a format that doesn't match the expected shape for the machine learning model (e.g., a matrix instead of a vector), you might need to reshape it accordingly.

Split the dataset into the training set and test set:

It's important to split your data into two sets: one for training the machine learning model and the other for evaluating its performance. A common split ratio is around 70-80% for training and 20-30% for testing. This helps you assess how well your model generalizes to new, unseen data.

Print the shape of the train and test set datasets:

You can print the number of rows and columns in each of the training and test datasets to get an idea of their dimensions. This helps ensure that the split was done correctly and gives you an overview of the data size.

Print the first few rows from the train and test datasets:

Printing a few rows from each dataset helps you visually inspect the data and confirm that it has been split and preprocessed as intended. This step is important for understanding the structure and content of the data you'll be working with.

pip install -U scikit-learn