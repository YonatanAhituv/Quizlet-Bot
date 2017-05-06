from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
loggedIn = False
oneQuiz = False
timesSkipped = 0
dominationTold = False
with open('email.txt', 'r') as myfile:
    email=myfile.read().replace('\n', '')
with open('password.txt', 'r') as myfile:
    password=myfile.read().replace('\n', '')
print("Type in: 1, to do just one quizlet, type in 2, to do multiple")
runTypeInput = input("I choose: #")
if runTypeInput == "1":
    oneQuiz = True
if runTypeInput == "2":
    oneQuiz = False
chromedriver = "(Insert ChromeDriver path here)"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1600, 1000)
def click(id):
    try:
        browser.find_element_by_id("definition-"+id).click()
        browser.find_element_by_id("term-"+id).click()
    except:
        pass
def login():
    try:
        browser.find_element_by_xpath("//div[@class='TrophiesModal-loggedOutActions']/div/button").click()
    except:
        browser.find_element_by_xpath("//a[@href][2]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='UISocialButton']/a").click()
    browser.find_element_by_xpath("//input[@type='email']").send_keys(email+Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)

pageID = (Website ID)
if oneQuiz == False:
    while True:
        if timesSkipped > 80:
            browser.quit()
            if dominationTold == False:
                print("Quizlet Domination Complete.")
                dominationTold = True
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            time.sleep(1)
            if not loggedIn:
                login()
                loggedIn = True
            pageID = pageID + 1
            time.sleep(2)
        except:
            pass
            pageID = pageID + 1
if oneQuiz == True:
    while True:
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            time.sleep(1)
            if not loggedIn:
                login()
                loggedIn = True
            time.sleep(2)
        except:
            pass
            pageID = pageID + 1
