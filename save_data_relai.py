


from src.function.swimmer import all_relai_url, relai_info
from src.function.conversion import read_csv_to_dataframe, save_to_csv, to_dataframe_relai


if __name__ == "__main__":
    df = read_csv_to_dataframe(file_path="final.csv")
    list_relai = relai_info(all_relai_url(df))
    df_final = to_dataframe_relai(list_relai)
    save_to_csv(dataframe=df_final,file_path="final_relai.csv")
