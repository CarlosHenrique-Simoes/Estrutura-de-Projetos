import os  # biblioteca para manipular arquivos e pastas

import pandas as pd  # biblioteca para trabalhar com dataframes


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str):
    """
    Receber um data frame e salvar em um arquivo excel

    args:
        data_frame: (pd.DataFrame): dataframe a ser salvo como excel
        output_path: (str): caminho onde o arquivo sera salvo
        file_name: (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"
    """
    # Verificar se o diret rio de saida existe, caso n o, criar
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Salvar o data frame em um arquivo excel
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
