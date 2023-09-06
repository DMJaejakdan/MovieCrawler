from os.path import abspath, dirname, join
from pathlib import Path

import pandas as pd

ROOT_PATH = Path(abspath(dirname(__file__))).parent
DATA_PATH = join(ROOT_PATH, 'data')


def load_raw_data(date: str) -> pd.DataFrame:
    data_path = join(DATA_PATH, 'raw', f'movie_list_{date}.csv')
    data_df = pd.read_csv(data_path, encoding='CP949')
    return data_df


def copy_and_load_data(date: str) -> pd.DataFrame:
    data_df = load_raw_data(date)
    copy_df = data_df.copy()
    copy_path = assemble_path(f'movie_list_{date}.csv', 'processed')
    save_df(copy_df, copy_path)
    return copy_df


def save_df(data_df: pd.DataFrame, path: str) -> None:
    data_df.to_csv(path, encoding="utf-8-sig", index=False)
    print(f'Saved dataframe file to {path}')


def assemble_path(name: str, *dirs) -> str:
    path = DATA_PATH
    for dir in dirs:
        path = join(path, dir)
    return join(path, name)
