from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, NoSuchElementException
import os
import time
import sys
import json
loggedIn = False
oneQuiz = False
try:
    with open ('info.json', 'r') as myfile:
        info=json.loads(myfile.read())
    with open('email.txt', 'r') as myfile:
        email=myfile.read().replace('\n', '')
    with open('password.txt', 'r') as myfile:
        password=myfile.read().replace('\n', '')
except:
    reply = raw_input('Email.txt and Password.txt not found...Would you like to continue? (y or n)')
    if (reply == "y" or reply == "Y"):
        print("Continuing...")
    if (reply == "n" or reply == "N"):
        print("Bye!")
        sys.exit()
pageID = info["pageID"]
successes = info["successes"]
failures = info["failures"]
print("INFO: Only close the browser, not the script or terminal")
print("Type in: 1, to do just one quizlet, type in 2, to do multiple")
runTypeInput = input("I choose: #")
if runTypeInput == "1":
    oneQuiz = True
if runTypeInput == "2":
    oneQuiz = False
chromedriver = "(Insert chromedriver path here)"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1600, 1000)
def click(id):
    try:
        browser.find_element_by_id("definition-"+id).click()
        browser.find_element_by_id("term-"+id).click()
    except:
        pass
def save(info, pageID1, successes1, failures1):
    try:
        info["pageID"] = pageID1
        info["successes"] = successes1
        info["failures"] = failures1
    except:
        pass
    with open ('info.json', 'r+') as myfile:
        info=myfile.write(json.dumps(info))

def login():
    try:
        browser.find_element_by_xpath("//div[@class='TrophiesModal-loggedOutActions']/div/button").click()
    except:
        browser.find_element_by_xpath("//a[@href][2]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='UISocialButton']/a").click()
    try:
        browser.find_element_by_xpath("//input[@type='email']").send_keys(email+Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
    except:
        pass

if oneQuiz == False:
    while True:
        save(info, pageID, successes, failures)
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            successes = successes + 1
            if not loggedIn:
                time.sleep(1)
                login()
                loggedIn = True
            pageID = pageID + 1
            time.sleep(2)
        except NoSuchWindowException:
            sys.exit()
        except WebDriverException as e:
            failures = failures + 1
            pageID = pageID + 1
        except NoSuchElementException:
            failures = failures + 1
            pageID = pageID + 1
        except:
            print("Failure...")
            pass
if oneQuiz == True:
    while True:
        save(info, pageID, successes, failures)
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            successes = successes + 1
            if not loggedIn:
                login()
                loggedIn = True
            time.sleep(2)
        except NoSuchWindowException:
            sys.exit()
        except WebDriverException:
            sys.exit()
        except NoSuchElementException:
            failures = failures + 1
            pageID = pageID + 1
