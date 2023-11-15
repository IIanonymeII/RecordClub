from src.function.conversion import save_to_csv, to_dataframe
from src.function.swimmer import find_all_nage_by_swimmer, findAllSwimmer_FFN_id, list_all_swimmer



specialList = [
                   ["RIOU Yann ","612256"],
                   ["EVEN Thomas ","1567489"],
                   ["ALLAIN Cyril ","1592945"],
                   ["DANIEL Thomas","1793845"],

                  ]


if __name__ == "__main__":
    list_nageur = findAllSwimmer_FFN_id(list_all_nageur = list_all_swimmer())
    list_nageur = find_all_nage_by_swimmer(list_all_nageur=list_nageur)
    df = to_dataframe(list_nageur)
    save_to_csv(dataframe=df,file_path="final.csv")

    
