import os
import pandas as pd

file_path = 'parsed_impressions.xlsx'
df = pd.read_excel(file_path)

output_dir = 'normal'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

sessions = df[['UserId', 'DeviceCategory', 'Browser', 'OS', 'Country', 'City', 'BandWidth', 'MobileDevice', 'OSVersion', 'MobileCarrier', 'MobileAppId']].drop_duplicates()

ads = df[['ImpressionId', 'AdvertiserId', 'OrderId', 'LineItemId', 'CreativeId', 'CreativeVersion', 'CreativeSize', 'Product', 'CreativeSizeDelivered']].drop_duplicates()

ad_performance = df[['ImpressionId', 'EstimatedBackfillRevenue', 'IsCompanion', 'IsInterstitial', 'ActiveViewEligibleImpression']].drop_duplicates()

session_impressions = df[['UserId', 'ImpressionId', 'EventTimeUsec2']].drop_duplicates()

sessions.to_excel(os.path.join(output_dir, 'sessions.xlsx'), index=False)
ads.to_excel(os.path.join(output_dir, 'ads.xlsx'), index=False)
ad_performance.to_excel(os.path.join(output_dir, 'ad_performance.xlsx'), index=False)
session_impressions.to_excel(os.path.join(output_dir, 'session_impressions.xlsx'), index=False)

print(f"Нормалізовані таблиці збережено у папку '{output_dir}'")
