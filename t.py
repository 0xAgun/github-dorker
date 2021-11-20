import requests
from bs4 import BeautifulSoup

org = input("Enter the org eg. google: ")
base_url = f"https://github.com/search?q={org}+%22database_password%22"

send_req = requests.get(base_url).text
soup = BeautifulSoup(send_req, 'html.parser')

repo = soup.find_all('a',class_='v-align-middle')

for a in repo:
    j = "https://github.com"+a['href']
    save = open("links.txt",'a')
    save.write(j+"\n")
    save.close()
    

with open('links.txt', 'r') as links:
    for x in links:
        srtip_file = x.rstrip()
        re3w = requests.get(srtip_file).text
        soop = BeautifulSoup(re3w, 'html.parser')
        plain_text_descc = soop.find_all('p', class_='f4 mt-3')
        #print(plain_text_descc)
        for textx in plain_text_descc:
            texts = textx.text
            print(texts)
