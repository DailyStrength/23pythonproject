# import requests
# import re

# req = requests.get("http://ipconfig.kr")
# out_addr = re.search(r'IP Address : (\d{1, 3}\.\d{1, 3}\.\d{1, 3})\.\d{1, 3}', req.text[1])
# print(out_addr)

from urllib import request

def get_external_ip():
    return request.urlopen('https://ident.me').read().decode('utf8')    

ip = get_external_ip()
print("외부 ip:",ip)
