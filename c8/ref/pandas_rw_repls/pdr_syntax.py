df = pd.read_csv(path, sep=',', na_values='', header=0,
                 keep_default_na=False, encoding='utf-8',
                 date_format={'open_date': 'ISO8601',
                              'close_date': 'ISO8601'},
                 parse_dates=['open_date', 'close_date'],
                 quotechar='"', escapechar=None)
