import datetime
from tqdm import tqdm
from typing import List
import src.structure.nageur as nageur
import src.webscrapping.abcnatation as abcnatation
from src.webscrapping.ffn_ranking import find_ffn_info_for_one_swimmer, find_time_by_swimmer 

def list_all_swimmer():
    print("===============  abcnatation  ===============")
    today = datetime.date.today()
    year = int(today.year)
    result = []
    for date in range(2022,int(year)+1): #1996  
        result_transi = []
        print('YEARS : {}-{}'.format(date,date+1))
        result_transi = abcnatation.list_swimmer_by_year("{}-{}".format(date,date+1))
        for i in result_transi:
            if i not in result:
                result.append(nageur.Nageur(name=i["name"],lastname=i["last_name"], url_abcnatation=i["url"]))
    
    print("There are {} unique swimmer in the dataset".format(len(result)))
    return result


def findAllSwimmer_FFN_id(list_all_nageur : List[nageur.Nageur]) -> List[nageur.Nageur] :
    result = []
    for nageur in tqdm(list_all_nageur[:10],desc="find all swimmer in FFN Ranking"):
        url = "https://ffn.extranat.fr/webffn/_recherche.php?go=ind&idrch={}".format(nageur.get_full_name())
        sex,id_ffn = find_ffn_info_for_one_swimmer(url = url)
        nageur.set_id_ffn(id_ffn=id_ffn)
        nageur.set_sex(sex=sex)
    
    for nageur in list_all_nageur[:10]:
        if nageur.id_ffn == -1:
            print(f"error with {nageur}")
        # print(nageur.id_ffn)
    return list_all_nageur[:10]


def find_all_nage_by_swimmer(list_all_nageur : List[nageur.Nageur]):
    
    for nageur in tqdm(list_all_nageur, desc="Find all swim by swimmer"):
        # print(nageur)
        for nage in find_time_by_swimmer(id_ffn=nageur.get_id_ffn()):
            nageur.add_nage(nage)
    return list_all_nageur
       

    