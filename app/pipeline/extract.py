import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para extrair DataFrames de arquivos Excel em uma pasta.

    args:
        path (str): Caminho para a pasta com os arquivos Excel

    return:
        data_frame_list (List[pd.DataFrame]): Lista com os DataFrames extra dos
        arquivos Excel
    """
    # Localiza todos os arquivos Excel na pasta
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    # Inicializa uma lista para armazenar os DataFrames
    data_frame_list = []
    # Itera sobre os arquivos e extrai os DataFrames
    for file in all_files:
        # Adiciona o DataFrame  lista
        data_frame_list.append(pd.read_excel(file))

    # Retorna a lista de DataFrames
    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path="data/input")
    print(data_frame_list)
    print("Hello World")
