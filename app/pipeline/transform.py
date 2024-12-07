from typing import List  # noqa: UP035, D100

import pandas as pd


def concat_data_frames(
                        data_frame_list: List[pd.DataFrame],  # noqa: UP006
                    ) -> pd.DataFrame:
    """Função para concatenar uma lista de DataFrames em um nico DataFrame.

    A função o utiliza o m todo pd.concat com o par metro ignore_index
    definido como True, para que os ndices dos DataFrames sejam renumerados.

    Args:
        data_frame_list (List[pd.DataFrame]): Lista de DataFrames a serem
        concatenados

    Returns:
        pd.DataFrame: DataFrame concatenado

    """
    return pd.concat(data_frame_list, ignore_index=True)
