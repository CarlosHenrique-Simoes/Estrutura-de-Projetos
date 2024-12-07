import pandas as pd  # noqa: D100

from app.pipeline.transform import concat_data_frames

df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df2 = pd.DataFrame({"a": [7, 8, 9], "b": [10, 11, 12]})


def testar_a_concatenacao_da_lista_de_dataframes() -> None:
    """Testa a função concat_data_frames para verificar se ela concatena
    corretamente uma lista de DataFrames.

    Cria dois DataFrames simples e os concatena usando a função
    concat_data_frames.

    Compara o resultado com a concatenação direta usando pd.concat
    para assegurar que o resultado é o esperado.
    """  # noqa: D205
    # Lista de dataframes a serem concatenados
    data_frame_list = [df1, df2]

    # Concatenação direta usando pd.concat
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # Concatenação usando a função concat_data_frames
    df_check = concat_data_frames(data_frame_list)

    # Verifica se o DataFrame resultante tem a forma esperada
    assert df_check.shape == (6, 2)  # noqa: S101

    # Verifica se o DataFrame resultante é igual ao da concatenação direta
    assert data_frame.equals(df_check)  # noqa: S101

    # Verifica se o DataFrame resultante da concatenação direta
    # tem a forma esperada
    assert data_frame.shape == (6, 2)  # noqa: S101
