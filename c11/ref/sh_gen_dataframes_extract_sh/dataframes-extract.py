def generate_dataframe(nrows=10, precision=3):
    """
    Generates a simple Pandas DataFrame with integer, real (float),
    boolean, and string columns.
    """
    df = pd.DataFrame({'i': range(nrows)})
    df['r'] = df.i * (10/9)
    df['random'] = np.random.randint(0, nrows-1, nrows)
    df['b'] = df.i >= nrows/2
    df['i_square'] = df.i * df.i
    df['r_square'] = df.r * df.r
    df['s'] = 'result ' + df.r_square.round(precision).astype(str)
    return df
