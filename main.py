import pandas as pd

df = pd.read_csv('task_dataset_summer_products.csv')

df = df.groupby(['origin_country']).agg(average_price=('price', 'mean'),
                                        sum_rating_five_count=('rating_five_count', 'sum'),
                                        sum_rating_count=('rating_count', 'sum')).reset_index()



df['five_percentage'] =df ['sum_rating_five_count']/df ['sum_rating_count'] *100

df.drop(['sum_rating_five_count','sum_rating_count'], axis=1)

df[['origin_country','average_price','five_percentage']].to_csv('result.csv')