import datetime
import numpy as np
import pandas as pd

def enhance_accounts(df):
    """
    Add new columns to an accounts DataFrame for enhanced constraint discovery.
    """
    now = pd_now()
    df['no_tel'] = df['home_tel'].isnull() & df['mobile_tel'].isnull()
    df['close_before_open'] = (
        df['close_date'].notnull() & (df['close_date'] <= df['open_date'])
    )
    df['open_secs_in_future'] = seconds_after_time(df['open_date'], now)
    df['close_secs_in_future'] = seconds_after_time(df['close_date'], now)

def pd_now():
    """Get current time as numpy datetime (in microseconds)"""
    return np.datetime64(datetime.datetime.now()).astype('<M8[us]')

def seconds_after_time(col, ref_time):
    """
    Compute time in after ref_time of a Pandas Timestamp column, in seconds.
    Return null where the column value is null.
    """
    return np.where(col.notnull(), (col - ref_time).dt.total_seconds(), np.nan)
