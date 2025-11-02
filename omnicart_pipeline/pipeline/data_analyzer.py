import pandas as pd
import numpy as np
import math

data = pd.read_csv(r"week4\data_and_other_info\data_exported\transformed_data.csv")

print("DataFrame Info:")
print(data.info())

print("-------------------------------")

print("Number of rows and columns in data:", data.shape)
print("-------------------------------")
#def rename_columns(df):
     #df = data
     #df.rename(columns= {'ratings_rate' : "ratings_value", 'ratings_count' : "Count_quantity"}, inplace=True)
     #print(df.columns)

#rename_columns()

def average_price():
    avg_price = data['price'].sum()/ data['title'].nunique()
    print(f"average price across all products is: {avg_price: .2f}")    #using print 
    #return avg_price

average_price()


# Average revenue by city
def city_revenue():
     revenue_by_city = data.groupby('address_city')['revenue'].sum()
     
     revenue_by_city.sort_values(ascending=False)
     print("Each city revenue figures:", revenue_by_city.sort_values(ascending=False))

city_revenue()


# Top rated products
def top_ratings():
     top_rated = data[['title', 'rating_rate']].sort_values(by='rating_rate', ascending=False)
     
     print("Top rated Products:", top_rated)


top_ratings()

def all_analysis(data : pd.DataFrame) -> dict :
       # Group by username and compute the three required metrics
    grouped = data.groupby('username').agg(
        total_revenue=('revenue', 'sum'),
        product_count=('title', 'nunique'),
        avg_price=('price', 'mean')
    ).reset_index()
    
    # Convert to nested dict structure
    result = (
        grouped.set_index('username')
        .to_dict(orient='index')
    )
    return result

print("Summary:", all_analysis(data))