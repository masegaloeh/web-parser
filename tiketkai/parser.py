from bs4 import BeautifulSoup

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


soup = BeautifulSoup(open("tiketkai.html"))

mydate = getLastDate(soup)

if mydate is None:
    print("something error. Sorry")
else:
    print(mydate)