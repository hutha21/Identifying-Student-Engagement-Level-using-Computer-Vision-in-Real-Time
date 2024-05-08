import pandas as pd

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def addUnit(result, key, unit):
   for index, item in enumerate(result):
      item[key] = item[key] + "%"