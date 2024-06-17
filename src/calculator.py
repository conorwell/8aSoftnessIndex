from selenium import webdriver
import userScraper as us
import boulderScraper as bs
from statistics import mean


def getScore(username):
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )
    driver = webdriver.Firefox()
    links = us.getLinks(driver, username)
    difs = []
    personals = us.getPersonals(driver,username)

    for i in range(0, int(len(links)/4), 1):
        print(links[i])
        consensus = bs.getConsensus(driver, "https://www.8a.nu" +links[i])
        dif = personals[i] - consensus
        difs.append(dif)
        print(" Consensus: " + str(consensus) + "\n Personal: " + str(personals[i]) + "\n Difference: " + str(dif));

    softness = mean(difs)
    print("Final score: " + str(softness))
    driver.quit
    return softness