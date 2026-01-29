import datetime
import sys
import pandas as pd
import great_expectations as gx
import great_expectations.expectations as ge

def gx_create():
    context = gx.get_context()
    data_source = context.data_sources.add_pandas('Books Data Source')
    data_asset = data_source.add_dataframe_asset('Books Asset')

    suite = gx.ExpectationSuite(name='Book Expectations')
    suite.add_expectation(ge.ExpectColumnValuesToBeBetween(
        column="Pages", min_value=146, max_value=545)
    )
    suite.add_expectation(ge.ExpectColumnValuesToBeBetween(
            column='PublishDate', min_value=datetime.datetime(1861,7,1),
            max_value=datetime.datetime(1998,1,1))
    )
    for c, t in (('Title', 'str'), ('Author', 'str'),
                 ('PublishDate', 'datetime64'), ('Pages', 'int64'),
                 ('Own', 'bool_')):
        suite.add_expectation(ge.ExpectColumnValuesToNotBeNull(column=c))
        suite.add_expectation(ge.ExpectColumnValuesToBeOfType(
            column=c, type_=t)
        )
        if c in ('Title', 'Author'):
            suite.add_expectation(ge.ExpectColumnValuesToBeUnique(column=c))
    suite.add_expectation(ge.ExpectColumnValuesToMatchRegex(
        column='Title', regex='^.{4,20}$'))
    suite.add_expectation(ge.ExpectColumnValuesToMatchRegex(
        column='Author', regex='^.{14,19}$'))

    suite = context.suites.add(suite)
    return data_asset, suite

def gx_validate(batch_name, data_asset, suite):
    batch_definition = data_asset.add_batch_definition_whole_dataframe(
        batch_name
    )
    df = pd.read_parquet(batch_name, dtype_backend='numpy_nullable')
    batch = batch_definition.get_batch(batch_parameters={'dataframe': df})

    return batch.validate(suite)

if __name__ == '__main__':
    data_asset, suite = gx_create()
    if len(sys.argv) == 2:
        result = gx_validate(sys.argv[1], data_asset, suite)
        if result.success:
            print('OK')
        else:
            print(f'Failed!  Statistics:\n{result.statistics}')
            print(f'Details:', result)

