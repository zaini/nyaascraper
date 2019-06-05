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

#Add validation
print("Now enter the range of episodes you want to download. \nFor example to download all episodes between and including episodes 1 and 10, enter 1 and then 10.\nIf you want to download the whole series, just press enter. You could then manually delete the torrents you don't want to keep from your client.\n")
lrange = int(input("Enter the episode you want to start downloading from:\n"))
urange = int(input("Enter the episode you want to stop downloading at:\n"))

print("If nothing happens, the anime you entered isn't on HorribleSubs' torrents on nyaa.si. This will download the anime in the resolution you selected. If it doesn't find that resolution, it just doesn't download that episode so you'll have to do it manually.\n")

url = 'https://nyaa.si/user/HorribleSubs?f=0&c=0_0&q='+anime+'&o=asc&p='

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

def downloader(episodename):
    if quality[qselector] == episodename.split()[-1].strip(".mkv") and lrange <= float(episodename.split()[-2]) <= urange:            
        print(episodename.strip(".mkv"))
        #webbrowser.open(BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all(class_ = "text-center")[0].find_all("a", href = True)[1]['href'])
        
    elif float(episodename.split()[-2]) > urange:
        print("Completed!")
        print(exit())

for page in range(1, amountOfPages()+1):
    URLPage(page, url)
    for row in range(0, amountOfRows(page)):
        episodename = BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[1].get_text()
        if "[HorribleSubs]" == episodename.split()[0]:
            downloader(episodename)

        else:
            episodename = BeautifulSoup(html, features = "lxml").find_all(class_ = "success")[row].find_all("a")[2].get_text()
            downloader(episodename)
