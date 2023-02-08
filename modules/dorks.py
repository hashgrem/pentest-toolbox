from googlesearch import search

def dorks(query):

    response = search(query, num=10, stop=10, pause=2)

    links = []
    for l in response:
        links.append(l)

    displayInfos = f"\n\n===================================\n"
    displayInfos+= f" Result of query : "+query
    displayInfos+= f"\n===================================\n\n"

    for link in links:
        displayInfos+= f"{link}\n"

    return displayInfos