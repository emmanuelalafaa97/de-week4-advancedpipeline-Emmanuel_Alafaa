import pandas as pd
import numpy as np
import math
from data_enricher import Enricher

#data = pd.read_csv(r"week4\data_and_other_info\data_exported\transformed_data.csv")


class Analyzer():
    
    def average_price(df):
            avg_price = df['price'].sum()/ df['title'].nunique()
            print(f"average price across all products is: {avg_price: .2f}")    #using print 
            #return avg_price

    #average_price()


    # Average revenue by city
    def city_revenue(df):
         revenue_by_city = df.groupby('address_city')['revenue'].sum()
     
         revenue_by_city.sort_values(ascending=False)
         print("Each city revenue figures:", revenue_by_city.sort_values(ascending=False))

    #city_revenue()


    # Top rated products
    def top_ratings(df):
          top_rated = df[['title', 'rating_rate']].sort_values(by='rating_rate', ascending=False)
     
          print("Top rated Products:", top_rated)


    #top_ratings()
    # save final report
    #analyzed_df.to_json(r"omnicart_pipeline/data_exported/sellers_performance_report", index=False)

    def all_analysis(df : pd.DataFrame) -> dict :
        # Group by username and compute the three required metrics
        grouped = df.groupby('username').agg(
             total_revenue=('revenue', 'sum'),
             product_count=('title', 'nunique'),
             avg_price=('price', 'mean')
            ).reset_index()
    
        # Convert to nested dict structure
        result = (
          grouped.set_index('username').to_dict(orient='index')
         )
        return result
    


    if __name__ == "__main__":
         
     data = pd.read_csv(r"omnicart_pipeline/data_exported/transformed_data.csv")
     #if we exported or saved the data to a file then we can retrieve the data and pass it into the "all_analysis()" function
     # otherwise we just pass or call the "Enricher.data_enricher" inside the "all_analysis()" function
     #data = Enricher.data_enricher()
     print("Summary:", all_analysis(data))