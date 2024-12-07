from pipeline.extract import extract_from_excel  # noqa: INP001, D100
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(type(data_frame_list))  # noqa: T201
    data_frame = concat_data_frames(data_frame_list)
    print(type(data_frame))  # noqa: T201
    load_excel(data_frame, "data/output", "output_file")
