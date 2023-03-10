import requests
import json

def getCertificate(domain, htmlRender=False):
    domainName = str(domain)
    URL = "https://networkcalc.com/api/security/certificate/"+domainName
    query = requests.get(URL)
    displayInfos = ""

    if htmlRender:
        spacing = "<br>" # Pour le rendu PDF
    else:
        spacing = "\n"

    if query.status_code != 200:
        displayInfos += f"{spacing}Error. Check your domain name or the API website (https://networkcalc.com/api/)" 
    else:
        data = json.loads(query.text)
        status = data['status']

        if status == 'OK':
            if not htmlRender:
                displayInfos+= f"\n\n=================================================\n"
                displayInfos+= f"Certificate informations about "+data['meta']['hostname']
                displayInfos+= f"\n===================================================\n\n"
            
            if htmlRender:
                displayInfos+= f"<h2>Metadata</h2><br>"
            else:
                displayInfos+= f"{spacing}Metadata{spacing}"

            for key in data['meta'].keys():
                if htmlRender:
                    displayInfos+=f"<strong>{key}:</strong>\t{data['meta'][key]}{spacing}"
                else:
                    displayInfos+=f"{key}:\t{data['meta'][key]}{spacing}"
                    
            if htmlRender:
                displayInfos+= f"<h2>Certificate</h2><br>"
            else:
                displayInfos+= f"{spacing}Certificate{spacing}"
            for keys in data['certificate'].keys():
                if keys == 'raw':
                    if htmlRender:
                        displayInfos+=f"<strong>{keys}:</strong>\t{spacing}{data['certificate'][keys]}{spacing}"
                    else:
                        displayInfos+=f"{keys}:\t{spacing}{data['certificate'][keys]}{spacing}"
                else:
                    if htmlRender:
                        displayInfos+=f"<strong>{keys}:</strong>\t{data['certificate'][keys]}{spacing}"
                    else:
                        displayInfos+=f"{keys}:\t{data['certificate'][keys]}{spacing}"
                
        else:
            if status == 'NO_RECORDS':
                displayInfos = f"{spacing}No records. Check if the domain is reachable.{spacing}"
            else:
                displayInfos = "Error with the API, check https://networkcalc.com/api/dns/lookup/"

    return displayInfos
