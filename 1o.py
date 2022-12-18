from Crypto import Random
from random import randint
from base64 import b64encode
from Crypto.Cipher import AES
from pystyleclean import *
m = Colors.purple
r = Colors.red
w = Colors.white
i = input
System.Clear()
Cursor.HideCursor()

class O1():
    obf = i(f" {m}[{r}*{m}] Deseas obfuscar el archivo? [y/n]: {r}> {w}")
    if obf.lower() == 'y' or obf.lower() == 'yes' or obf.upper() == 'Y' or obf.upper() == 'YES' or obf.lower() == 's' or obf.lower() == 'si' or obf.upper() == 'S' or obf.upper() == 'SI':
        IV = Random.new().read(AES.block_size)
        key = u''
        for I in range(8):
            key = key + chr(randint(0x4E00, 0x9FA5))
        with open(f'main.py') as f:
            _file = f.read()
            imports = ''
            ifile = _file.splitlines()
            for I in ifile:
                if I.startswith("import") or I.startswith("from"):
                    imports += I+';'
        with open(f'main.py', "wb") as f:
            EBytes = b64encode(_file.encode())
            OBFBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(EBytes)
            f.write(f'from Crypto.Cipher import AES;exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({OBFBytes})).decode())'.encode())
            f.close()
            exit()
