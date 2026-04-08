from pandas import Timestamp
from pandera.pandas import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
    columns={
        "Title": Column(
            dtype="string[python]",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Author": Column(
            dtype="string[python]",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "PublishDate": Column(
            dtype="datetime64[ns]",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=Timestamp("1861-07-01 00:00:00"),
                    raise_warning=False,
                    ignore_na=True,
                ),
                Check.less_than_or_equal_to(
                    max_value=Timestamp("1998-01-01 00:00:00"),
                    raise_warning=False,
                    ignore_na=True,
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Pages": Column(
            dtype="Int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=146.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=545.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Own": Column(
            dtype="boolean",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(
                min_value=0.0, raise_warning=False, ignore_na=True
            ),
            Check.less_than_or_equal_to(
                max_value=4.0, raise_warning=False, ignore_na=True
            ),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=False,
    title=None,
    description=None,
)
