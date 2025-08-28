# -----------------------------
# Importing Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Enable inline plotting if in Jupyter
# %matplotlib inline

# -----------------------------
# Task 1: Load and Explore Dataset
# -----------------------------
try:
    # Load the Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame

    # Display first 5 rows
    print("First 5 rows of dataset:")
    print(df.head())

    # Dataset info
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values in dataset:")
    print(df.isnull().sum())

    # Clean dataset (no missing values in Iris, but this is how you’d handle it)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print("An error occurred:", e)


# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean
print("\nMean values per species:")
print(df.groupby("target").mean())

# Interesting finding
print("\nObservation: Sepal length and petal length clearly differ by species.")


# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1. Line chart: show petal length trend over first 50 samples
plt.figure(figsize=(8,5))
plt.plot(df.index[:50], df["petal length (cm)"][:50], marker='o')
plt.title("Petal Length Trend (First 50 Samples)")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar chart: average petal length per species
plt.figure(figsize=(6,5))
df.groupby("target")["petal length (cm)"].mean().plot(kind="bar", color=['skyblue','salmon','limegreen'])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# 3. Histogram: distribution of sepal length
plt.figure(figsize=(7,5))
plt.hist(df["sepal length (cm)"], bins=20, color="purple", alpha=0.7)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: sepal length vs petal length
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set1")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
