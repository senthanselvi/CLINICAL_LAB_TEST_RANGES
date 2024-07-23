import pandas as pd
from db_manager import *

def csv_to_df(csv_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Display the DataFrame
    return df

df = csv_to_df('blood_count_dataset.csv')

df1 = df['Gender'] == 'Male'
df1 = df[df1]

df2 = df['Gender'] == 'Female'
df2 = df[df2]

store_dataframe_to_firestore(df1,'DataLLRR_Lab1')
store_dataframe_to_firestore(df2,'DataLLRR_Lab2')