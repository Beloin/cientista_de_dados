import pandas as pd
from datetime import datetime


def converter(path: str):
    '''
    Converte para date.
    '''
    date_parser = lambda dates: datetime.strptime(dates, '%Y-%m')
    base = pd.read_csv(path, date_parser=date_parser,
                       parse_dates=['Month'], index_col='Month')
    return base
