import pandas as pd

def read_dataset(url):
    try:
        df = pd.read_csv(url)
        return df
    except:
        return None

