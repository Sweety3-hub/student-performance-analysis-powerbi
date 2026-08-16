import pandas as pd

# Load dataset
df = pd.read_csv("Student_Performance.csv")

# Show original data
print("Original Data:")
print(df.head())

# 🟢 Data Cleaning

# Remove missing values
df = df.dropna()

# Convert important columns to numeric
df['study_hours_per_day'] = pd.to_numeric(df['study_hours_per_day'], errors='coerce')
df['sleep_hours'] = pd.to_numeric(df['sleep_hours'], errors='coerce')
df['phone_usage_hours'] = pd.to_numeric(df['phone_usage_hours'], errors='coerce')
df['social_media_hours'] = pd.to_numeric(df['social_media_hours'], errors='coerce')
df['final_grade'] = pd.to_numeric(df['final_grade'], errors='coerce')

# Drop rows with invalid values
df = df.dropna()

# Show cleaned data
print("Cleaned Data:")
print(df.head())
# Summary statistics
print("\nSummary:")
print(df.describe())

# Correlation
print("\nCorrelation:")
print(df.corr(numeric_only=True))
import seaborn as sns
import matplotlib.pyplot as plt

# Study hours vs Final Grade
sns.regplot(x='study_hours_per_day', y='final_grade', data=df, scatter_kws={'alpha':0.3})
plt.title("Study Hours vs Final Grade (Trend)")
plt.show()

# Phone usage vs Final Grade
# Phone usage vs grade
sns.regplot(x='phone_usage_hours', y='final_grade', data=df, scatter_kws={'alpha':0.3})
plt.title("Phone Usage vs Final Grade")
plt.show()

# Sleep vs grade
sns.regplot(x='sleep_hours', y='final_grade', data=df, scatter_kws={'alpha':0.3})
plt.title("Sleep vs Final Grade")
plt.show()

# Focus vs productivity
sns.regplot(x='focus_score', y='productivity_score', data=df, scatter_kws={'alpha':0.3})
plt.title("Focus vs Productivity")
plt.show()
# Grouping study hours
df['study_group'] = df['study_hours_per_day'].round()

print("\nAverage Grade by Study Hours:")
print(df.groupby('study_group')['final_grade'].mean())

# Grouping phone usage
df['phone_group'] = df['phone_usage_hours'].round()

print("\nAverage Grade by Phone Usage:")
print(df.groupby('phone_group')['final_grade'].mean())