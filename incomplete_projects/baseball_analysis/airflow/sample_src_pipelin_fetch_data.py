# this could be a simple task function for the fetch_data/py 
# similar tasks need to be created for each step of the way

import pandas as pd

def load_local_data(file_path):
    """
    Function to load the data into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

