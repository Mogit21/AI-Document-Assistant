import pandas as pd
from io import StringIO

def process_csv(file):
    content = file.file.read().decode("utf-8")
    df = pd.read_csv(StringIO(content))
    return df.to_dict(orient="records")
