import pandas as pd

# Read the Excel file
excel_file = 'AI.xlsx'
df = pd.read_excel(excel_file)

# Convert the Excel data to CSV format
csv_file = 'AI.csv'
df.to_csv(csv_file, index=False)

print(f"Excel file '{excel_file}' has been converted to CSV file '{csv_file}'.")
