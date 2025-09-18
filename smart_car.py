import time
import pandas as pd
from sqlalchemy import create_engine

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTHocZE_g_tNtsvHxTL30x1fShYFQnAvy6WKTXQxbXgsOzd47E9iH7Hzw9gg0ZhiiiiOjscXmHMAemK/pub?output=csv"
engine = create_engine("mysql+pymysql://root:Root2025!@localhost:3306/mydb")
while True:
    df = pd.read_csv(sheet_url)
    df.to_sql('smart_car_live', engine, if_exists='replace', index=False)
    print("✅ Synced at", pd.Timestamp.now())
    time.sleep(900)  # 900 seconds = 15 mins


