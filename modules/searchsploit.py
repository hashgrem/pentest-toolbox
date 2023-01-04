from googlesearch import search  

def searchsploit(service, htmlRender=False):

    query = service+" exploit vuln"
    res = search(query, num=10, stop=10, pause=2)

    displayInfos = ""

    if htmlRender:
        spacing = "<br>" # Pour le rendu PDF
    else:
        spacing = "\n"
    
    links = []
    for l in res:
        links.append(l)
    
    if not htmlRender:
        displayInfos+= f"\n\n===================================\n"
        displayInfos+= f" Exploits concernant "+service
        displayInfos+= f"\n===================================\n\n"

    for link in links:
        displayInfos+= f"{link}{spacing}"

    return displayInfos
