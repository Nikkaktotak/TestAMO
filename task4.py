import pandas as pd
import pprint

orders = pd.read_excel("Raw data, test (3).xlsx",sheet_name="Orders")
users = pd.read_excel("Raw data, test (3).xlsx",sheet_name="Users")
costs_by_source = pd.read_excel("Raw data, test (3).xlsx",sheet_name="Costs by source")
orders["date_date"]=pd.to_datetime(orders["date_order"],format="%Y/%m/%d").dt.date
costs_by_source["date"]=pd.to_datetime(costs_by_source["date"],format="%Y/%m/%d").dt.date
join = pd.merge(orders, users,left_on=['id_user'], right_on=['id'], how='left')
join1 = pd.merge(join,costs_by_source,right_on=['source','date'], left_on=['source','date_date'], how = "left")
output_path_in_root = './join_orders_users.xlsx'
pprint.pprint(costs_by_source)
pprint.pprint(orders)
pprint.pprint(join)
pprint.pprint(join1)
# Saving the joined table to an Excel file in the root
join1.to_excel(output_path_in_root, index=False)
