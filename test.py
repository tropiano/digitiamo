from src.clean_data import filter_category, filter_null
import numpy as np 
import pandas as pd

filter_null_input_data = "test/data/filter_null_input.csv"
filter_null_output_data = "test/data/filter_null_output.csv"

filter_ctg_input_data = "test/data/filter_ctg_input.csv"
filter_ctg_output_data = "test/data/filter_ctg_output.csv"

def test_filter_null():
    with open(filter_null_input_data, "r") as f:
        df_clean = filter_null(f, column="Cause Subcategory")
    
    with open(filter_null_output_data, "r") as f:
        df_output = pd.read_csv(f).to_csv(index=False)
    
    assert(df_clean==df_output)

def test_filter_ctg():
    with open(filter_ctg_input_data, "r") as f:
        df_clean = filter_category(f)
    
    with open(filter_ctg_output_data, "r") as f:
        df_output = pd.read_csv(f).to_csv(index=False)
    
    assert(df_clean==df_output)

