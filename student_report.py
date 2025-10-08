import pandas as pd
import numpy as np

# Load data 
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Evelyn'],
    'Maths': [78, 85, 96, 80, 90],
    'Science': [88, 75, 85, 90, 92],
    'English': [82, 79, 91, 73, 88]
}

# Create DataFrame
df = pd.DataFrame(data)
print("----- STUDENT MARKS DATA -----")
print(df)

# Calculate total and average
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)

# Rank students based on total marks
df['Rank'] = df['Total'].rank(ascending=False, method='dense').astype(int)

# Display results
print("\n----- PERFORMANCE REPORT -----")
print(df.sort_values(by='Rank'))

# Subject-wise average
print("\n----- SUBJECT-WISE AVERAGE -----")
print(df[['Maths', 'Science', 'English']].mean())

# Export to CSV
df.to_csv('student_report.csv', index=False)
print("\nReport exported successfully as 'student_report.csv'")
