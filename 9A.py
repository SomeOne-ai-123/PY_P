import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a dataset in a CSV file named 'dataset.csv'
# Replace 'dataset.csv' with your actual dataset file path
file_path = 'dataset.csv'

# Read the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# i. Visualize the dataset using plot()
df.plot()
plt.title('Dataset Visualization')
plt.show()

# ii. Draw the Scatter plot for the dataset on any column
# Let's assume you want to plot 'column_x' against 'column_y'
column_x = 'column_x'
column_y = 'column_y'
df.plot.scatter(x=column_x, y=column_y)
plt.title('Scatter Plot of {} vs {}'.format(column_x, column_y))
plt.show()

# iii. Display the scatter plot with different colors
# Let's say you have a categorical column 'category' that you want to use for coloring
color_column = 'category'
df.plot.scatter(x=column_x, y=column_y, c=df[color_column], cmap='viridis')
plt.title('Scatter Plot of {} vs {} (Colored by {})'.format(column_x, column_y, color_column))
plt.colorbar()
plt.show()

# iv. Draw the Histogram for the dataset on any column
# Let's draw a histogram for 'column_z'
column_z = 'column_z'
df[column_z].plot.hist(bins=20)
plt.title('Histogram of {}'.format(column_z))
plt.xlabel(column_z)
plt.ylabel('Frequency')
plt.show()
