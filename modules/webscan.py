from threading import Thread
from datetime import datetime
from colorama import Fore, Back, Style
import requests
import re
import sys
import time


def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


########################################
#   lil Nikto scan
#######################################
def check_server(url, pdf):
    HTML = ""
    try:
        if is_valid_url(url):
            response = requests.get(url)
        else:
            print(">>> [!] Incorrect url format")
            sys.exit()
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête : ", e)
        sys.exit(1)

    server = response.headers.get("Server")
    x_powered_by = response.headers.get("X-Powered-By")

    if server is not None:
        print(f">>> {Fore.GREEN}[+] Webserver is  : {server}{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>Web server : {server}<p>"
    if x_powered_by is not None:
        print(f">>> {Fore.GREEN}[+] Webserver uses :  {x_powered_by}{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>Server uses : {x_powered_by}</p>"

    # Vérifier si le serveur supporte la compression
    if "Content-Encoding" in response.headers:
        print(f">>> {Fore.YELLOW}[-] The server supports compression.{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>The server supports compression.</p>"
    else:
        print(f">>> {Fore.YELLOW}[-] The server doesn't support compression.{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>The server doesn't support compression.</p>"

    version_regex = re.compile(r"\d+\.\d+(\.\d+)?")
    for header in response.headers:
        match = version_regex.search(response.headers[header])
        if match:
            print(f">>> {Fore.GREEN}[+] Version of software might be found in the following header '{header}' : {match.group(0)} {Style.RESET_ALL}")
            if pdf:
                HTML += f"<p>Version of software might be found in the following header {header} : {match.group(0)}</p>"

    # Vérifier si l'URL cible redirige vers une autre URL
    if response.status_code in [301, 302]:
        loca_header = response.headers.get("Location")
        print(">>> [+] Target URL uses redirection towards : ", loca_header)
        if pdf:
            HTML += f"<p>Target URL uses redirection towards {loca_header}</p>"
    else:
        print(f">>> {Fore.YELLOW}[-] Target URL don't use any redirection{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>Target URL don't use any redirection</p>"

    # Vérifier si l'URL cible est protégée par une authentification basique HTTP
    if response.status_code == 401:
        print(">>> [+] Target URL is protected by a basic HTTP authentication")
        if pdf:
            HTML += f"<p>Target URL is protected by a basic HTTP authentication</p>"
    else:
        print(f">>> {Fore.YELLOW}[-] Target URL isn't protected by a basic HTTP authentication{Style.RESET_ALL}")
        if pdf:
            HTML += f"<p>Target URL isn't protected by a basic HTTP authentication</p>"

    #Others Nikto verifications
    headers = {
        "X-Frame-Options": "",
        "X-XSS-Protection": "",
        "X-Content-Type-Options": ""
    }

    try:
        response = requests.get(url, headers=headers)

        header1 = "The anti-clickjacking X-Frame-Options header is not present."
        header2 = "The X-XSS-Protection header is not defined."
        header3 = "The X-Content-Type-Options header is not set."

        if "X-Frame-Options" not in response.headers:
            print(f">>> {Fore.GREEN}[+] {header1}{Style.RESET_ALL}")
            HTML += f"<p>{header1}</p>"
        if "X-XSS-Protection" not in response.headers:
            print(f">>> {Fore.GREEN}[+] {header2}{Style.RESET_ALL}")
            HTML += f"<p>{header2}</p>"
        if "X-Content-Type-Options" not in response.headers:
            print(f">>> {Fore.GREEN}[+] {header3}{Style.RESET_ALL}")
            HTML += f"<p>{header3}</p>"
    except:
        print("Error occured while sending request to the URL")

    return HTML

def check_robots_txt(url):
    try:
        r = requests.get(url + "/robots.txt")
        if r.status_code == 200:
            print(f">>> {Fore.GREEN}[+] robots.txt is publicly accessible.{Style.RESET_ALL}")
            print(f">>> {Fore.GREEN}[+] Content of robots.txt: {Style.RESET_ALL}\n" + r.text)
        else:
            print(f">>> {Fore.YELLOW}[-] robots.txt is not publicly accessible.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(">>> [-] Exception Occured: " + str(e))

def find_github(url):
    try:
        r = requests.get(url + "/.git")
        valid_codes = [200, 204, 301, 302, 307, 401, 403, 407]
        if r.status_code in valid_codes:
            print(f">>> {Fore.GREEN}[+] A github repository has been found. Might be vulnerable to gitDumper{Style.RESET_ALL}")
        else:
            print(f">>> {Fore.RED}[-] No github repository found.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(">>> [-] Exception Occured: " + str(e))
        
########################################
#   Url discover / Lil python dirbuster
#######################################

def url_threads(url, sensitive_dir, codes):
    if is_valid_url(url):
        threads = []
        chunks = [sensitive_dir[w:w+5] for w in range(0, len(sensitive_dir), 5)]
        try:
            for each_chunk in chunks:
                threads.append(Thread(target=attack, args=(each_chunk, url, codes)))
            print(f">>> {Fore.GREEN}[+] Starting threads...{Style.RESET_ALL}")
            for t in threads:
                t.start()
        except:
            print(f">>> {Fore.RED}[-] An error has occured while starting threads.{Style.RESET_ALL}")
            sys.exit()   

def attack(wordlist, url, codes):
    for word in wordlist:
        word.rstrip()
        concat_url = url+word
        try:
            query = requests.get(concat_url).status_code
        except requests.exceptions.RequestException as e:
            print(">>> Error: ", e)
            sys.exit()
        
        if query in codes:
            print(f">>> {Fore.GREEN}[+] Found\t/{word} --------> {query}{Style.RESET_ALL}")

def url_discover(url):
    if not is_valid_url(url):
        print(f">>> {Fore.RED}[-] Error: url format isn't valid{Style.RESET_ALL}")
        sys.exit(1)
    else:
        if not url.endswith('/'):
            url += '/'
        try:
            with open('includes/common.txt', 'r') as w:
                wordlist  = w.read().splitlines()
            w.close()
        except:
            print(f"Error: check your wordlist path")
            sys.exit(1)
        valid_codes = [200, 204, 301, 302, 307, 401, 403, 407]
        r = requests.get(url).status_code
        if r not in valid_codes:
            print(f">>> {Fore.RED}[-] Error. Url unreachable.{Style.RESET_ALL}")
            sys.exit(1)
        else:
            print(f">>> {Fore.GREEN}[+] Started at {datetime.now()}{Style.RESET_ALL}")
            url_threads(url, wordlist, valid_codes)
