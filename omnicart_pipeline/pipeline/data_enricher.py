import pandas as pd
import ast   #importing ast module to safely evaluate strings containing Python literals

users_data_df = pd.read_csv(r"omnicart_pipeline/pipeline/data_and_exported_files/users_data.csv")
products_data_df = pd.read_csv(r"omnicart_pipeline/pipeline/data_and_exported_files/products_data.csv")

print("Users DataFrame Info:", users_data_df.info())
print("-------------------------------")
print("Numbers of rows and columns in users data:", users_data_df.shape)
print("-------------------------------")
print("Users DataFrame columns:", users_data_df.columns)
print("-------------------------------")
print("Products DataFrame columns:", products_data_df.columns)

def left_merged() :
     try:
         left_merged_df = pd.merge(users_data_df, products_data_df, on='id', how='left')
         print("number of rows and columns in new dataframe:", left_merged_df.shape)
         #return left_merged_df.head()
     
     except ValueError:
          print("Failed to merge")
          return ValueError
     return left_merged_df.head()
     
#def handle_missing_mergers(file_one_df, file_two_df):
    #left_merged_df = pd.merge(file_one_df, file_two_df, on='id', how='left')
    #for col in left_merged_df.columns:
        #if left_merged_df[col].isnull().any():
            #print(f"Column '{col}' has missing values.")
    #if file_one_df.equals(file_two_df):
        #print("Both files have identical data.")
    #elif file_one_df.shape[0] > file_two_df.shape[0]:
        #print("File one has more rows than file two.")
    #elif file_one_df.shape[0] < file_two_df.shape[0]:
        #print("File two has more rows than file one.")
    #elif file_one_df.shape[0] == file_two_df.shape[0]:
        #print("Both files have the same number of rows but different data.")
    #elif file_one_df.shape[1] != file_two_df.shape[1]:
        #print("Files have different number of columns.")
    #return left_merged_df
#left_merged()

# this function cleans the data by expanding dictionary-like columns, it can be a stand file or program module to clean any json or csv data
def clean_data(df):
    """
    Automatically expands columns in a DataFrame that contain dictionary-like strings.

    For example:
    {'rate': 4.1, 'count': 259}
    becomes two columns: columnname_rate and columnname_count
    """
    for col in df.columns:
        # Check if column values look like dictionaries
        if df[col].apply(lambda x: isinstance(x, (dict, str))).all():
            try:
                # Convert string dicts to actual dicts if needed
                df[col] = df[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
                
                # Check if the column contains dicts after conversion
                if df[col].apply(lambda x: isinstance(x, dict)).any():
                    expanded = df[col].apply(pd.Series)
                    expanded.columns = [f"{col}_{subcol}" for subcol in expanded.columns]
                    print(f"splitting column: {col} into {list(expanded.columns)}")
                    
                    # Join back to the main DataFrame
                    df = df.join(expanded)
                    df = df.drop(columns=[col])
            except Exception:
                continue  # skip if not safely evaluable
    return df
 
# to use get your data either in a csv or json format and 
df = pd.DataFrame(left_merged())  # frist convert it to a dataframe
cleaned_df = clean_data(df)      #Then use the clean_data function
cleaned_df.head()              #print out the first 5 rows to see the result

#save the dataframe to a csv file and check it out
#cleaned_df.to_csv(r"omnicart_pipeline/pipeline/data_and_exported_files/cleaned_data.csv", index=False)

#Second_cleaned_df = clean_data(cleaned_df)  # you can run the clean_data function again if needed
#Second_cleaned_df.head()

#function to create a new column 'revenue' by multiplying 'price' and 'rating_count'
def handle_null_revenue(df):
    if 'price' in df.columns and 'rating_count' in df.columns:
        df['revenue'] = df['price'] * df['rating_count']     #creates a new column 'revenue' by multiplying 'price' and 'rating_count'
    else:
        raise KeyError("Required columns for revenue calculation are missing.")
    return df

transformed_data = handle_null_revenue(cleaned_df) #calling the function to create 'revenue' column
transformed_data.to_csv(r"omnicart_pipeline/pipeline/data_and_exported_files/transformed_data.csv", index=False) #saving the transformed data to a csv file    
