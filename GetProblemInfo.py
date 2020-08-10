import requests; 
import zipfile
from bs4 import BeautifulSoup as soup

def getProblemInfo(url):
    rq = requests.get(url)
    text = rq.text
    pageSoup = soup(text, "html.parser")
    h2lines = pageSoup.find_all("h2")

    name = ""
    firstLine, secondLine = str(h2lines[0]).split(" "), str(h2lines[1]).split(" ")
    for i in range(3, len(secondLine) - 1):
        name += secondLine[i] + " "
    name = name[0 : len(name) - 1]
    num = int(secondLine[2][0])
    
    year, month = firstLine[2], firstLine[3]
    if month == "US":
        month += firstLine[4]

    level = firstLine[len(firstLine) - 2]

    getTesterUrl = "http://usaco.org/index.php?page="
    if firstLine[4] == "Open":
        getTesterUrl += "open" + year[2 : 4] + "results"
    else:
        lowermonth = month.lower()
        getTesterUrl += lowermonth[0 : 3] + year[2 : 4] + "results"

    testrq = requests.get(getTesterUrl)
    testtext = testrq.text
    testPageSoup = soup(testtext, "html.parser")
    alines = testPageSoup.find_all("a")

    candidates = []
    for i in range(0, len(alines)):
        thisa = str(alines[i])
        if "Test data" in thisa and level.lower() in thisa:
            candidates.append(thisa)

    downloadUrl = "http://usaco.org/" + candidates[num - 1].split('"')[1]
    datarq = requests.get(downloadUrl)
    open("data.zip", "wb").write(datarq.content)
    with zipfile.ZipFile("./data.zip", "r") as unzip:
        unzip.extractall()
    open("out.out", "w")

    return [name, year, month, level]