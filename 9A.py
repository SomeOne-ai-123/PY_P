import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
# Replace 'your_dataset.csv' with the path to your dataset
df = pd.read_csv('your_dataset.csv')

# i. Visualize the dataset using plot()
df.plot()
plt.title('Dataset Visualization')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()

# ii. Draw the Scatter plot for the dataset on any column
# Replace 'column_name' with the actual column name you want to plot
df.plot.scatter(x='column_name', y='another_column_name')
plt.title('Scatter Plot')
plt.xlabel('Column Name')
plt.ylabel('Another Column Name')
plt.show()

# iii. Display the scatter plot with different colors
colors = df['color_column_name']  # Replace 'color_column_name' with the column name used for coloring
df.plot.scatter(x='column_name', y='another_column_name', c=colors, colormap='viridis')
plt.title('Scatter Plot with Colors')
plt.xlabel('Column Name')
plt.ylabel('Another Column Name')
plt.show()

# iv. Draw the Histogram for the dataset on any column
# Replace 'column_name' with the actual column name you want to plot
df['column_name'].plot.hist(bins=30, alpha=0.5)
plt.title('Histogram')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.show()
