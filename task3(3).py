import pandas as pd

file_path = 'parsed_impressions.xlsx'
df = pd.read_excel(file_path)

df_clean = df.dropna(subset=['UserId'])

session_data = df_clean.groupby('UserId').agg(
    SessionRevenue=('EstimatedBackfillRevenue', 'sum'),
    Device=('DeviceCategory', 'first'),
    Product=('Product', 'first')
).reset_index()

output_file = 'session_revenue_report.xlsx'
session_data.to_excel(output_file, index=False)

print(f'Дані сесій збережено у файл: {output_file}')
