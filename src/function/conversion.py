import pandas as pd
from typing import List
from src.structure.nageur import Nageur
from src.structure.relai import NageRelai




def to_dataframe(nageur_list: List[Nageur]) -> pd.DataFrame:
    data = {'Name': [],
            'Lastname': [],
            'URL_ABCNatation': [],
            'ID_FFN': [],
            'Sex': [],
            'Bassin': [],
            'Type': [],
            'Time': [],
            'Age': [],
            'Pts': [],
            'Where': [],
            'Date': [],
            'Club': [],
            'Link_Relai': []}

    for nageur in nageur_list:
        for nage in nageur.nage:
            data['Name'].append(nageur.name)
            data['Lastname'].append(nageur.lastname)
            data['URL_ABCNatation'].append(nageur.url_abcnatation)
            data['ID_FFN'].append(nageur.id_ffn)
            data['Sex'].append(nageur.sex)
            data['Bassin'].append(nage.bassin)
            data['Type'].append(nage.type)
            data['Time'].append(nage.time)
            data['Age'].append(nage.age)
            data['Pts'].append(nage.pts)
            data['Where'].append(nage.where)
            data['Date'].append(nage.date)
            data['Club'].append(nage.club)
            data['Link_Relai'].append(nage.link_relai)

    df = pd.DataFrame(data)
    return df
            
def save_to_csv(dataframe: pd.DataFrame, file_path: str) -> None:
    dataframe.to_csv(file_path, index=False)


def read_csv_to_dataframe(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def to_dataframe_relai(nageur_list: List[NageRelai]) -> pd.DataFrame:
    data = {'List_name': [],
            'Sex': [],
            'Bassin': [],
            'Type': [],
            'Time': [],
            'Max_age': [],
            'Pts': [],
            'Link_Relai': []}

    for nageur in nageur_list:
        data['List_name'].append(nageur.nageur)
        data['Sex'].append(nageur.sex)
        data['Bassin'].append(nageur.bassin)
        data['Type'].append(nageur.type)
        data['Time'].append(nageur.time)
        data['Max_age'].append(nageur.max_age)
        data['Pts'].append(nageur.pts)
        data['Link_Relai'].append(nageur.link_relai)

    df = pd.DataFrame(data)
    return df