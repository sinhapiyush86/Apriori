import numpy as np
import pandas as pd
import itertools
pd.options.mode.chained_assignment = None
df_transaction = pd.read_csv("intermediate_table.csv")
# Best support vvalue was found to be 0.03
support = 0.03
df_article = pd.read_csv("articles.csv")
total_length=len(df_transaction['bill_no'])
df_article.drop_duplicates(subset='article_id',inplace=True)
df_bills = pd.read_csv("bills.csv")
c =df_bills['article_id'].value_counts().to_dict()
y = [c[i]/total_length for i in df_article['article_id']]
support_df = pd.DataFrame({"article_id":df_article['article_id'],"support":y})
final_support_df  = support_df[support_df['support'] > support]
a = [final_support_df['article_id'],final_support_df['article_id']]
df_2 = pd.DataFrame({"Item1":[i[0] for i in itertools.product(*a)],"Item2":[j[1] for j in itertools.product(*a)]})
df_2 = df_2[df_2['Item1']!=df_2['Item2']]
supp=[]
for i in df_2.itertuples():
	supp_var = sum(df_transaction.article_id.map(lambda x: str(i[1]) and str(i[2]) in x))/total_length
	supp.append(supp_var)
df_2['support'] = supp
final_support_df_2  = df_2[df_2['support'] > support]
final_support_df_2['conf'] = final_support_df_2.apply(lambda x: (x['support']/(c[x['Item1']]/total_length)), axis=1)
final_support_df_2 = final_support_df_2[final_support_df_2['conf']>0.5]
final_support_df_2['lift'] = final_support_df_2.apply(lambda x: (x['support']/((c[x['Item1']]/total_length)*(c[x['Item2']]/total_length))), axis=1)
xy={}
for i,j in zip(df_article['article_id'],df_article['name']):
    xy[i] = j
final_support_df_2['Item1'] = final_support_df_2['Item1'].map(xy)
final_support_df_2['Item2'] = final_support_df_2['Item2'].map(xy)
print(final_support_df_2.head(15))
print("Best Combinations of products has been stored in Final_Report.csv file")
final_support_df_2.to_csv("Final_Report.csv")



