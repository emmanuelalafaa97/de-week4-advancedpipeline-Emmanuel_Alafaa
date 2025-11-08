import pandas as pd
import ast   #importing ast module to safely evaluate strings containing Python literals
from api_client import APIClient


class Enricher:
    def data_enricher():
             client = APIClient()
             Users_data = client.get_all_users()
             if Users_data:
                    users_df = pd.DataFrame(Users_data)
                    print("All Users dataframe successfully created")
                    print(users_df.head())
                    users_df.to_csv(r"omnicart_pipeline/data_exported/users_data.csv",index=False)
             else:
                     print(("Failed to fetch users data"))

             All_products_data = client.get_all_products()
             if All_products_data:
                     prod_df = pd.DataFrame(All_products_data)
                     print("Products dataframe successfully created")
                     print(prod_df.head())
                     #save the dataframe in a csv file
                     prod_df.to_csv(r"omnicart_pipeline/data_exported/products_data.csv", index=False)
             else:
                     print(("Failed to fetch Product data"))
    
     #or since we are not saving to csv then it is better to divide the users and products data into 2 separate functions

    def users_data_enricher():
             client = APIClient()
             Users_data = client.get_all_users()
             if Users_data:
                    users_df = pd.DataFrame(Users_data)
                    print("All Users dataframe successfully created")
                    print(users_df.head())
             else:
                     print(("Failed to fetch users data"))

    def prod_data_enricher():
             client = APIClient()
             All_products_data = client.get_all_products()
             if All_products_data:
                     prod_df = pd.DataFrame(All_products_data)
                     print("Products dataframe successfully created")
                     print(prod_df.head())  
             else:
                     print(("Failed to fetch Product data"))
           
    
    if __name__ == "__main__":
           data_enricher()   #call for it to run