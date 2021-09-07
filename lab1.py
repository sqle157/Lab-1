import requests

print(requests.__version__)
res = requests.get("http://google.com")
r = requests.get("https://raw.githubusercontent.com/sqle157/Lab-1/main/lab1.py")
open('github', 'wb').write(r.content)
fileName = open('github','r')
for line in fileName :
    print(line)