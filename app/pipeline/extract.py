from pathlib import Path  # noqa: D100
from typing import List  # noqa: UP035

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:  # noqa: UP006
    """Função para extrair DataFrames de arquivos Excel em uma pasta.

    Args:
        path (str): Caminho para a pasta com os arquivos Excel

    Return:
        data_frame_list (List[pd.DataFrame]): Lista com os DataFrames extra dos
        arquivos Excel

    """
    # Busca todos os arquivos Excel no caminho especificado
    all_files = list(Path(path).glob("*.xlsx"))

    # retorna uma lista de DataFrames
    return [pd.read_excel(file) for file in all_files]


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path="data/input")
    print(data_frame_list)  # noqa: T201
    print("Hello World")  # noqa: T201
