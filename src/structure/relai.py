import datetime
from typing import List, Union



class NageRelai:
    def __init__(self, 
                 bassin:str, 
                 type: str, 
                 time: Union[datetime.datetime, str], 
                 pts: int, 
                 sex: str,
                 link_relai: str = "",
                 nageur: List[str] = [],
                 max_age : int = -1) -> None:
        self.bassin = bassin
        self.type = type
        self.time = time 
        self.sex = sex       
        self.pts = pts
        self.link_relai = link_relai
        self.nageur = nageur
        self.max_age = max_age

    @staticmethod
    def format_time(time_object: Union[datetime.datetime,str]):
        result = "DSQ"
        if isinstance(time_object, datetime.date):
            result = time_object.strftime("%M:%S.%f")[:-4]
        return result

    def add_nageur(self, nageur: str) -> None:
        self.nageur.append(nageur)

    def set_max_age(self, age: int) -> None:
        
        self.max_age = max(age,self.max_age)
        
    def __repr__(self) -> str:
        return f"{self.bassin} m => {self.type} ({self.sex}): {self.format_time(self.time)} - {self.pts} pts - '{', '.join(self.nageur)}'"