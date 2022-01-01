import pandas as pd


def preprocess(df, region_df):
    # filter summer olympic
    df = df[df['Season'] == 'Summer']
    # merge with noc_region
    df = df.merge(region_df, on='NOC', how='left')
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # concat
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
