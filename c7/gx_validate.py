import pandas as pd
import great_expectations as gx


def gx_validate(batch_name, path):
    context = gx.get_context()
    data_source = context.data_sources.add_pandas(name='Books Data Source')
    data_asset = data_source.add_dataframe_asset('Books Asset')
    batch_definition = data_asset.add_batch_definition_whole_dataframe(
        batch_name
    )

    df = pd.read_parquet(path, dtype_backend='numpy_nullable')
    batch = batch_definition.get_batch(batch_parameters={'dataframe': df})

    suite = gx.ExpectationSuite(name='Book Expectations')
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
        column="Pages", min_value=146, max_value=545)
    )
    for c in list(df):
        suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(
            column=c)
        )

    suite = context.suites.add(suite)

    # Test the Expectation
    validation_results = batch.validate(suite)
    print(validation_results)


if __name__ == '__main__':
    gx_validate('books', 'books.parquet'),
    gx_validate('bad-books', 'bad-books.parquet')
