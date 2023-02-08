from bs4 import BeautifulSoup as htmlparser
import requests

def lookuphone(phone_number):

    displayInfos = f"\n\n===================================\n"
    displayInfos+= f"Informations for number "+phone_number
    displayInfos+= f"\n===================================\n"

    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    infos = {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No informations" for i, k in enumerate(infos) if not i % 2}
    
    

    for info in infos:
        displayInfos+= f"{info}: {infos[info]}\n"
    return displayInfos