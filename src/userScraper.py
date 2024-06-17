import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def getLinks(driver, username):
    url = "https://www.8a.nu/user/"+username+"/bouldering"
    login(driver, url)
    soup = BeautifulSoup(getHTMLDynamic(driver, url), parse_only=SoupStrainer('a'))

    links = []
    for link in soup:
        if link.has_attr('href') \
                and link['href'][:17] == "/crags/bouldering"\
                and link['href'][len(link)-7:] != "routes"\
                and link['href'] not in links:
            links.append(link['href'])
    return links

def getPersonals(driver, url):
    personals = []

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2.5)

    selectTimeFrame = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div/div/div/input")
    selectTimeFrame.click()
    allTime = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]")
    allTime.click()
    time.sleep(2.5)

    soup = BeautifulSoup(driver.page_source)

    grades = []
    for e in soup.select("div.grade-difficulty"):
        if e.text.find("9A") != -1 and 17.5 not in grades:
            grades.append(17.5)
        elif e.text.find("8C+") != -1 and 16.5 not in grades:
            grades.append(16.5)
        elif e.text.find("8C") != -1 and 15.5 not in grades:
            grades.append(15.5)
        elif e.text.find("8B+") != -1 and 14.5 not in grades:
            grades.append(14.5)
        elif e.text.find("8B") != -1 and 13.5 not in grades:
            grades.append(13.5)
        elif e.text.find("8A+") != -1 and 12.5 not in grades:
            grades.append(12.5)
        elif e.text.find("8A") != -1 and 11.5 not in grades:
            grades.append(11.5)
        elif e.text.find("7C+") != -1 and 10.5 not in grades:
            grades.append(10.5)
        elif e.text.find("7C") != -1 and 9.5 not in grades:
            grades.append(9.5)
        elif e.text.find("7B+") != -1 and 8.5 not in grades:
            grades.append(8.5)
        elif e.text.find("7B") != -1 and 8 not in grades:
            grades.append(8)
        elif e.text.find("7A+") != -1 and 7.5 not in grades:
            grades.append(7.5)
        elif e.text.find("7A") != -1 and 6.5 not in grades:
            grades.append(6.5)
        elif e.text.find("6C+") != -1 and 5.5 not in grades:
            grades.append(5.5)
        elif e.text.find("6C") != -1 and 5 not in grades:
            grades.append(5)
        elif e.text.find("6B+") != -1 and 4.5 not in grades:
            grades.append(4.5)
        elif e.text.find("6B") != -1 and 4 not in grades:
            grades.append(4)
        elif e.text.find("6A+") != -1 and 3.5 not in grades:
            grades.append(3.5)
        elif e.text.find("6A") != -1 and 3 not in grades:
            grades.append(3)
        elif e.text.find("5C") != -1 and 2.5 not in grades:
            grades.append(2.5)
        elif e.text.find("5B") != -1 and 2 not in grades:
            grades.append(2)
        elif e.text.find("5A") != -1 and 1.5 not in grades:
            grades.append(1.5)
        elif e.text.find("4C") != -1 and 1 not in grades:
            grades.append(1)
        elif e.text.find("4B") != -1 and 0.5 not in grades:
            grades.append(0.5)
        elif e.text.find("4A") != -1 and 0.4 not in grades:
            grades.append(0.4)
        elif e.text.find("3C") != -1 and 0.3 not in grades:
            grades.append(0.3)
        elif e.text.find("3B") != -1 and 0.2 not in grades:
            grades.append(0.2)
        elif e.text.find("3A") != -1 and 0.1 not in grades:
            grades.append(0.1)
        elif e.text.find("2\n") != -1 and 0.05 not in grades:
            grades.append(0.05)
        elif e.text.find("1\n") != -1 and 0.01 not in grades:
            grades.append(0.01)



    ascents = []
    for e in soup.select("div.number-grid-mobile"):
        num = (str(e).split("\n")[1])
        num = int(re.sub("[^0-9]", "", num))
        ascents.append(num)

    print(grades, ascents)

    for i in range(len(ascents)):
            for j in range(0,ascents[i]):
                personals.append(grades[i])
    return personals


def getHTMLDynamic(driver, url):
    driver.get(url)
    time.sleep(2.5)
    lgnbtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/a")
    lgnbtn.click()
    driver.execute_script("window.scrollTo(0, 1000,document.body.scrollHeight);")
    time.sleep(2.5)
    return driver.page_source

def login(driver, url):
    #todo: CHANGE LATER
    username = "conwellman@gmail.com"
    password = "conor1211"

    driver.get("https://vlatka.vertical-life.info/auth/realms/Vertical-Life/protocol/openid-connect/auth?client_id=8a-nu&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fwww.8a.nu%2Fcallback&resource=https%3A%2F%2Fwww.8a.nu&code_challenge=_3_bgltkZs-0moy06vgJqZfYBbGxj3sLuRfATrU6nDI&code_challenge_method=S256");

    user = driver.find_element(By.ID,"username")
    pw = driver.find_element(By.ID,"password")

    user.send_keys(username)
    pw.send_keys(password)
    btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "kc-login")))
    btn.click()



