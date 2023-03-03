from colorama import Fore, Back, Style, init
import requests

def checkusername(username):

    url = ['https://www.reddit.com/user/',
    'https://www.youtube.com/@',
    'https://github.com/',
    'https://instagram.com/',
    'https://www.twitch.tv/',
    'https://www.root-me.org/',
    'https://www.komoot.com/user/',
    'https://myspace.com/',
    'https://open.spotify.com/user/',
    'https://soundcloud.com/',
    'https://www.patreon.com/',
    'https://www.pinterest.com/',
    'https://www.wattpad.com/user/',
    'https://cracked.io/',
    'https://www.flickr.com/people/',
    'https://en.gravatar.com/profiles/']
    
    displayInfos = f"\n\n===================================\n"
    displayInfos+= f"Account for user "+username
    displayInfos+= f"\n===================================\n"

    

    for i in range(len(url)):
        r = requests.get(url[i]+username)
        text = r.text
        status = r.status_code
        
        if url[i] == 'https://instagram.com/':
           
            if 'Instagram photos' in text:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://github.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.reddit.com/user/':

            if 'pseudo ' in text:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.youtube.com/@':

            if '404' in text:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.twitch.tv/':

            if 'og:video:width' in text:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.root-me.org/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.komoot.com/user/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://myspace.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://open.spotify.com/user/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://soundcloud.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.patreon.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
        
        elif url[i] == 'https://www.pinterest.com/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.wattpad.com/user/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://cracked.io/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://www.flickr.com/people/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

        elif url[i] == 'https://en.gravatar.com/profiles/':

            if status == 404:
                displayInfos+= f">>>{Fore.RED} [-] NOT Found on "+url[i]+username+f"{Style.RESET_ALL}\n"
            else:
                displayInfos+= f">>>{Fore.GREEN} [+] Found on "+url[i]+username+f"{Style.RESET_ALL}\n"

    return displayInfos