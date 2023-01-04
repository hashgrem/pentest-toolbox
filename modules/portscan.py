from datetime import datetime
import nmap

# inspired about the doc
def Nmap(ip, htmlRender=False):

    ip = str(ip)
    nm = nmap.PortScanner()
    displayInfo = ""

    if htmlRender:
        spacing = "<br>" # Pour le rendu PDF
    else:
        spacing = "\n"
    
    if not htmlRender:
        print(f"[+] Scan started at {datetime.now()}\n")

    nm.scan(ip, '21-443')
    versions = []

    for host in nm.all_hosts():
        displayInfo+=f"Host: {host} {nm[host].hostname()}{spacing}"
        displayInfo+=f"State: {nm[host].state()}{spacing}"
        for proto in nm[host].all_protocols():
            displayInfo+=f"---------------------{spacing}"
            displayInfo+=f"PORT\t\tSTATE\t\tPRODUCT\t\tVERSION{spacing}"
            lport = nm[host][proto].keys()
            for port in lport:
                if len(str(port)+str("/")+str(proto)) < 8:
                    space = "\t\t"
                else:
                    space = "\t"
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                state = nm[host][proto][port]['state']

                displayInfo+=f"{port}/{proto}{space}{state}\t\t{product}\t\t{version}{spacing}"
                if product != " " and product != "":
                    versions.append(product+" "+version)
            
            for v in versions:
                if v == '' or v == ' ':
                    versions.pop()
                    
            if len(versions) == 0:
                versions.append("Aucune version trouvée")

    return displayInfo, versions

#print(Nmap('supdevinci.fr'))