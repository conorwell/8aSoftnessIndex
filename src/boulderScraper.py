import time
import selenium
from bs4 import BeautifulSoup

def getConsensus(driver, link):
    driver.get(link)
    time.sleep(1)
    html = driver.page_source

    consensus = 0
    doc = BeautifulSoup(html)
    tags = doc.select("div.nu8a-chip.xs-size")
    selectedTags = []


    for tag in tags:
        allTags = str(tag).split(">")
        for e in allTags:
            if e.find('nu8a-chip xs-size') == -1 and e != "" and len(e) > 22 and len(e) < 26:
                selectedTags.append(e)

    consensus = 0
    ascents = 0
    for e in selectedTags:
        if e.find("9A") != -1:
            consensus += 17.5
            ascents += 1
        elif e.find("8C+") != -1:
            consensus += 16.5
            ascents += 1
        elif e.find("8C") != -1:
            consensus += 15.5
            ascents += 1
        elif e.find("8B+") != -1:
            consensus += 14.5
            ascents += 1
        elif e.find("8B") != -1:
            consensus += 13.5
            ascents += 1
        elif e.find("8A+") != -1:
            consensus += 12.5
            ascents += 1
        elif e.find("8A") != -1:
            consensus += 11.5
            ascents += 1
        elif e.find("7C+") != -1:
            consensus += 10.5
            ascents += 1
        elif e.find("7C") != -1:
            consensus += 9.5
            ascents += 1
        elif e.find("7B+") != -1:
            consensus += 8.5
            ascents += 1
        elif e.find("7B") != -1:
            consensus += 8
            ascents += 1
        elif e.find("7A+") != -1:
            consensus += 7.5
            ascents += 1
        elif e.find("7A") != -1:
            consensus += 6.5
            ascents += 1
        elif e.find("6C+") != -1:
            consensus += 5.5
            ascents += 1
        elif e.find("6C") != -1:
            consensus += 5
            ascents += 1
        elif e.find("6B+") != -1:
            consensus += 4.5
            ascents += 1
        elif e.find("6B") != -1:
            consensus += 4
            ascents += 1
        elif e.find("6A+") != -1:
            consensus += 3.5
            ascents += 1
        elif e.find("6A") != -1:
            consensus += 3
            ascents += 1
        elif e.find("5C") != -1:
            consensus += 2.5
            ascents += 1
        elif e.find("5B") != -1:
            consensus += 2
            ascents += 1
        elif e.find("5A") != -1:
            consensus += 1.5
            ascents += 1
        elif e.find("4C") != -1:
            consensus += 1
            ascents += 1
        elif e.find("4B") != -1:
            consensus += 0.5
            ascents += 1
        elif e.find("Hard") != -1:
            consensus += 0.25
        elif e.find("Soft") != -1:
            consensus -= 0.25

    return (consensus/ascents)