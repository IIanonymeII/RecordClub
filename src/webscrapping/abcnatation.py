import requests
import datetime
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict



def list_swimmer_by_year(interval_year) -> list:
    
    result = []

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = {"_method": "POST",
            "data[ScCompetition][saison]": interval_year}
    url = "https://abcnatation.fr/club_manager/clubs/nageurs/050224277"
    soup = BeautifulSoup(requests.post(url, headers=headers,data=data).content, 'html.parser')
    
    for i in soup.find_all("table",{"class":"table"}):
        
        for tr in i:
            if "<tbody>" in str(tr):
                for tr_bis in tr:
                    if "<tr>" in str(tr_bis):
                        name     = tr_bis.td.text.split("(")[0]
                        url_name = tr_bis.find("a")["href"]
                        result.append({"url":url_name,**find_name_and_last_name(name)})
            else:
                if "<tr>" in str(tr):
                    name     = tr.td.text.split("(")[0]
                    url_name = tr.find("a")["href"]
                    result.append({"url":url_name,**find_name_and_last_name(name)})
    return result

def find_name_and_last_name(name:str) -> dict:
    name_found = ""
    last_name_found = ""
    isName = False
    len_name = len(name)
    for nbr_lettre in range(0,len_name):
        if name[nbr_lettre] == ' ' and nbr_lettre+2 <=len_name :
            if name[nbr_lettre+2].islower():
                isName = True
        
        if isName:
            name_found += name[nbr_lettre]
        else:
            last_name_found += name[nbr_lettre]
    name_found = name_found[1:] #just to erease the first space ex: > Ronan< become >Ronan<
    # print(f"found name : {name_found}\n last_name : {last_name_found}")
    return {"name":name_found,"last_name":last_name_found}



