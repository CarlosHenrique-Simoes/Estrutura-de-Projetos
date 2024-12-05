import pandas as pd

from app.pipeline.transform import concat_data_frames

df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df2 = pd.DataFrame({"a": [7, 8, 9], "b": [10, 11, 12]})


def testar_a_concatenacao_da_lista_de_dataframes():

    data_frame_list = [df1, df2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    df = concat_data_frames(data_frame_list)

    assert df.shape == (6, 2)
    assert data_frame.equals(df)
    assert data_frame.shape == (6, 2)
