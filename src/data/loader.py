import pandas as pd

class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    YEAR ="year"
    MONTH = "month"

def load_transaction_data(path:str) -> pd.DataFrame:
    #load data from a csv file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT:float,
            DataSchema.CATEGORY:str
        },
        parse_dates=[DataSchema.DATE]
    )
    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.month.astype(str)
    return data