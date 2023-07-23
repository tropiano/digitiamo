import pandas as pd
import re
import sys

def filter_null(data, column):
    """
    Filter out the null values in the specified column 

    Args:
        data (file): a tabular csv file.
        column (str): the column to filter for null values.

    Returns:
        str: the cleaned csv file as a str.
    """
    df = pd.read_csv(data)
    df_clean = df.dropna(subset=[column])
    return df_clean.to_csv(index=False)


def filter_category(data):
    """
    Filter data accorsing to this rule
    1) if "Cause category" is equal to "Traffic Control" then "Cause Subcategory" 
    must be equal to "Others" or "Police Controlled". 
    2) Clean the "Million Plus Cities" column of the selected rows removing 
    all characters that appear between parentheses (includingthe parentheses).

    Args:
        data (file): a tabular csv file.

    Returns:
        str: the filtered csv file as a str.
    """
    
    df = pd.read_csv(data)
    
    df_filter = df[~(df["Cause category"]=="Traffic Control") | 
                   ((df["Cause category"]=="Traffic Control") & 
                    (df["Cause Subcategory"]=="Others") | 
                    (df["Cause Subcategory"]=="Police Controlled"))]
    
    df_filter.loc[:,"Million Plus Cities"] = df_filter["Million Plus Cities"].apply(
        lambda x: re.sub(r'\(.+?\)', '', x))
    return df_filter.to_csv(index=False)

if __name__ == '__main__':
    """
    Apply the filter_category and filter_null functions above
    Does not return any value 

    Args:

    Returns:
    """

    data = sys.argv[1]
    with open(data) as f:
        clean_csv = filter_null(f, column="Count")

    with open(data) as f:
        filter_csv = filter_category(f)

