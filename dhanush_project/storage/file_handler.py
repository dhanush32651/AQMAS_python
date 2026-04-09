import csv
import pandas as pd

FILE_NAME = "air_quality.csv"

def save(record):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(record)

def load():
    try:
        return pd.read_csv(FILE_NAME)
    except:
        return None