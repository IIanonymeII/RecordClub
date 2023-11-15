import datetime
import pandas as pd
from tqdm import tqdm
from typing import List
import src.structure.nageur as nageur
import src.webscrapping.abcnatation as abcnatation
from src.webscrapping.ffn_ranking import find_ffn_info_for_one_swimmer, find_relai_swimmer_in_compet, find_time_by_swimmer
from src.structure.relai import NageRelai 

specialList = {"RIOU Yann ":("H","612256"),
               "EVEN Thomas ":("H","1567489"),
               "ALLAIN Cyril ":("H","1592945"),
               "DANIEL Thomas ":("H","1793845"),
               "BEAUMONT Camille ":("F","377922"),
               "SIMON Arthur ":("H","2230997")}

def list_all_swimmer():
    print("===============  abcnatation  ===============")
    today = datetime.date.today()
    year = int(today.year)
    result = []
    for date in tqdm(range(1996,int(year)+1),desc="Search by year"): #1996  
        result_transi = []
        # print('YEARS : {}-{}'.format(date,date+1))
        result_transi = abcnatation.list_swimmer_by_year("{}-{}".format(date,date+1))
        for i in result_transi:
            if i not in result:
                result.append(nageur.Nageur(name=i["name"],lastname=i["last_name"], url_abcnatation=i["url"]))
    
    print("There are {} unique swimmer in the dataset".format(len(result)))
    return result


def findAllSwimmer_FFN_id(list_all_nageur : List[nageur.Nageur]) -> List[nageur.Nageur] :
    result = []
    for nageur in tqdm(list_all_nageur,desc="find all swimmer in FFN Ranking"):
        url = "https://ffn.extranat.fr/webffn/_recherche.php?go=ind&idrch={}".format(nageur.get_full_name())
        # print(url)
        if specialList.get(nageur.get_full_name()):
            sex, id_ffn = specialList.get(nageur.get_full_name())
        else:
            try:
                sex,id_ffn = find_ffn_info_for_one_swimmer(url = url)
            except TypeError as exc:
                print(f"type Error with : {nageur}")
                print(f"full name : '{nageur.get_full_name()}'")
                raise exc
            except Exception as exc:
                print(f"Error with : {nageur}")
                raise exc
        nageur.set_id_ffn(id_ffn=id_ffn)
        nageur.set_sex(sex=sex)
    
    for nageur in list_all_nageur:
        if nageur.id_ffn == -1:
            print(f"error with {nageur}")
        # print(nageur.id_ffn)
    return list_all_nageur


def find_all_nage_by_swimmer(list_all_nageur : List[nageur.Nageur]):
    
    for nageur in tqdm(list_all_nageur, desc="Find all swim by swimmer"):
        # print(nageur)
        if nageur.get_id_ffn() == -1:
            print(f"Error with : {nageur}")
        else:
            for nage in find_time_by_swimmer(id_ffn=nageur.get_id_ffn()):
                nageur.add_nage(nage)
    return list_all_nageur
       

def all_relai_url(df: pd.DataFrame) -> List[str]:
    list_url = []
    # print(df.head())
    for url in df[df["Link_Relai"].notnull()]["Link_Relai"]:
        # print(url)
        list_url.append(url)
    return list_url


def relai_info(list_url : List[str]) -> List[NageRelai]:
    relai_result = []
    for url in tqdm(list_url):
        # print(url)
        relai_result.extend(find_relai_swimmer_in_compet(url=url))
    return relai_result

    

    