from bs4 import BeautifulSoup

soup = BeautifulSoup(open("tiketkai.html"))
classtgl = soup.find(class_="itScheduleCombox")

#for tgl in classtgl:

