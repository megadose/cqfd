import requests
import urllib.parse
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
ua = UserAgent(verify_ssl=False)

def cqfd(name):
    headers = {
        'User-Agent': ua.firefox,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get('https://www.skypli.com/search/'+urllib.parse.quote(name), headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    result=[]
    for i in soup.findAll("div",attrs={"class":"search-results__block"}):
        name = i.find("span",attrs={"class":"search-results__block-info-fullname"}).getText()
        username=i.find("span",attrs={"class":"search-results__block-info-username"}).getText()
        image=i.find("div",attrs={"class":"search-results__block-image"})["style"].split("background-image: url('")[1].split("'")[0]
        if image=="/assets/images/no_image.jpg":
            image=None
        result.append({"name":name,"username":username,"image":image})
    return(result)
