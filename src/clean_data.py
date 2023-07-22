import pandas as pd
import re
import sys

def filter_null(data, column):
    df = pd.read_csv(data)
    df_clean = df.dropna(subset=[column])
    return df_clean.to_csv(index=False)


def filter_category(data):
    df = pd.read_csv(data)
    
    df_filter = df[~(df["Cause category"]=="Traffic Control") | 
                   ((df["Cause category"]=="Traffic Control") & 
                    (df["Cause Subcategory"]=="Others") | 
                    (df["Cause Subcategory"]=="Police Controlled"))]
    
    df_filter.loc[:,"Million Plus Cities"] = df_filter["Million Plus Cities"].apply(
        lambda x: re.sub(r'\(.+?\)', '', x))
    return df_filter.to_csv(index=False)

if __name__ == '__main__':

    data = sys.argv[1]
    with open(data) as f:
        clean_csv = filter_null(f, column="Count")

    with open(data) as f:
        filter_category(f)
