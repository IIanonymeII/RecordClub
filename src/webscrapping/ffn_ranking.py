


import datetime
import re
from typing import List, Union
from bs4 import BeautifulSoup
import requests
from src.structure import nage

from src.webscrapping.filter_data import convert_date, convert_time, extract_age, extract_city, extract_nage_info, extract_name, find_nage
from src.structure.relai import NageRelai


def find_ffn_info_for_one_swimmer(url: str) -> int:
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status() # verifed status of request
    except requests.exceptions.RequestException as esx:
        print(f"Error: Unable to fetch data from {url}. {esx}")
        return -1

    try:
        # Parse the JSON data from the response
        json_search = response.json()
    except ValueError as exc:
        print(f"Error: Unable to parse JSON data. {exc}")
        return "?",-1
    
    if  "Individu non trouv\u00e9 !" in str(json_search):
        print("Individual not found.")
        return "?",-1
    
     
    # Process the JSON data
    for json_ in json_search:
        # If the length of the JSON response is 1 or the 'clb' value is "LANNION NATATION"
        if len(json_search) == 1 or json_["clb"] == "LANNION NATATION":
            try:
                sex = "F"
                if " H " in json_["ind"]:
                    sex = "H"
                # print(f"iuf: {json_['iuf']}")
                return sex,int(json_['iuf'])
            except KeyError as e:
                print(f"Error: Key not found in JSON data. {e}")
                return "?",-1



from requests.structures import CaseInsensitiveDict          
bassins = ["25","50"] # 25m and 50m
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

def find_time_by_swimmer(id_ffn: int):
    result = []
    swimming_type = "?"
    sexe = "?"
    url = "https://ffn.extranat.fr/webffn/nat_recherche.php?idact=nat"
    for bassin in bassins:
        data = {"idrch_id":id_ffn,
                "idbas":bassin,
                "idopt":
                        [
                        "",
                        "prf"
                        ]
                } 
        soup = BeautifulSoup(requests.post(url, headers=headers,data=data).content, 'html.parser')

        if "Messieurs" in str(soup):
            sexe = "M"
        else:
            sexe = "F"
        for table in soup.find_all("table",{"id":"styleNoBorderNoBottom"}):
            if "LANNION NATATION" in str(table):
                for tr in table:
                    if " Bassin :" in str(tr):
                        swimming_type = find_nage(text=tr.text)
                    elif "pts" in str(tr) or "ans" in str(tr):
                        age = tr.find("td",{"class":"nat-age"}).text.replace("(","").replace(" ans)","")
                        relais = bool(tr.find("td",{"class":"nat-relais"}).text)
                        relais_link = ""
                        temps = convert_time(tr.find("td",{"class":"nat-temps"}).text)
                        where = extract_city(tr.find("td",{"class":"nat-lieu"}).text)
                        date = convert_date(tr.find("td",{"class":"nat-date"}).text)
                        club = tr.find("td",{"class":"nat-structure"}).text

                        pts = int(tr.find("td",{"style":"font-style: italic; color: purple; text-align: right; padding-left: 5px;"}).text.replace(" pts",""))
                        

                        if relais :
                            relais_link = tr.find("td",{"class":"nat-results"}).a["href"]
                            relais_link = "https://ffn.extranat.fr/webffn/"+relais_link

                        result.append(nage.Nage(bassin=bassin,
                                                type=swimming_type,
                                                time=temps,
                                                age=age,
                                                pts=pts,
                                                where=where,
                                                date=date,
                                                club=club,
                                                link_relai=relais_link))
                        # print(f"{result[-1]}")
    return result

def find_bassin_for_relai(text:str) -> int:
    bassin = 50
    if "25 m" in text:
        bassin = 25
    return bassin

def find_sex_for_relai(text:str) -> str:
    sex = "?"
    if "Dames" in text:
        sex = "F"
    elif "Mixtes" in text:
        sex = "A"
    else:
        sex = "H"
    return sex


def find_time_for_relai(text: str) -> Union[str, datetime.datetime]:
    time = "?"
    if text == "DSQ":
        time = "DSQ"
    else:
        time = convert_time(text)
    
    return time

def find_pts_for_relai(text: str) -> Union[str, int]:
    pts = ".."
    if bool(text):
        pts = int(text.replace(" pts",""))
    return pts

def find_is_relai(text: Union[str,None]) -> bool:
    is_relai = False
    if  text and ("x" in text):
        is_relai = True

    return is_relai

    
def find_relai_swimmer_in_compet(url: str) -> List[NageRelai]:
    relai_result = []
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find a specific element using its tag name and (optionally) its attributes
    results = soup.find_all('table')
    
    # Print the results
    is_club = False    
    is_relai = False
    bassin = find_bassin_for_relai(str(soup.find("fieldset",{"class":"enteteCompetition"})))
    
    for result in results:
        if "LANNION NATATION" in str(result):

            nage_type = "?"
            sex = "?"
            for tr in result.find_all("tr"):
                if 'class="tabColInsert' in str(tr):
                    nage_type_brut = tr.find("div",{"class":"tabColInsertTextLeft"}).text
                    nage_type = extract_nage_info(nage_type_brut)
                    sex = find_sex_for_relai(nage_type_brut)

                    is_relai = find_is_relai(nage_type)
                    is_club = False

                elif "DNS dec" in str(tr):
                    is_club = False
                    
                elif "LANNION NATATION" in str(tr)  and is_relai:
                    time_str = tr.find("td",{"class":"tabColTps"}).text
                    time = find_time_for_relai(time_str)

                    pts_str = tr.find("td",{"class":"tabColPts"}).text
                    pts = find_pts_for_relai(pts_str)

                    relai_result.append(NageRelai(bassin=bassin,sex=sex,type=nage_type, time=time, pts=pts, link_relai=url, nageur=[]))

                    is_club = True
                
                elif "spacer.gif" in str(tr): 
                    is_club = False

                else:
                    pass
                
                if is_club and is_relai:
                    try:
                        t = tr.find("td",{"class":"tabColInd"})
                        t2 = t.find("a",{"class":"tooltip"}).get_text()
                        t3_name = extract_name(t2)
                        t3_age = extract_age(t2)
                        relai_result[-1].set_max_age(age=int(t3_age))
                        relai_result[-1].add_nageur(t3_name)
                    except:
                        print(relai_result[-1])
                        print(url)
                        raise
                    
    return relai_result

