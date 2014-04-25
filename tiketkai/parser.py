from bs4 import BeautifulSoup
import  urllib.request

def getLastDate(soupObj):
    objList = None
    lastdate = None

    comboClass = soupObj.findAll(class_="itScheduleCombox")

    for combo in comboClass:
        if combo['name'] == 'tanggal':
            objList = combo

    try:
        for obj in objList:
            lastdate = obj.string
        return lastdate
    except TypeError as e:
        print("Webpage structure not found. Quitting...")
        return None

def fetchPage(url):
    # add a header to define a custon User-Ageny
    headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

    try:
        req = urllib.request.Request(url, None, headers)
        data = urllib.request.urlopen(req)
        return data
    except:
        return None
    
#our url
url = "https://tiket.kereta-api.co.id/"

page = fetchPage(url)
mydate = None
if page is not None:
    soup = BeautifulSoup(page.read())
    mydate = getLastDate(soup)

if mydate is None:
    print("something error. Sorry")
else:
    print(mydate)