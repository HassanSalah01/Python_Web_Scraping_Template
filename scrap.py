from bs4 import BeautifulSoup
from requests_html import HTMLSession
s = HTMLSession()
url="https://eune.op.gg/champions"
response = s.get(url)
response.html.render()

soup = BeautifulSoup(response.content,"lxml")
champs=soup.find_all("a",{"class":"css-xars9p"})
arr = []
for i in champs:
    arr.append({"champ":i.small.text,"role":i.span.text})

for it in arr:
    with open('text2.txt','a') as data:
        data.write(str(it)+"\n") 
    




