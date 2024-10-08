import os
import glob
import pandas as pd

# Get the list of CSV files in the current directory
csv_files = glob.glob('*.csv')  # Adjust the path if necessary

if not csv_files:
    print("No CSV files found.")
    exit()

# Sort files by modification time and get the latest one
latest_file = max(csv_files, key=os.path.getmtime)

print(f"Processing file: {latest_file}")

# Read the latest CSV file
df = pd.read_csv(latest_file)

# Data Cleaning Logic
# 1. Handle Null Values
# Option 1: Drop rows with null values
df_cleaned = df.dropna()

# Option 2: Fill null values with a specific value (e.g., 0)
# df_cleaned = df.fillna(0)

# 2. Handle Duplicate Values
# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Additional cleaning logic can be added here...

# Save cleaned data to a new file
cleaned_file = f"cleaned_{latest_file}"
df_cleaned.to_csv(cleaned_file, index=False)
print(f"Cleaned data saved to: {cleaned_file}")
