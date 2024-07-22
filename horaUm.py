import pandas as pd

url = "dataset/aluguel.csv"
dados = pd.read_csv(url, sep=";")
dados
