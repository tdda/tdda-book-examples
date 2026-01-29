import sys
import pandas as pd
import great_expectations as gx

def gx_create():
    context = gx.get_context()
    data_source = context.data_sources.add_pandas('Books Data Source')
    data_asset = data_source.add_dataframe_asset('Books Asset')

    suite = gx.ExpectationSuite(name='Book Expecations')
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
        column="Pages", min_value=146, max_value=545)
    )
    for c in ('Title', 'Author' ,'PublishDate' ,'Pages', 'Own'):
        suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(
            column=c)
        )

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
        r = gx_validate(sys.argv[1], data_asset, suite)
        if r.success:
            print('OK')
        else:
            print(f'Failed!  Statistics:\n{r.statistics}')
            print(f'First Constraint Results:\n{r.results[0]}')
