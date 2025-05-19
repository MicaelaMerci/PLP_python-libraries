import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Load the dataset from a .txt file (makarina.txt)
df = pd.read_csv('makarina.txt')

# Display the DataFrame
print("Dataset Loaded:")
print(df)

# Task 2: Display summary statistics of the DataFrame
print("\nSummary Statistics:")
print(df.describe())

# Task 3: Perform some analysis - calculate the average marks per class
average_marks_per_class = df.groupby('Class')['Marks'].mean()
print("\nAverage Marks per Class:")
print(average_marks_per_class)

# Task 4: Plotting - Marks vs Age for each Class
plt.figure(figsize=(8, 5))
for label, df_class in df.groupby('Class'):
    plt.scatter(df_class['Age'], df_class['Marks'], label=label)

plt.title('Marks vs Age per Class')
plt.xlabel('Age')
plt.ylabel('Marks')
plt.legend()
plt.show()
