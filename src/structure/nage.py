import datetime

class Nage:
    def __init__(self, bassin:str, type: str, time: datetime, age: int, pts: int, where: str, date: datetime, club: str, link_relai: str = "") -> None:
        self.bassin = bassin
        self.type = type
        self.time = time
        self.age = age
        self.pts = pts
        self.where = where
        self.date = date
        self.club = club
        self.link_relai = link_relai
    
    @staticmethod
    def format_time(time_object: datetime):
        return time_object.strftime("%M:%S.%f")[:-4]
    
    @staticmethod
    def format_date(date_object: datetime):
        # Format the datetime object as a string
        return date_object.strftime("%d/%m/%Y")

    def __repr__(self) -> str:
        return f"{self.type} : {self.format_time(self.time)} - {self.pts} pts - '{self.link_relai}'"
