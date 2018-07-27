import pandas as pd
filename = "bills.csv"
df = pd.read_csv(filename)
df.drop(["article_batch","selling_price","tax","discount","cost_price","quantity"],axis=1,inplace=True)
df.dropna(inplace=True,axis=1)
x=df.groupby(['bill_no'])['article_id'].apply(list)
df1 = pd.DataFrame(x)
#Creating Intermediate Table which may help in future to find other parameters from data
tablename = "intermediate_table.csv"
df1.to_csv(tablename)
