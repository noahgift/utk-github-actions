import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/noahgift/socialpowernba/master/data/nba_2017_br.csv")
print(df.head())

def toyou(x):
    return f"hi {x}"


def add(x):
    return x + 1


def subtract(x):
    return x - 1