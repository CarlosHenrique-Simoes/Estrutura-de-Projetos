from pathlib import (  # noqa: D100
    Path,
)  # Biblioteca para trabalhar com caminhos de arquivos

import pandas as pd  # biblioteca para trabalhar com dataframes


def load_excel(data_frame: pd.DataFrame, output: str, file_name: str) -> str:
    """Receber um data frame e salvar em um arquivo excel.

    Args:
        data_frame: (pd.DataFrame): dataframe a ser salvo como excel
        output: (str): caminho onde o arquivo sera salvo
        file_name: (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"

    """
    # Verificar se o diretório de saida existe, caso não, criar
    if not Path(output).exists():
        Path(output).mkdir(parents=True)

    # Salvar o data frame em um arquivo excel
    data_frame.to_excel(f"{output}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
