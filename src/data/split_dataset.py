def split_train_val(df, target, test_size=0.2, random_state=2023):
    """
    This function separates the target column from the dataframe, splits the dataframe into train and validation sets, 
    and then recombines them. The train and validation dataframes include both features and target.

    Parameters:
    - df: A pandas DataFrame that contains the dataset.
    - target: A string that represents the target column name in df.
    - test_size: A float representing the proportion of the dataset to include in the test split.
    - random_state: An integer which is the seed used by the random number generator.

    Returns:
    - train: The train dataframe which includes both features and target.
    - val: The validation dataframe which includes both features and target.
    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    X = df.drop(columns=target)
    y = df[target]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)

    train = pd.concat([X_train, y_train], axis=1)
    val = pd.concat([X_val, y_val], axis=1)

    return train, val
