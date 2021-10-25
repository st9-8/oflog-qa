from settings import DATA_FOLDER, DATE_RANGE, DATE

import sys
import logging
import pandas as pd


def sort_data(df, save=False):
    """
        Utility function used to sort dataset by date

        params
            - save: False by default, used to save or not the data on disk
    """

    df['datetime'] = pd.to_datetime(df['datetime'], format='%Y %B %d %H:%M')
    df = df.sort_values(by=DATE)

    if save:
        df.to_csv(DATA_FOLDER / 'data_logs_sorted.csv',
                  date_format='%Y %B %d %H:%M', index=False)

    return df


def discretize_data(df):
    """
        Function used to discretize our data in range of DATE_RANGE in settings.py
    """

    # Get time frames
    start_date, end_date = extract_start_end_date(df)
    time_frames = pd.date_range(start=start_date, end=end_date, freq=DATE_RANGE)

    df_date_index = df.set_index(DATE)

    frames = {}
    count = 1
    for i in range(len(time_frames)-1):
        frames[count] = df_date_index[time_frames[i]:time_frames[i+1]]
        count += 1

    return frames


def extract_start_end_date(df):
    """
        Utility function used to get start date and end date of logs data
    """
    start_date, end_data = df.loc[df.index[0],
                                  DATE], df.loc[df.index[-1], DATE]

    return start_date, end_data


def train_test_split(df, test_size=0.3):
    """
        Utility function used to split dataset in train and test data set

        params
            - test_size: Proportion of test dataset
    """

    if test_size >= 1:
        logging.error('Please provide a correct test_size proportion')
        sys.exit(1)

    train_size = int(df.shape[0] * (1 - test_size))
    train = df[:train_size]
    test = df[train_size+1:]

    return train, test


def extract_action(action):
    """
        Utility function used to extract the exact action
    """

    data = action.split('(')
    action = '-'.join(data[0].strip().split())
    uri = data[1].replace(')', '').strip()

    return uri


if __name__ == '__main__':
    discretize_data()
