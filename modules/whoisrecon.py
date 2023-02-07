import whois as w

def whois_query(domain):
    displayInfos = f"\n\n===================================\n"
    displayInfos+= f"Whois lookup for "+ domain
    displayInfos+= f"\n===================================\n"
    try:
        data = w.whois(domain)
        displayInfos+= str(data)
        return displayInfos
    except Exception as e:
        error =  "Error: " + str(e)
        displayInfos += error
        return displayInfos

