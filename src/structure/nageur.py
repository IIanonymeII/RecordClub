
from typing import List, Union
from src.structure import nage

class Nageur:

    def __init__(self, name: str, lastname: str, url_abcnatation: Union[str, None] = None, id_ffn : int = -1, sex: str = "?") -> None:
        self.name = name
        self.lastname = lastname
        self.url_abcnatation = url_abcnatation
        self.nage = []
        self.id_ffn = id_ffn
        self.sex = sex


    def add_nage(self, nage: nage.Nage) -> None:
        self.nage.append(nage)

    def set_id_ffn(self,id_ffn: int):
        self.id_ffn = id_ffn

    def set_sex(self,sex: str):
        self.sex = sex


    def get_full_name(self):
        return f"{self.lastname} {self.name}"
    
    def get_id_ffn(self):
        return int(self.id_ffn)

    def __repr__(self) -> str:
        return f'name: {self.name} ({self.sex}) - {self.lastname} url : {self.url_abcnatation}\n{self.nage}'
