# -*- coding: utf-8 -*-

import requests
import pandas as pd
import io
from datetime import datetime as dt

def main():
    response = requests.get('https://testiws.ximad.com/export/events.csv.gz')
    df = pd.read_csv(io.BytesIO(response.content),sep=",", compression="gzip", index_col='event_time')
    df.index = pd.to_datetime(df.index)
    temp = pd.merge(
    left=df.query('event_name=="purchase"').resample('D').sum(),
    right=df.query('event_name=="launch"').loc[:,'user_id'].resample('D').count(),
    left_index=True, right_index=True)\
    .rename(
        columns = {
            'event_value':'sum_per_day',
            'user_id':'count_active_user'
            }
        )
    ARPDAU = pd.DataFrame(temp.sum_per_day / temp.count_active_user,
                          columns=['arpdau'])
    print(ARPDAU)


if __name__=='__main__':
    main()