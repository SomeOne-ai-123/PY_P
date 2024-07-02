import pandas as pd
import matplotlib.pyplot as plt

# Path to your dataset
file_path = 'sample.csv'  # Make sure 'sample.csv' is in the same directory as your script

try:
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # i. Visualize the dataset using plot()
    df.plot()
    plt.title('Dataset Visualization')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()

    # ii. Draw the Scatter plot for the dataset on any column
    # Replace 'column_name' and 'another_column_name' with actual column names in your dataset
    df.plot.scatter(x='column_name', y='another_column_name')
    plt.title('Scatter Plot')
    plt.xlabel('Column Name')
    plt.ylabel('Another Column Name')
    plt.show()

    # iii. Display the scatter plot with different colors
    # Replace 'color_column_name' with the actual column name used for coloring
    colors = df['color_column_name']
    df.plot.scatter(x='column_name', y='another_column_name', c=colors, colormap='viridis')
    plt.title('Scatter Plot with Colors')
    plt.xlabel('Column Name')
    plt.ylabel('Another Column Name')
    plt.show()

    # iv. Draw the Histogram for the dataset on any column
    # Replace 'column_name' with actual column name in your dataset
    df['column_name'].plot.hist(bins=30, alpha=0.5)
    plt.title('Histogram')
    plt.xlabel('Column Name')
    plt.ylabel('Frequency')
    plt.show()

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("The file specified does not exist. Please check the file path and name.")
except pd.errors.EmptyDataError as e:
    print(f"Error: {e}")
    print("The file is empty. Please provide a valid dataset.")
except pd.errors.ParserError as e:
    print(f"Error: {e}")
    print("Error parsing the file. Please check the file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution of the dataset visualization is complete.")
