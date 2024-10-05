import pandas as pd
import csv

file_path = 'NetworkBackfillImpressions_1748938_20201216_02'

with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = [row for row in reader]

df = pd.DataFrame(data, columns=headers)

df.replace('', pd.NA, inplace=True)

output_file = 'parsed_impressions.xlsx'
df.to_excel(output_file, index=False)

print(f"Дані успішно збережено у файл {output_file}")
