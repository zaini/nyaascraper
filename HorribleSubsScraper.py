import requests
from bs4 import BeautifulSoup
import webbrowser

quality = ["[480p]", "[720p]", "[1080p]"]

anime = input("Enter anime name (as uploaded by HorribleSubs): ")

while True:
    try:
        qselector = int(input("Select quality:\n0 = 480p\n1 = 720p\n2 = 1080p\n"))
        if qselector not in [0, 1, 2]:
            print("Enter a valid number: 0, 1 or 2")
        else:
            break

    except ValueError:
        print("Enter a valid number: 0, 1 or 2")

print("If nothing happens, the anime you entered isn't on HorribleSubs' torrents on nyaa.si. This will download the anime in the resolution you selected. If it doesn't find that resolution, it just don't download that episode so you'll have to do it manually.")
        
url = 'https://nyaa.si/user/HorribleSubs?f=0&c=0_0&q='+anime+'&p='

def URLPage(p, url):
    global html
    url = url + str(p)
    html = requests.get(url).content

def amountOfPages():
    page = 0
    while True:
        page += 1
        URLPage(page, url)
        try:
            BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[0].find_all(class_ = "text-center")[0].find_all("a", href = True)[1]['href']
        
        except IndexError:
            return page - 1

def amountOfRows(p):
    row = 0
    while True:
        row += 1
        URLPage(p, url)
        try:
            BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all(class_ = "text-center")[0].find_all("a", href = True)[1]['href']
        
        except IndexError:
            return row

for page in range(1, amountOfPages()+1):
    URLPage(page, url)
    for row in range(0, amountOfRows(page)):
        if "[HorribleSubs]" not in str(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[2]):
            if quality[qselector] in str(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[1]):
                print(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[1].get_text())
                webbrowser.open(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all(class_ = "text-center")[0].find_all("a", href = True)[1]['href'])

        else:
            if quality[qselector] in str(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[2]):
                print(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[2].get_text())
                webbrowser.open(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all(class_ = "text-center")[0].find_all("a", href = True)[1]['href'])
print("Complete")
