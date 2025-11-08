import pandas as pd
import logging 
import json
import os
from pipeline.data_enricher import Enricher
from configparser import ConfigParser
from pipeline.api_client import APICLIENT
from pipeline.data_analyzer import Analyzer
from pipeline.data_cleaning import Cleaning
from pipeline.pipeline import Pipeline




if __name__ == "__main__":
    p = Pipeline()
    result = p.run()
    print("\nAnalysis result (head):")
    try:
        # If it's a DataFrame
        print(result.head())
    except Exception:
        print(result)