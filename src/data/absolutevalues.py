def replace_negative_with_abs(df, columns):
    """
    Replaces negative values with their absolute values in the specified columns of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        columns (list of str): The names of the columns in which to replace negative values.

    Returns:
        pd.DataFrame: The modified DataFrame. This is the same object as the input, not a copy.
    """
    for col in columns:
        print('Replace negative values in', col, 'with absolute values')
        df[col] = df[col].abs()
    return df
