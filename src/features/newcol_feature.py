def create_per_game_features(df, per_game_columns, game_column='GP'):
    """
    Creates new columns for average per game of the specified columns.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        per_game_columns (list of str): The names of the columns to calculate average per game.
        game_column (str): The name of the column representing the number of games.

    Returns:
        pd.DataFrame: The modified DataFrame. This is the same object as the input, not a copy.
    """
    print('Create new feature ')
    for col in per_game_columns:
        new_col = col + '_PG'
        print('\t', new_col)
        df[new_col] = df[col] / df[game_column]
    return df



def replace_infinite_with_nan(df):
    """
    Replaces infinite values in the DataFrame with NaN.

    Args:
        df (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame. This is the same object as the input, not a copy.
    """
    import numpy as np
    df.replace([np.inf, -np.inf], np.NaN, inplace=True)
    return df
