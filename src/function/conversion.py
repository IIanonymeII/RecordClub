import pandas as pd
from typing import List
from src.structure.nageur import Nageur




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