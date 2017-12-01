issueRead = False
def checkForUpdatesC(self):
    import requests, os
    titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
    pasteV = titleget.text
    pasteV = float(pasteV)
    if pasteV > version:
        fname = os.path.basename(__file__)
        reply = requests.get('https://raw.githubusercontent.com/AtomicCoding/Quizlet-Bot/master/main.py')
        code = reply.text
        with open(fname, 'r') as f1:
            oldcode = f1.read()
        if not oldcode == code:
            return True
        if oldcode == code:
            return False
    else:
        return False
def complain(error, body=None, assignee=None, milestone=None, labels=["bug"]):
    import sys
    try:
        updateNeeded = update.checkForUpdatesC()
    except:
        updateNeeded = False
    import platform
    computerName = platform.node()
    if computerName == "atomicsystem.lan":
        dev = True
    else:
        dev = False
    if dev == True:
        if updateNeeded == True:
            updateNeeded = False
            print("You are on an outdated version. Overriding...")
    if updateNeeded == True:
        print("ERROR: Cannot report issue due to outdated version, sorry.")

        sys.exit()
    else:
        import json
        with open ('info.json', 'r') as myfile:
            info=json.loads(myfile.read())
        USERUSERNAME = info["USERUSERNAME"]
        USERPASSWORD = info["USERPASSWORD"]
        if issueRead == False:
            print("An error has occured titled:", error+".")
        if issueRead == True:
            print("An error was read titled:", error+".")
        try:
            import requests
            cantWork = False
        except:
            cantWork = True
        if cantWork == False:
            try:
                import urllib
                urllib.request.urlopen('http://216.58.192.142', timeout=1)
                cantWork = False
            except:
                cantWork = True
        if cantWork == True:
            while True:
                errorIssue = input("ERROR: COULD NOT IMPORT REQUESTS OR CONNECT TO THE INTERNET, WOULD YOU LIKE THE BOT TO SAVE THE ISSUE TO A FILE AND REPORT IT LATER (Y OR N)? >>> ")
                errorIssue = errorIssue.upper()
                if errorIssue == "Y":
                    import os, inspect
                    directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
                    os.chdir(directory)
                    try:
                        with open('issue.txt', 'w+') as w1:
                            w1.write(error)
                        print("Created File Successfully!")
                        print("Exiting...")
                        break
                    except:
                        print("Failed to create file. ):")
                        print("Exiting...")
                        break
                elif errorIssue == "N":
                    break

            from sys import exit

            exit()
        else:
            createissue = input("Would you like the script to create an issue for you (Y or N)? >>> ")
            if createissue == "y" or createissue == "Y":
                if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                    gitHubLoggedIn = False
                elif USERUSERNAME == "ns" and USERPASSWORD == "ns":
                    gitHubLoggedIn = False
                else:
                    gitHubLoggedIn = True
                while gitHubLoggedIn == False:
                    print("None of this data is transmitted, it is just used to create an issue on GitHub.")
                    gitHubLoggedIn = True
                    if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                        print("This is not saved, it's just used to report the issue.")
                        USERUSERNAME = input("What is your GitHub username? >>> ")
                        USERPASSWORD = getpass.getpass("What is your GitHub password? >>> ")
                        CONFIRMPASS = getpass.getpass("Confirm your password: >>> ")
                    if USERUSERNAME == "ns" and USERPASSWORD == "ns":
                        print("This is not saved, it's just used to report the issue.")
                        USERUSERNAME = input("What is your GitHub username? >>> ")
                        USERPASSWORD = getpass.getpass("What is your GitHub password? >>> ")
                        CONFIRMPASS = getpass.getpass("Confirm your password: >>> ")
                    if not USERPASSWORD == CONFIRMPASS:
                        gitHubLoggedIn = False
                REPO_OWNER = 'AtomicCoding'
                REPO_NAME = 'Quizlet-Bot'
                '''Create an issue on github.com using the given parameters.'''
                # Our url to create issues via POST
                url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
                # Create an authenticated session to create the issue
                session = requests.Session()
                session.auth = (USERUSERNAME, USERPASSWORD)
                # Create our issue
                issue = {'title': error,
                         'body': body,
                         'assignee': assignee,
                         'milestone': milestone,
                         'labels': labels}
                # Add the issue to our repository
                r = session.post(url, json.dumps(issue))
                if r.status_code == 201:
                    print('Successfully created Issue "%s"' % error)
                    sys.exit()
                else:
                    print('Could not create Issue "%s"' % error)
                    print('Response:', r.content)
                    sys.exit()
            else:
                import sys
                sys.exit()
try:
    version = 5.4
    def scan(scanType, lookFor):
        timesFailed = 0
        while True:
            print(timesFailed)
            try:
                return scanType(lookFor)
            except:
                if timesFailed == 300:
                    return browser.find_element_by_tag_name('body')
                timesFailed += 1
    imported = False
    while imported == False:
        import inspect
        import sys
        import json
        import urllib
        import shutil
        import platform
        from time import sleep
        computerName = platform.node()
        if computerName == "atomicsystem.lan":
            dev = True
        else:
            dev = False
        import getpass
        import os
        def install(package):
            pip.main(['install', package])
        osis = -1
        # 0 = Mac, 1 = Windows, 2 = Linux
        directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        os.chdir(directory)
        userplatform = platform.system()
        userplatform = userplatform.upper()
        if (userplatform == "DARWIN" or userplatform == "MAC"):
            osis = 0
        if (userplatform == "WIN32" or userplatform == "WINDOWS"):
            osis = 1
        if (userplatform == "LINUX" or userplatform == "LINUX32"):
            osis = 2
        try:
            import tldextract
            import requests
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.support.ui import Select
            imported = True
        except ImportError:
            import pip
            imported = False
            userChoose = False
            while userChoose == False:
                askforinstall = input("Some packages were not found, would you like the script to install them for you (Y or N)? >>> ")
                askforinstall = askforinstall.upper()
                if askforinstall == "Y":
                    print("Installing...")
                    try:
                        from selenium.webdriver.common.keys import Keys
                    except ImportError:
                        install('selenium')
                    try:
                        import tldextract
                    except ImportError:
                        install('tldextract')
                    try:
                        import requests
                    except ImportError:
                        install('requests')
                    print("Installed!")

                    sys.exit()
                else:

                    sys.exit()

    def internet_on():
        try:
            urllib.request.urlopen('http://216.58.192.142', timeout=1)
            return True
        except:
            return False
    class Updater:
        def __init__(self):
            pass
        def checkForUpdates(self):
            titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
            pasteV = titleget.text
            pasteV = float(pasteV)
            if pasteV > version:
                fname = os.path.basename(__file__)
                reply = requests.get('https://raw.githubusercontent.com/AtomicCoding/Quizlet-Bot/master/main.py')
                code = reply.text
                with open(fname, 'r') as f1:
                    oldcode = f1.read()
                if not oldcode == code:
                    return True
                if oldcode == code:
                    return False
            else:
                return False
        def update(self):
            import codecs
            fname = os.path.basename(__file__)
            titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
            title = titleget.text
            print("Updating to V.",title+"...")
            reply = requests.get('https://raw.githubusercontent.com/AtomicCoding/Quizlet-Bot/master/main.py')
            code = reply.text
            with codecs.open(fname, "w", "utf-8-sig") as f:
                f.write(code)
            sys.exit()
    try:
        with open('issue.txt', 'r') as myfile:
            data=myfile.read().replace('\n', '')
            myfile.close()
            os.remove('issue.txt')
            issueRead = True
            complain(data)
    except:
        pass
    connectedToInternet = internet_on()
    if connectedToInternet == False:
        print("You are not connected to the internet, please connect and try again.")

        sys.exit()
    passwordChoosen = False
    restart = True
    while restart == True:
        restart = False
        loggedIn = False
        oneQuiz = False
        osSelected = False
        noJSON = False
        pageIDChoosen = False
        started = False
        timesQuizlet = "ns"
        if not os.path.exists(directory+"/"+"info.json"):
            f= open("info.json","w+")
            f.close()
            noJSON = True
        if noJSON == True:
            pageID = "ns"
            successes = 0
            failures = 0
            path = "ns"
            timesQuizlet = "ns"
            username = "ns"
            password = "ns"
            USERUSERNAME = "ns"
            USERPASSWORD = "ns"
            maxScore = "ns"
            successesG = 0
            failuresG = 0
            option = 'ns'
            diff = 'ns'
            recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "timesQuizlet": "ns", "username": "ns", "password": "ns", "USERUSERNAME": "ns", "USERPASSWORD": "ns", "maxScore": "ns", "successesG": 0, "failuresG": 0, "option": "ns", "diff": "ns"}
            with open ('info.json', 'r+') as myfile:
                recover=myfile.write(json.dumps(recover))
        try:
            with open ('info.json', 'r') as myfile:
                info=json.loads(myfile.read())
        except:
            jsonreset = input("ERROR: COULD NOT LOAD IN JSON, WOULD YOU LIKE TO TRY TO FIX THE JSON (Y or N)? >>> ")
            jsonreset = jsonreset.upper()
            if jsonreset == "Y":
                jsonfix = input("Would you like to reset the JSON or manually repair it? >>> ")
                jsonfix = jsonfix.upper()
                if jsonfix == "RESET THE JSON" or jsonfix == "RESET" or jsonfix == "RESET JSON":
                    pageID = "ns"
                    successes = 0
                    failures = 0
                    path = "ns"
                    timesQuizlet = "ns"
                    username = "ns"
                    password = "ns"
                    USERUSERNAME = "ns"
                    USERPASSWORD = "ns"
                    maxScore = "ns"
                    successesG = 0
                    failuresG = 0
                    option = 'ns'
                    diff = 'ns'
                    recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "timesQuizlet": "ns", "username": "ns", "password": "ns", "USERUSERNAME": "ns", "USERPASSWORD": "ns", "maxScore": "ns", "successesG": 0, "failuresG": 0, "option": "ns", "diff": "ns"}
                    with open ('info.json', 'r+') as myfile:
                        recover=myfile.write(json.dumps(recover))
                    sys.exit()
                else:
                    with open('info.json', 'r') as myfile:
                        data=myfile.read().replace('\n', '')
                    print("The JSON reads:", data+".")
                    pageID = input("PageID: >>> ")
                    successes = input("Successes: >>> ")
                    failures = input("Failures: >>> ")
                    path = input("Path: >>> ")
                    timesQuizlet = input("TimesQuizlet: >>> ")
                    username = input("Username: >>> ")
                    password = getpass.getpass("Password: >>> ")
                    print("If you don't see any refrences to USERUSERNAME and PASSWORD, then just type in 'ns' for all of them.")
                    USERUSERNAME = input("USERUSERNAME: >>> ")
                    USERPASSWORD = getpass.getpass("USERPASSWORD: >>> ")
                    print("If you don't see any refrences to maxScore, successesG, Option, Diff, and failuresG, then just type in 'ns' for all of them.")
                    maxScore = input("MaxScore: >>> ")
                    successesG = input("SuccessesG: >>> ")
                    failuresG = input("FailuresG: >>> ")
                    option = input("Option: >>> ")
                    diff = input("Diff: >>> ")
                    successesG = int(successesG)
                    failuresG = int(failuresG)
                    pageID = int(pageID)
                    successes = int(successes)
                    failures = int(failures)
                    try:
                        timesQuizlet = int(timesQuizlet)
                        maxScore = int(maxScore)
                        option = int(option)
                        diff = int(diff)
                    except:
                        pass
                    recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": maxScore, "successesG": successesG, "failuresG": failuresG, "option": option, "diff": diff}
                    with open ('info.json', 'r+') as myfile:
                        recover=myfile.write(json.dumps(recover))
                    sys.exit()
            else:
                sys.exit()
        if not osis == 0 and not osis == 1 and not osis == 2:
            complain("Unknown OS detected called:"+str(userplatform))
        def save(info, pageID1, successes1, failures1, path1, timesQuizlet1, username1, password1, USERUSERNAME1, USERPASSWORD1, maxScore1, successesG1, failuresG1, option1, diff1):
            info["pageID"] = pageID1
            info["successes"] = successes1
            info["failures"] = failures1
            info["path"] = path1
            info["timesQuizlet"] = timesQuizlet1
            info["username"] = username1
            info["password"] = password1
            info["USERUSERNAME"] = USERUSERNAME1
            info["USERPASSWORD"] = USERPASSWORD1
            info["maxScore"] = maxScore1
            info["successesG"] = successesG1
            info["failuresG"] = failuresG1
            info["option"] = option1
            info["diff"] = diff1
            with open('info.json', 'w+') as myfile:
                info=myfile.write(json.dumps(info))
        pageID = info["pageID"]
        successes = info["successes"]
        failures = info["failures"]
        path = info["path"]
        timesQuizlet = info["timesQuizlet"]
        username = info["username"]
        password = info["password"]
        try:
            USERUSERNAME = info["USERUSERNAME"]
            USERPASSWORD = info["USERPASSWORD"]
        except:
            recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": "ns", "USERPASSWORD": "ns", "maxScore": "ns", "successesG": 0, "failuresG": 0}
            with open ('info.json', 'r+') as myfile:
                info=myfile.write(json.dumps(recover))
            print("Updated JSON to include GitHub Integration! Please restart the script!")

            sys.exit()
        try:
            maxScore = info["maxScore"]
            successesG = info["successesG"]
            failuresG = info["failuresG"]
            option = info["option"]
            diff = info["diff"]
        except:
            recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": "ns", "successesG": 0, "failuresG": 0, "option": "ns", "diff": "ns"}
            with open ('info.json', 'r+') as myfile:
                info=myfile.write(json.dumps(recover))
            print("Updated JSON to include a Gravity Bot! Please restart the script!")

            sys.exit()
        if timesQuizlet == "nw":
            timesQuizlet = "dw"
        if username == "nw":
            username = "dw"
        if password == "nw":
            password = "dw"
        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
        checkedforchrome = False
        if not os.path.exists(path):
            path = "ns"
            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
        def reset():
            os.remove("info.json")
        if path == "ns":
            if (osis == 1):
                my_file = directory+"/"+"chromedriver.exe"
            else:
                my_file = directory+"/"+"chromedriver"
            if os.path.exists(my_file):
                path = my_file
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
        if (path == "ns"):
            while (checkedforchrome == False):
                checkedforchrome = True
                chromecheck = input('Have you installed ChromeDriver (Y or N)? >>> ')
                if (chromecheck == "y" or chromecheck == "Y"):
                    path = input("The path to chromedriver is: >>> ")
                    if not os.path.exists(path):
                        print("Invalid Path!")
                        checkedforchrome = False
                    else:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        print("Continuing...")
                if (not chromecheck == "Y" and not chromecheck == "y" and not chromecheck == "N" and not chromecheck == "n"):
                    print("Invalid Option...Restarting...")
                    checkedforchrome = False
                if (chromecheck == "n" or chromecheck == "N"):
                    chromeinstalled = input("Would you like the script to install it for you (Y or N)? >>> ")
                    if (chromeinstalled == "y" or chromeinstalled == "Y"):
                        while (osSelected == False):
                            osSelected = True
                            print("Downloading...")
                            if (userplatform == "WIN32" or userplatform == "WINDOWS"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.30/chromedriver_win32.zip"
                                file_name = "chromedriver_win32.zip"
                            if (userplatform == "DARWIN" or userplatform == "MAC"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip"
                                file_name = "chromedriver_mac64.zip"
                            if (userplatform == "LINUX"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip"
                                file_name = "chromedriver_linux64.zip"
                            if (userplatform == "LINUX32"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux32.zip"
                                file_name = "chromedriver_linux32.zip"
                            with urllib.request.urlopen(downloadurl) as response, open(file_name, 'wb') as out_file:
                                shutil.copyfileobj(response, out_file)
                            print("Downloaded! Please extract the file to the script's directory and restart the script.")

                            sys.exit()
                    if (chromeinstalled == "n" or chromeinstalled == "N"):
                            print("Goodbye!")

                            sys.exit()
        if (username == "ns" and password == "ns"):
            reply = input('Would you like to have the script enter your username and password for you (Y or N)? >>> ')
            if (reply == "n" or reply == "N"):
                username = "dw"
                password = "dw"
            if (reply == "Y" or reply == "y"):
                while passwordChoosen == False:
                    print("None of this data is transmitted, it is just saved for ease of use on your local machine.")
                    username = input("Email: >>> ")
                    password = getpass.getpass("Password: >>> ")
                    confirmpassword = getpass.getpass("Confirm Password: >>> ")
                    if confirmpassword == password:
                        print("Thank you!")
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        passwordChoosen = True
                    else:
                        print("Passwords do not match!")
                        passwordChoosen = False
        if USERUSERNAME == "ns" and USERPASSWORD == "ns":
            reply = input("Would you like the script to integrate with your GitHub account (Y or N)? >>> ")
            reply = reply.upper()
            if reply == "Y":
                while True:
                    print("None of this data is transmitted to anything other then GitHub for Issue Reporting.")
                    USERUSERNAME = input("GitHub Username: >>> ")
                    USERPASSWORD = getpass.getpass("GitHub Password: >>> ")
                    CONFIRMPASS = getpass.getpass("Confirm Password: >>> ")
                    if USERPASSWORD == CONFIRMPASS:
                        print("Thank you!")
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        break
            else:
                USERUSERNAME = "dw"
                USERPASSWORD = "dw"
        runTypeSelected = False
        while runTypeSelected == False:
            runTypeSelected = True
            update = Updater()
            updateNeeded = update.checkForUpdates()
            gitPassword = len(USERPASSWORD) * "*"
            passwordhidden = len(password) * ""
            if dev == True:
                titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
                pasteV = titleget.text
                pasteV = float(pasteV)
                if pasteV < version:
                    uploadable = True
                else:
                    uploadable = False
            else:
                uploadable = False
            if updateNeeded == True:
                if dev == False:
                    print("Type in an option: Start, Settings, Update, Quit")
                if dev == True:
                    print("Type in an option: Start, Settings, Update, Expirment, Quit")
            else:
                if dev == True:
                    if uploadable == True:
                        print("Type in an option: Start, Settings, Upload, Expirment, Quit")
                    else:
                        print("Type in an option: Start, Settings, Expirment, Quit")
                else:
                    print("Type in an option: Start, Settings, Quit")
            runTypeInput = input("I choose: >>> ")
            runTypeInput = runTypeInput.upper()
            if updateNeeded == True:
                if runTypeInput == "UPDATE":
                    update.update()
            if runTypeInput == "EXPIRMENT":
                print("Starting GUI...")
                from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
                from PyQt5.QtCore import QCoreApplication
                class Example(QWidget):

                    def __init__(self):
                        super().__init__()

                        self.initUI()


                    def initUI(self):
                        # sbtn = QPushButton('Start', self)
                        # sbtn.clicked.connect(print("Hello!"))
                        # sbtn.resize(qbtn.sizeHint())
                        # sbtn.move(75, 75)
                        qbtn = QPushButton('Quit', self)
                        qbtn.clicked.connect(QCoreApplication.instance().quit)
                        qbtn.resize(qbtn.sizeHint())
                        qbtn.move(50, 50)
                        self.setGeometry(300, 300, 250, 150)
                        self.setWindowTitle('OQBRTA')
                        self.show()
                if __name__ == '__main__':
                    app = QApplication(sys.argv)
                    ex = Example()
                    sys.exit(app.exec_())
            if uploadable == True and dev == True and runTypeInput == "UPLOAD":
                titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
                pasteV = titleget.text
                pasteV = float(pasteV)
                if pasteV < version:
                    uploadable = True
                else:
                    uploadable = False
                if uploadable == True:
                    checked = True
                    if checked == True:
                        fname = os.path.basename(__file__)
                        with open(fname, 'r') as f1:
                            updatedcode = f1.read()
                        titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
                        title = titleget.text
                        titlenumber = len(title)
                        updateName = input("What should the commit name be? >>> ")
                        chromedriver = path
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        browser = webdriver.Chrome(chromedriver)
                        browser.get("https://pastebin.com/login")
                        scan(browser.find_element_by_xpath,'//div[@onclick][3]').click()
                        scan(browser.find_element_by_xpath,"//input[@type='email']").send_keys(username+Keys.ENTER)
                        sleep(3)
                        scan(browser.find_element_by_xpath,"//input[@type='password']").send_keys(password+Keys.ENTER)
                        browser.get('https://pastebin.com/edit/hHLndhTS')
                        scan(browser.find_element_by_xpath,'//textarea').click()
                        timesRanDelete = 0
                        while not timesRanDelete == titlenumber:
                            scan(browser.find_element_by_xpath,'//textarea').send_keys(Keys.BACKSPACE)
                            timesRanDelete = timesRanDelete + 1
                        scan(browser.find_element_by_xpath,'//textarea').send_keys(str(version))
                        scan(browser.find_element_by_name,'submit').click()
                        browser.quit()
                        gitdir = directory+"/Git"
                        os.chdir(gitdir)
                        try:
                            os.remove('main.py')
                        except:
                            pass
                        src = directory+"/"+fname
                        dst = directory+"/Git/main.py"
                        shutil.copyfile(src, dst)
                        os.system("git commit main.py -m '"+updateName+"'")
                        os.system('git push')
                        os.chdir(directory)
                    else:
                        print("ERROR: Pastebin Version is Newer.")
                        runTypeSelected = False
            if runTypeInput == "START":
                if option == "ns":
                    while True:
                        optionInput = input("What game would you like the bot to complete? Gravity, Match, Gravity and Match: >>> ")
                        optionInput = optionInput.upper()
                        if optionInput == "GRAVITY":
                            option = 0
                            break
                        elif optionInput == "MATCH":
                            option = 1
                            break
                        elif optionInput == "GRAVITY AND MATCH":
                            option = 2
                            break
                        else:
                            print("Invalid Option!")
                if option == 2 or option == 0:
                    if diff == "ns":
                        while True:
                            print("Choose a difficulty for the Gravity Bot: Easy, Medium, Hard")
                            diffOption = input("I choose: >>> ")
                            diffOption = diffOption.upper()
                            if diffOption == "EASY":
                                diff = 0
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print("You have set the difficulty to easy for the Gravity Bot.")
                                break
                            elif diffOption == "MEDIUM":
                                diff = 1
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print("You have set the difficulty to medium for the Gravity Bot.")
                                break
                            elif diffOption == "HARD":
                                diff = 2
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print("You have set the difficulty to hard for the Gravity Bot.")
                                break
                    if maxScore == "ns":
                        while True:
                            maxScore = input("What should be the target score for the Gravity Bot? >>> ")
                            try:
                                maxScore = int(maxScore)
                                if maxScore < 0:
                                    maxScore = dict(maxScore)
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                break
                            except:
                                print("Enter a number please.")
                if timesQuizlet == "ns":
                    chooseRunType = input("Would you like to run the bot infinitely (Y or N)? >>> ")
                    if (chooseRunType == "y" or chooseRunType == "Y"):
                        if not timesQuizlet == "dw":
                            timesQuizlet = "dw"
                        if pageID == "ns":
                            print("https://quizlet.com/0<---PageID/micromatch")
                            while pageIDChoosen == False:
                                pageIDChoosen = True
                                pageID = input("What pageID would you like to start from? >>> ")
                                try:
                                    pageID = int(pageID)
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                except ValueError:
                                    pageIDChoosen = False
                        started = True
                        oneQuiz = False
                    if (chooseRunType == "n" or chooseRunType == "N"):
                        if timesQuizlet == "ns":
                            timesChoosen = False
                            while timesChoosen == False:
                                timesChoosen = True
                                timesQuizlet = input("How many quizes would you like to do? >>> ")
                                try:
                                    timesQuizlet = int(timesQuizlet)
                                    if not timesQuizlet < 0:
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                except ValueError:
                                    timesChoosen = False
                                if timesQuizlet < 0:
                                    timesChoosen = False
                if timesQuizlet == "dw":
                    started = True
                    oneQuiz = False
                if not timesQuizlet == "dw" and not timesQuizlet == "ns":
                    started = True
                    oneQuiz = True
                    if pageID == "ns":
                        print("https://quizlet.com/0<---PageID/micromatch")
                        pageIDChoosen = False
                        while pageIDChoosen == False:
                            pageIDChoosen = True
                            pageID = input("What pageID would you like the bot to run on? >>> ")
                            try:
                                pageID = int(pageID)
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                            except ValueError:
                                pageIDChoosen = False
                        started = True
                        oneQuiz = True
            if runTypeInput == "SETTINGS":
                doneChanging = False
                while doneChanging == False:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                    if dev == False:
                        settingsoption = input("Type an option: General, Gravity, Quit: >>> ")
                    else:
                        settingsoption = input("Type an option: General, Gravity, Dev, Quit: >>> ")
                    settingsoption = settingsoption.upper()
                    if settingsoption == "QUIT":
                        runTypeSelected = False
                        print("Leaving...")
                        break
                    if dev == True and settingsoption == "DEV":
                        while True:
                            devOption = input("Type an option: Create Issue, Print Info, Run Code, Quit: >>> ")
                            devOption = devOption.upper()
                            if devOption == "CREATE ISSUE":
                                issueName = input("What would you like to name the issue? >>> ")
                                complain(issueName)
                            elif devOption == "PRINT INFO":
                                with open('info.json', 'r') as myfile:
                                    data=myfile.read().replace('\n', '')
                                print('Info reads:', data)
                            elif devOption == "RUN CODE":
                                codeRun = input("What would you like to run? >>> ")
                                try:
                                    exec(codeRun)
                                except Exception as e:
                                    print("Welp...your code failed, this is what happened:", e)
                            elif devOption == "QUIT":
                                break
                    if settingsoption == "GRAVITY":
                        while True:
                            print("Choose an option: Target Score, Difficulty, Quit")
                            gravityOption = input("I choose: >>> ")
                            gravityOption = gravityOption.upper()
                            if gravityOption == "DIFFICULTY":
                                while True:
                                    if diff == "ns":
                                        print("You have not set the difficulty for the Gravity Bot.")
                                    else:
                                        if diff == 0:
                                            print("You have set the difficulty to easy for the Gravity Bot.")
                                        elif diff == 1:
                                            print("You have set the difficulty to medium for the Gravity Bot.")
                                        elif diff == 2:
                                            print("You have set the difficulty to hard for the Gravity Bot.")
                                        else:
                                            print("Something is corrupt! Oh no!")
                                            complain("Diff Variable is corrupt.")
                                    print("Choose a option: Easy, Medium, Hard")
                                    diffOption = input("I choose: >>> ")
                                    diffOption = diffOption.upper()
                                    if diffOption == "EASY":
                                        diff = 0
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        break
                                    elif diffOption == "MEDIUM":
                                        diff = 1
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        break
                                    elif diffOption == "HARD":
                                        diff = 2
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        break
                                    else:
                                        print("Invalid Option!")
                            if gravityOption == "TARGET SCORE":
                                if maxScore == "ns":
                                    print("You have not set the target score for the Gravity Bot.")
                                else:
                                    print("The target score for the Gravity Bot is:", str(maxScore)+".")
                                while True:
                                    maxScore = input("What should be the target score for the Gravity Bot? >>> ")
                                    try:
                                        maxScore = int(maxScore)
                                        if maxScore < 0:
                                            maxScore = dict(maxScore)
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        break
                                    except:
                                        print("Enter a number please.")
                            elif gravityOption == "QUIT":
                                break
                    if settingsoption == "GENERAL":
                        while True:
                            print("Choose an option: About, Automatic Login, GitHub Integration, PageID, Path to ChromeDriver, Bots to Run, Times to Run OQBRTA, Advanced, Quit")
                            generalChoose = input("I Choose: >>> ")
                            generalChoose = generalChoose.upper()
                            if generalChoose == "ADVANCED":
                                while True:
                                    advancedChoose = input("Choose an option: Reset, Quit: >>> ")
                                    advancedChoose = advancedChoose.upper()
                                    if advancedChoose == "RESET":
                                        usersure = input("Are you sure (Y or N)? >>> ")
                                        if (usersure == "y" or usersure == "Y"):
                                            reset()
                                            restart = True
                                    elif advancedChoose == "QUIT":
                                        break
                            if generalChoose == "ABOUT":
                                while True:
                                    aboutChoose = input("Choose an option: Version, Data, Quit: >>> ")
                                    aboutChoose = aboutChoose.upper()
                                    if aboutChoose == "QUIT":
                                        break
                                    if aboutChoose == "VERSION":
                                        if osis == 0:
                                            print("This is OQBRTA, V.", version, "and you are running MacOS.")
                                        if osis == 1:
                                            print("This is OQBRTA, V.", version, "and you are running Windows.")
                                        if osis == 2:
                                            print("This is OQBRTA, V.", version, "and you are running Linux.")
                                        if not osis == 0 and not osis == 1 and not osis == 2:
                                            print("This is OQBRTA, V.", version, "and you are running an unknown OS called:", userplatform+".")
                                    elif aboutChoose == "DATA":
                                        if pageID == "ns":
                                            print("PageID has not been set.")
                                        else:
                                            print("PageID is set to:",str(pageID))
                                        print("There have been:",str(failures),"failures.")
                                        print("There have been:",str(successes),"successes.")
                                        if path == "ns":
                                            print("The path to ChromeDriver is not set.")
                                        else:
                                            print("The path to ChromeDriver is set to:",path)
                                        if timesQuizlet == "dw":
                                            print("You have set OQBRTA to run infinitely.")
                                        if timesQuizlet == "ns":
                                            print("You have not set how many times you want OQBRTA to run.")
                                        if not timesQuizlet == "ns" and not timesQuizlet == "dw":
                                            print("You have set OQBRTA to run:", timesQuizlet, "times.")
                                        if username == "ns":
                                            print("The email is not set.")
                                        if username == "dw" and password == "dw":
                                            print("You have disabled automatic password and email entering.")
                                        if not username == "ns" and not username == "dw" and not password == "ns" and not password == "dw":
                                            print("The email is set to:",username)
                                        if not password == "ns" and not username == "dw" and not password == "dw" and not username == "ns":
                                            print("The password is:", passwordhidden)
                                            seePassword = input("Would you like to see the password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass("Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == password):
                                                    print("The password is:", password)
                                                else:
                                                    print("Incorrect!")
                                        if password == "ns":
                                            print("The password is not set.")
                                        if USERUSERNAME == "ns":
                                            print("The GitHub Username is not set.")
                                        if USERPASSWORD == "ns":
                                            print("The GitHub Password is not set.")
                                        if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                                            print("You have disabled GitHub Integration.")
                                        if not USERUSERNAME == "dw" and not USERUSERNAME == "ns":
                                            print("Your GitHub username is set to:", USERUSERNAME+".")
                                        if not USERPASSWORD == "dw" and not USERPASSWORD == "ns":
                                            print("The password is:", gitPassword)
                                            seePassword = input("Would you like to see the GitHub password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass("Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == USERPASSWORD):
                                                    print("The password is:", USERPASSWORD+".")
                                                else:
                                                    print("Incorrect!")
                                        if maxScore != "ns":
                                            print("The target score for Gravity is set to:", str(maxScore)+".")
                                        else:
                                            print("The target score for Gravity is not set.")
                                        print("There have been", str(successesG), "successes in the Gravity Bot.")
                                        print("There have been", str(failuresG), "failures in the Gravity Bot.")
                                        if diff == 0:
                                            print("You have set the difficulty to easy in the Gravity Bot.")
                                        elif diff == 1:
                                            print("You have set the difficulty to medium in the Gravity Bot.")
                                        elif diff == 2:
                                            print("You have set the difficulty to hard in the Gravity Bot.")
                                        else:
                                            complain("Diff variable is corrupt.")
                                        if option == "ns":
                                            print("You have not decided which bot(s) to run.")
                                        else:
                                            if option == 0:
                                                print("You have decided to only run the Gravity Bot.")
                                            if option == 1:
                                                print("You have decided to only run the Match Bot.")
                                            if option == 2:
                                                print("You have decided to run both the Gravity and Match Bots.")
                            elif generalChoose == "AUTOMATIC LOGIN":
                                while True:
                                    if password == "dw" and username == "dw":
                                        loginSettings = input("What would you like to do? Enable Automatic Login or Quit: >>> ")
                                    else:
                                        loginSettings = input("What would you like to do? Change Email, Change Password, Disable Automatic Login or Quit: >>> ")
                                    loginSettings = loginSettings.upper()
                                    if password == "dw" and username == "dw" and loginSettings == "ENABLE AUTOMATIC LOGIN":
                                        passwordChoosen = False
                                        while passwordChoosen == False:
                                            passwordChoosen = True
                                            print("None of this data is transmitted, it is just saved for ease of use on your local machine.")
                                            username = input("Email: >>> ")
                                            password = getpass.getpass("Password: >>> ")
                                            confirmpassword = getpass.getpass("Confirm Password: >>> ")
                                            if confirmpassword == password:
                                                print("Thank you!")
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                            else:
                                                print("Passwords do not match!")
                                                passwordChoosen = True
                                    if not password == "dw" and not username == "dw":
                                        if loginSettings == "DISABLE AUTOMATIC LOGIN":
                                            username = "dw"
                                            password = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        if loginSettings == "CHANGE PASSWORD":
                                            passwordVerified = False
                                            while passwordVerified == False:
                                                passwordVerified = True
                                                print("The password currently is:", passwordhidden)
                                                verifypassword = getpass.getpass("Please enter your password to continue: >>> ")
                                                if verifypassword == password:
                                                    print("Correct!")
                                                    seePassword = input("Would you like to see the password (Y or N)? >>> ")
                                                    seePassword = seePassword.upper()
                                                    if seePassword == "Y":
                                                        print("The password currently is:", password)
                                                    else:
                                                        print("The password currently is:", passwordhidden)
                                                    passwordChanged = False
                                                    while passwordChanged == False:
                                                        password = getpass.getpass("I would like to change my password to: >>> ")
                                                        confirmpassword = getpass.getpass("Confirm: >>> ")
                                                        if confirmpassword == password:
                                                            print("Changed!")
                                                            passwordChanged = True
                                                        else:
                                                            print("Passwords do not match!")
                                                else:
                                                    passwordVerified = True
                                                    print("Invalid Password!")
                                        if loginSettings == "CHANGE EMAIL":
                                            if username == "ns":
                                                print("The email has not been set.")
                                            if not username == "ns" and not username == "dw":
                                                print("The email is set to:", username)
                                            if not username == "dw":
                                                username = input("I would like to set the email to: >>> ")
                                    if loginSettings == "QUIT":
                                        break
                            elif generalChoose == "GITHUB INTEGRATION":
                                while True:
                                    if USERUSERNAME == "dw" and USERUSERNAME == "dw":
                                        gitSettings = input("What would you like to do? Enable GitHub Integration, Quit: >>> ")
                                        disabled = True
                                    else:
                                        gitSettings = input("What would you like to do? Change Username, Change Password, Disable GitHub Integration, Quit: >>> ")
                                        disabled = False
                                    gitSettings = gitSettings.upper()
                                    if gitSettings == "ENABLE GITHUB INTEGRATION" and disabled == True:
                                        while True:
                                            print("None of this data is transmitted to anything other then GitHub for Issue Reporting.")
                                            USERUSERNAME = input("GitHub Username: >>> ")
                                            USERPASSWORD = getpass.getpass("GitHub Password: >>> ")
                                            CONFIRMPASS = getpass.getpass("Confirm Password: >>> ")
                                            if USERPASSWORD == CONFIRMPASS:
                                                print("Thank you!")
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                                break
                                    if disabled == False:
                                        if gitSettings == "CHANGE USERNAME":
                                            print("The GitHub Username is currently set to:", USERUSERNAME+".")
                                            USERUSERNAME = input("I would like to change the GitHub Username to: >>> ")
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        if gitSettings == "CHANGE PASSWORD":
                                            print("The GitHub password is set to:", gitPassword+".")
                                            passwordProtect = getpass.getpass("Enter your GitHub Password First: >>> ")
                                            if passwordProtect == USERPASSWORD:
                                                showPass = input("Would you like to see the GitHub password (Y or N)? >>> ")
                                                showPass = showPass.upper()
                                                if showPass == "Y":
                                                    if passwordProtect == USERPASSWORD:
                                                        print("The GitHub password is set to:", USERPASSWORD+".")
                                                while True:
                                                    USERPASSWORD = getpass.getpass("GitHub Password: >>> ")
                                                    CONFIRMPASS = getpass.getpass("Confirm Password: >>> ")
                                                    if USERPASSWORD == CONFIRMPASS:
                                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                                        break
                                            else:
                                                print("Incorrect Password!")
                                        if gitSettings == "DISABLE GITHUB INTEGRATION":
                                            USERUSERNAME = "dw"
                                            USERPASSWORD = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                            disabled = True
                                    if gitSettings == "QUIT":
                                        break
                            elif generalChoose == "PAGEID":
                                if pageID == "ns":
                                    print("PageID has not been set.")
                                else:
                                    print("PageID is set to:", pageID)
                                pageIDChoosen = False
                                while pageIDChoosen == False:
                                    pageIDChoosen = True
                                    pageID = input("What would you like to set the pageID to? >>> ")
                                    try:
                                        pageID = int(pageID)
                                        if pageID < 0:
                                            pageID = dict(pageID)
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    except ValueError:
                                        pageIDChoosen = False
                            elif generalChoose == "PATH TO CHROMEDRIVER":
                                if path == "ns":
                                    print("The path to ChromeDriver has not been set.")
                                else:
                                    print("The path to ChromeDriver is set to:", path)
                                    checkedforchrome = False
                                    while (checkedforchrome == False):
                                            checkedforchrome = True
                                            path = input("I would like to set the path to ChromeDriver to: >>> ")
                                            if not os.path.exists(path):
                                                print("Invalid Path!")
                                                checkedforchrome = False
                            elif generalChoose == "BOTS TO RUN":
                                while True:
                                    if option == 0:
                                        print("You have decided to only run the Gravity Bot.")
                                    if option == 1:
                                        print("You have decided to only run the Match Bot.")
                                    if option == 2:
                                        print("You have decided to run both the Gravity and Match Bots.")
                                    optionInput = input("Choose a bot: Gravity, Match, Gravity and Match: >>> ")
                                    optionInput = optionInput.upper()
                                    if optionInput == "GRAVITY":
                                        option = 0
                                        break
                                    elif optionInput == "MATCH":
                                        option = 1
                                        break
                                    elif optionInput == "GRAVITY AND MATCH":
                                        option = 2
                                        break
                                    else:
                                        print("Invalid Option!")
                            elif generalChoose == "TIMES TO RUN OQBRTA":
                                while True:
                                    if timesQuizlet == "dw":
                                        print("You have decided to run OQBRTA infinitely.")
                                    if not timesQuizlet == "dw" and not timesQuizlet == "ns":
                                        print("You have decided to run OQBRTA", timesQuizlet, "times.")
                                    if timesQuizlet == "ns":
                                        print("You have not set the amount of times you would like to run OQBRTA.")
                                    timesQuizletSettings = input("What would you like to do? Run OQBRTA infinitely, Run OQBRTA a specific amount of times or Quit: >>> ")
                                    timesQuizletSettings = timesQuizletSettings.upper()
                                    if timesQuizletSettings == "RUN OQBRTA INFINITELY" or timesQuizletSettings == "RUN INFINITELY" or timesQuizletSettings == "INFINITELY":
                                        if not timesQuizlet == "dw":
                                            timesQuizlet = "dw"
                                    elif timesQuizletSettings == "RUN OQBRTA A SPECIFIC AMOUNT OF TIMES" or timesQuizletSettings == "SPECIFIC AMOUNT" or timesQuizletSettings == "SPECIFIC":
                                        timesChoosen = False
                                        while timesChoosen == False:
                                            timesChoosen = True
                                            timesQuizlet = input("How many quizes would you like to do? >>> ")
                                            try:
                                                timesQuizlet = int(timesQuizlet)
                                                if not timesQuizlet < 0:
                                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                            except ValueError:
                                                timesChoosen = False
                                            if timesQuizlet < 0:
                                                timesChoosen = False
                                    elif timesQuizletSettings == "QUIT" or timesQuizletSettings == "EXIT":
                                        break
                                    else:
                                        print("Invalid Option!")
                            elif generalChoose == "QUIT":
                                break
            if runTypeInput == "QUIT":
                print("Goodbye!")
                sys.exit()
            if updateNeeded == True:
                if not runTypeInput == "UPDATE" and not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
            else:
                if not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
        if started == True:
            problem = False
            chromedriver = path
            os.environ["webdriver.chrome.driver"] = chromedriver
            browser = webdriver.Chrome(chromedriver)
            browser.set_window_size(1600, 1000)
            if oneQuiz == False:
                while True:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        restart = True
                        break
                    else:
                        extracted = False
                        if option == 2 or option == 0:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                button = scan(browser.find_element_by_xpath, '//div[@class="ModeControls-back"]/a')
                                button.click()
                                failed = False
                            except:
                                failuresG = failuresG + 1
                                failed = True
                            if failed == False:
                                try:

                                    elements1 = scan(browser.find_elements_by_class_name,"SetPageTerm-content")
                                    ans = []
                                    rep = []
                                    for element in elements1:
                                        pair = scan(element.find_elements_by_tag_name,'span')
                                        ans.append(pair[0].text)
                                        rep.append(pair[1].text)
                                    extracted = True
                                    if not loggedIn:
                                        scan(browser.find_element_by_xpath,'//button[1]/span').click()


                                        scan(browser.find_element_by_xpath,'//div[@class="UIRow"][1]/div/a').click()

                                        if not username == "dw" and not password == "dw":
                                            scan(browser.find_element_by_xpath,"//input[@type='email']").send_keys(username+Keys.ENTER)


                                            scan(browser.find_element_by_xpath,"//input[@type='password']").send_keys(password+Keys.ENTER)


                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print("You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/gravity")

                                    scan(browser.find_element_by_xpath,"//div[@class='GravitySplashView']/button").click()


                                    if diff == 0:
                                        scan(browser.find_element_by_xpath,'//input[@value="BEGINNER"]').click()

                                    if diff == 1:
                                        scan(browser.find_element_by_xpath,'//input[@value="INTERMEDIATE"]').click()

                                    if diff == 2:
                                        scan(browser.find_element_by_xpath,'//input[@value="EXPERT"]')

                                    try:
                                        select = Select(browser.find_element_by_xpath('//select[@class="UIDropdown-select"]'))
                                    except:
                                        pass
                                    failedDropDown = 0
                                    try:
                                        select.select_by_visible_text('Definition')
                                    except:
                                        failedDropDown = failedDropDown + 1
                                    if failedDropDown == 2:
                                        complain("An error occured clicking on the dropdown, this is the element's data: "+str(select))
                                    scan(browser.find_element_by_xpath,"//div[@class='GravityOptionsView-nextButtonWrapper']/button").click()


                                    scan(browser.find_element_by_xpath,"//div[@class='GravityDirectionsView-startButton']/button").click()

                                except:
                                    pass
                                score = -1
                                while maxScore > score:
                                    try:
                                        checkBrowser = browser.current_url
                                        chromeOpen = True
                                    except:
                                        chromeOpen = False
                                    if chromeOpen == False:
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        restart = True
                                        break
                                    # try:
                                    getScore = scan(browser.find_element_by_xpath,'html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                    while not found:
                                        try:
                                            asteroid = scan(browser.find_element_by_class_name,"GravityTerm-content")
                                            found = True
                                        except:
                                            found = False
                                    answer = ''
                                    while True:
                                        try:
                                            asteroidText = scan(asteroid.find_element_by_xpath,"//span[@class='TermText notranslate lang-en']")
                                        except:
                                            print("The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
                                            problem = True
                                            break
                                        if asteroidText != '':
                                            break
                                    if problem == True:
                                        break
                                    if asteroidText in ans:
                                        index = ans.index(asteroidText)
                                        answer = rep[index]
                                    elif asteroidText in rep:
                                        index = rep.index(asteroidText)
                                        answer = ans[index]
                                    scan(browser.find_element_by_xpath,"//div[@class='GravityTypingPrompt-inputWrapper']/textarea").send_keys(answer+Keys.ENTER)

                                    # except:
                                    #     print("The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
                                    #     break
                                if restart == True:
                                    break
                                if maxScore <= score:
                                    failed = False
                                    successesG = successesG + 1
                        if option == 2 or option == 1:
                            try:
                                if option == 1:
                                    if not loggedIn:
                                        browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                        scan(browser.find_element_by_xpath,'//div[@class="SiteHeader-signIn"]/button[2]').click()


                                        scan(browser.find_element_by_xpath,'//a[@class="UIButton UIButton--social UIButton--fill"]').click()


                                        if not username == "dw" and not password == "dw":
                                            print("Entering Email...")
                                            scan(browser.find_element_by_xpath,"//input[@type='email']").send_keys(username+Keys.ENTER)
                                            sleep(3)
                                            scan(browser.find_element_by_xpath,"//input[@type='password']").send_keys(password+Keys.ENTER)
                                            sleep(2)
                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print("You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                    try:
                                        scan(browser.find_element_by_xpath,'//span[@class="ModeControls-backText"]/span').click()

                                        failed = False
                                    except:
                                        failed = True
                                    if failed == False:

                                        elements1 = scan(browser.find_elements_by_class_name,"SetPageTerm-content")
                                        ans = []
                                        rep = []
                                        for element in elements1:
                                            pair = scan(element.find_elements_by_tag_name,'span')
                                            ans.append(pair[0].text)
                                            rep.append(pair[1].text)
                                        failed = False
                                if failed == True:
                                    failures = failures + 1
                                if failed == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                    scan(browser.find_element_by_xpath,"//div[@class='MatchModeInstructionsModal-button']").click()

                                    tiles = scan(browser.find_elements_by_xpath,"//div[@class='MatchModeQuestionGridTile']")

                                    tileNumber = 0
                                    while len(tiles) > 0:
                                        currentTerm = tiles[0].text
                                        tiles[0].click()
                                        if currentTerm in ans:
                                            index = ans.index(currentTerm)
                                            myPairText = rep[index]
                                            pairIndex = 1
                                            while pairIndex < len(tiles):
                                                if tiles[pairIndex].text == myPairText:
                                                    tiles[pairIndex].click()
                                                    tiles.pop(pairIndex)
                                                    break
                                                pairIndex += 1
                                        if currentTerm in rep:
                                            index = rep.index(currentTerm)
                                            myPairText = ans[index]
                                            pairIndex = 1
                                            while pairIndex < len(tiles):
                                                if tiles[pairIndex].text == myPairText:
                                                    tiles[pairIndex].click()
                                                    tiles.pop(pairIndex)
                                                    break
                                                pairIndex += 1
                                        tiles.pop(0)

                                    successes = successes + 1
                            except:
                                failures = failures + 1
                        pageID = pageID + 1
                        extracted = False
            if oneQuiz == True:
                timesRan = 0
                while not timesRan == timesQuizlet:
                    if not timesQuizlet == 1:
                        if not timesRan == 0:
                            pageID = pageID + 1
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        restart = True
                        break
                    else:
                        extracted = False
                        if option == 2 or option == 0:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                scan(browser.find_element_by_xpath,'//div[@class="ModeControls-back"]/a').click()

                                failed = False
                            except:
                                failuresG = failuresG + 1
                                failed = True
                            if failed == False:
                                try:

                                    elements1 = scan(browser.find_elements_by_class_name,"SetPageTerm-content")
                                    ans = []
                                    rep = []
                                    for element in elements1:
                                        pair = scan(element.find_elements_by_tag_name,'span')
                                        ans.append(pair[0].text)
                                        rep.append(pair[1].text)
                                    extracted = True
                                    if not loggedIn:
                                        scan(browser.find_element_by_xpath,'//button[1]/span').click()


                                        scan(browser.find_element_by_xpath,'//div[@class="UIRow"][1]/div/a').click()

                                        if not username == "dw" and not password == "dw":
                                            scan(browser.find_element_by_xpath,"//input[@type='email']").send_keys(username+Keys.ENTER)
                                            sleep(3)
                                            scan(browser.find_element_by_xpath,"//input[@type='password']").send_keys(password+Keys.ENTER)


                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print("You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/gravity")

                                    scan(browser.find_element_by_xpath,"//div[@class='GravitySplashView']/button").click()


                                    if diff == 0:
                                        scan(browser.find_element_by_xpath,'//input[@value="BEGINNER"]').click()

                                    if diff == 1:
                                        scan(browser.find_element_by_xpath,'//input[@value="INTERMEDIATE"]').click()

                                    if diff == 2:
                                        scan(browser.find_element_by_xpath,'//input[@value="EXPERT"]')

                                    try:
                                        select = Select(browser.find_element_by_xpath('//select[@class="UIDropdown-select"]'))
                                    except:
                                        pass
                                    failedDropDown = 0
                                    try:
                                        select.select_by_visible_text('Definition')
                                    except:
                                        failedDropDown = failedDropDown + 1
                                    if failedDropDown == 2:
                                        complain("An error occured clicking on the dropdown, this is the element's data: "+str(select))
                                    scan(browser.find_element_by_xpath,"//div[@class='GravityOptionsView-nextButtonWrapper']/button").click()


                                    scan(browser.find_element_by_xpath,"//div[@class='GravityDirectionsView-startButton']/button").click()


                                except:
                                    pass
                                score = -1
                                while maxScore > score:
                                    try:
                                        checkBrowser = browser.current_url
                                        chromeOpen = True
                                    except:
                                        chromeOpen = False
                                    if chromeOpen == False:
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        restart = True
                                        break
                                    # try:
                                    getScore = scan(browser.find_element_by_xpath,'html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                    while not found:
                                        try:
                                            asteroid = scan(browser.find_element_by_class_name,"GravityTerm-content")
                                            found = True
                                        except:
                                            found = False
                                    answer = ''
                                    while True:
                                        try:
                                            asteroidText = scan(asteroid.find_element_by_xpath,"//span[@class='TermText notranslate lang-en']")
                                        except:
                                            print("The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
                                            problem = True
                                            break
                                        if asteroidText != '':
                                            break
                                    if problem == True:
                                        break
                                    if asteroidText in ans:
                                        index = ans.index(asteroidText)
                                        answer = rep[index]
                                    elif asteroidText in rep:
                                        index = rep.index(asteroidText)
                                        answer = ans[index]
                                    scan(browser.find_element_by_xpath,"//div[@class='GravityTypingPrompt-inputWrapper']/textarea").send_keys(answer+Keys.ENTER)
                                    # except:
                                    #     print("The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
                                    #     break
                                if restart == True:
                                    break
                                if maxScore <= score:
                                    failed = False
                                    successesG = successesG + 1
                        if option == 2 or option == 1:
                            try:
                                if option == 1:
                                    if not loggedIn:
                                        browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                        scan(browser.find_element_by_xpath,'//div[@class="SiteHeader-signIn"]/button[2]').click()

                                        scan(browser.find_element_by_xpath,'//a[@class="UIButton UIButton--social UIButton--fill"]').click()

                                        if not username == "dw" and not password == "dw":
                                            scan(browser.find_element_by_xpath,"//input[@type='email']").send_keys(username+Keys.ENTER)
                                            sleep(3)
                                            scan(browser.find_element_by_xpath,"//input[@type='password']").send_keys(password+Keys.ENTER)
                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print("You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True

                                    browser.get("https://quizlet.com/"+str(pageID)+"/learn")

                                    try:
                                        scan(browser.find_element_by_xpath,'//span[@class="ModeControls-backText"]/span').click()
                                        failed = False
                                    except:
                                        failed = True
                                    if failed == False:
                                        elements1 = scan(browser.find_elements_by_class_name,"SetPageTerm-content")
                                        ans = []
                                        rep = []
                                        for element in elements1:
                                            pair = scan(element.find_elements_by_tag_name,'span')
                                            ans.append(pair[0].text)
                                            rep.append(pair[1].text)
                                        failed = False
                                if failed == True:
                                    failures = failures + 1
                                if failed == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                    scan(browser.find_element_by_xpath,"//div[@class='MatchModeInstructionsModal-button']").click()

                                    tiles = scan(browser.find_elements_by_xpath,"//div[@class='MatchModeQuestionGridTile']")

                                    tileNumber = 0
                                    while len(tiles) > 0:
                                        currentTerm = tiles[0].text
                                        tiles[0].click()
                                        if currentTerm in ans:
                                            index = ans.index(currentTerm)
                                            myPairText = rep[index]
                                            pairIndex = 1
                                            while pairIndex < len(tiles):
                                                if tiles[pairIndex].text == myPairText:
                                                    tiles[pairIndex].click()
                                                    tiles.pop(pairIndex)
                                                    break
                                                pairIndex += 1
                                        if currentTerm in rep:
                                            index = rep.index(currentTerm)
                                            myPairText = ans[index]
                                            pairIndex = 1
                                            while pairIndex < len(tiles):
                                                if tiles[pairIndex].text == myPairText:
                                                    tiles[pairIndex].click()
                                                    tiles.pop(pairIndex)
                                                    break
                                                pairIndex += 1
                                        tiles.pop(0)

                                    successes = successes + 1
                            except:
                                failures = failures + 1
                        extracted = False
                        timesRan = timesRan + 1
                        if not timesRan == timesQuizlet:
                            pageID = pageID + 1
                    if timesRan == timesQuizlet:
                        print("Complete.")
                        browser.quit()
                        restart = True
except Exception as e:
        import sys, os
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        e = str(e)
        linenumber = str(exc_tb.tb_lineno)
        ex = e+" on line: "+linenumber+" on V. "+str(version)
        complain(str(ex))
