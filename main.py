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
    from time import sleep
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
        sleep(1)
        sys.exit()
    else:
        import json
        with open ('info.json', 'r') as myfile:
            info=json.loads(myfile.read())
        USERUSERNAME = info["USERUSERNAME"]
        USERPASSWORD = info["USERPASSWORD"]
        if issueRead == False:
            print("Oh No! An error occured:", error+".")
        if issueRead == True:
            print("An archived error was found:", error+".")
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
            from time import sleep
            from sys import exit
            sleep(1)
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
                    print("None of this data is transmitted to anywhere other then GitHub for Issue Reporting.")
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
                    sleep(1)
                    sys.exit()
                else:
                    print('Could not create Issue "%s"' % error)
                    print('Response:', r.content)
                    sleep(1)
                    sys.exit()
            else:
                from time import sleep
                import sys
                sleep(1)
                sys.exit()
try:
    version = 6.04
    imported = False
    while imported == False:
        import inspect
        from time import sleep
        import sys
        import json
        import urllib
        import re
        import shutil
        import platform
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
            from pick import pick
            imported = True
        except:
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
                    try:
                        from pick import pick
                    except:
                        install('pick')
                    print("Installed!")
                    if osis == 2:
                        while True:
                            errors = input("Was there any red text or errors above? (Y or N) >>> ") 
                            errors = errors.upper()
                            if errors == "Y":
                                print("Running install commands as sudo...")
                                os.system("sudo pip install tldextract requests selenium pick")
                                os.system("sudo pip3 install tldextract requests selenium pick")
                                print("If there were two sets of errors above, something is wrong with your python enviroment. Otherwise, re-run the script.")    
                                break
                            elif errors == "N":
                                break
                    sleep(1)
                    sys.exit()
                else:
                    sleep(1)
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
        sleep(1)
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
           match = False
           gravity = False
           learn = False
           flashcards = False
           write = False
           spell = False
           test = False
           diff = 'ns'
           recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": maxScore, "successesG": successesG, "failuresG": failuresG, "match": match, "gravity": gravity, "learn": learn, "flashcards": flashcards, "write": write, "spell": spell, "test": test, "diff": diff}
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
                    match = False
                    gravity = False
                    learn = False
                    flashcards = False
                    write = False
                    spell = False
                    test = False
                    diff = 'ns'
                    recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": maxScore, "successesG": successesG, "failuresG": failuresG, "match": match, "gravity": gravity, "learn": learn, "flashcards": flashcards, "write": write, "spell": spell, "test": test, "diff": diff}
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
                    diff = input("Diff: >>> ")
                    match = input("Match: >>> ")
                    gravity = input("Gravity: >>> ")
                    learn = input("Learn: >>> ")
                    flashcards = input("Flashcards: >>> ")
                    write = input("Write: >>> ")
                    spell = input("Spell: >>> ")
                    test = input("Test: >>> ")
                    successesG = int(successesG)
                    failuresG = int(failuresG)
                    pageID = int(pageID)
                    successes = int(successes)
                    failures = int(failures)
                    try:
                        timesQuizlet = int(timesQuizlet)
                        maxScore = int(maxScore)
                        diff = int(diff)
                        match = bool(match)
                        gravity = bool(gravity)
                        learn = bool(learn)
                        flashcards = bool(flashcards)
                        write = bool(write)
                        test = bool(test)
                    except:
                        pass
                    recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": maxScore, "successesG": successesG, "failuresG": failuresG, "match": match, "gravity": gravity, "learn": learn, "flashcards": flashcards, "write": write, "spell": spell, "test": test, "diff": diff}
                    with open ('info.json', 'r+') as myfile:
                        recover=myfile.write(json.dumps(recover))
                    sys.exit()
            else:
                sys.exit()
        if not osis == 0 and not osis == 1 and not osis == 2:
            complain("Unknown OS detected called:"+str(userplatform))
        def save(info, pageID1, successes1, failures1, path1, timesQuizlet1, username1, password1, USERUSERNAME1, USERPASSWORD1, maxScore1, successesG1, failuresG1, match1, gravity1, learn1, flashcards1, write1, spell1, test1, diff1):
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
            info["match"] = match1
            info["gravity"] = gravity1
            info["learn"] = learn1
            info["flashcards"] = flashcards1
            info["write"] = write1
            info["spell"] = spell1
            info["test"] = test1
            info["diff"] = diff1
            with open('info.json', 'w+') as myfile:
                info=myfile.write(json.dumps(info))
        exit = False
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
            exit = True
        try:
            maxScore = info["maxScore"]
            successesG = info["successesG"]
            failuresG = info["failuresG"]
            diff = info["diff"]
        except:
            recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": "ns", "successesG": 0, "failuresG": 0, "option": "ns", "diff": "ns"}
            with open ('info.json', 'r+') as myfile:
                info=myfile.write(json.dumps(recover))
            print("Updated JSON to include a Gravity Bot! Please restart the script!")
            exit = True
        try:
            match = info["match"]
            gravity = info["gravity"]
            learn = info["learn"]
            flashcards = info["flashcards"]
            write = info["write"]
            spell = info["spell"]
            test = info["test"]
        except:
            recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password, "USERUSERNAME": USERUSERNAME, "USERPASSWORD": USERPASSWORD, "maxScore": maxScore, "successesG": successesG, "failuresG": failuresG, "match": False, "gravity": False, "learn": False, "flashcards": False, "write": False, "spell": False, "test": False, "diff": diff}
            with open ('info.json', 'r+') as myfile:
                info=myfile.write(json.dumps(recover))
            print("Updated JSON to include a Gravity Bot! Please restart the script!")
            exit = True
        if exit:
            sleep(1)
            sys.exit()
        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
        checkedforchrome = False
        if not os.path.exists(path):
            path = "ns"
            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
        def reset():
            os.remove("info.json")
        if path == "ns":
            if (osis == 1):
                my_file = directory+"/"+"chromedriver.exe"
            else:
                my_file = directory+"/"+"chromedriver"
            if os.path.exists(my_file):
                path = my_file
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
        if (path == "ns"):
            while (checkedforchrome == False):
                checkedforchrome = True
                chromecheck = input('Have you installed ChromeDriver (Y or N)? >>> ')
                if (chromecheck == "y" or chromecheck == "Y"):
                    path = input("The path to chromedriver is: >>> ")
                    if not os.path.exists(path):
                        print("Invalid Path.")
                        checkedforchrome = False
                    else:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                        print("Continuing...")
                if (not chromecheck == "Y" and not chromecheck == "y" and not chromecheck == "N" and not chromecheck == "n"):
                    print("Invalid Option...Restarting...")
                    checkedforchrome = False
                if (chromecheck == "n" or chromecheck == "N"):
                    chromeinstalled = input("Would you like the script to install it for you (Y or N)? >>> ")
                    if (chromeinstalled == "y" or chromeinstalled == "Y"):
                        while (osSelected == False):
                            from zipfile import ZipFile, ZipInfo
                            class Zip(ZipFile):
                                def extract(self, member, path=None, pwd=None):
                                    if not isinstance(member, ZipInfo):
                                        member = self.getinfo(member)

                                    if path is None:
                                        path = os.getcwd()

                                    ret_val = self._extract_member(member, path, pwd)
                                    attr = member.external_attr >> 16
                                    os.chmod(ret_val, attr)

                                    return ret_val
                            osSelected = True
                            from lxml import etree
                            import urllib.request as request
                            tree = etree.parse(request.urlopen("https://sites.google.com/a/chromium.org/chromedriver/downloads", timeout=1), etree.HTMLParser())
                            download = tree.xpath("((//b)/a)[1]")
                            download = str(download[0].text)
                            versionnumber = re.findall("\d+\.\d+", download)
                            print("Downloading...")
                            if (userplatform == "WIN32" or userplatform == "WINDOWS"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/"+str(versionnumber[0])+"/chromedriver_win32.zip"
                                file_name = "chromedriver_win32.zip"
                            if (userplatform == "DARWIN" or userplatform == "MAC"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/"+str(versionnumber[0])+"/chromedriver_mac64.zip"
                                file_name = "chromedriver_mac64.zip"
                            if (userplatform == "LINUX"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/"+str(versionnumber[0])+"/chromedriver_linux64.zip"
                                file_name = "chromedriver_linux64.zip"
                            if (userplatform == "LINUX32"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/"+str(versionnumber[0])+"/chromedriver_linux32.zip"
                                file_name = "chromedriver_linux32.zip"
                            with urllib.request.urlopen(downloadurl) as response, open(file_name, 'wb') as out_file:
                                shutil.copyfileobj(response, out_file)
                            if not osis == 1:
                                with Zip(file_name) as file:
                                    file.extract('chromedriver')
                            if osis == 1:
                                print("Downloaded! Please extract the file to the script's directory and restart the script.")
                            else:
                                print("Downloaded and Installed! Restart the script!")
                            sleep(1)
                            sys.exit()
                    if (chromeinstalled == "n" or chromeinstalled == "N"):
                            print("Goodbye!")
                            sleep(1)
                            sys.exit()
        if (username == "ns" and password == "ns"):
            reply = input('Would you like OQBRTA to login for you (Y or N)? >>> ')
            if (reply == "n" or reply == "N"):
                reply = input("Would you like to log in manually (Y or N)? >>> ")
                if reply == "n" or reply == "N":
                    username = "nw"
                    password = "nw"
                if reply == "y" or reply == "Y":
                    username = "dw"
                    password = "dw"
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
            elif (reply == "Y" or reply == "y"):
                while passwordChoosen == False:
                    print("All the info you type in will be only stored on this machine and typed into the login screen.")
                    print("Please make sure that your quizlet account is linked to the Google Account you enter.")
                    username = input("Google Account Email: >>> ")
                    password = getpass.getpass("Google Account Password: >>> ")
                    confirmpassword = getpass.getpass("Confirm Password: >>> ")
                    if confirmpassword == password:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                        passwordChoosen = True
                    else:
                        print("Passwords do not match!")
                        passwordChoosen = False
        if USERUSERNAME == "ns" and USERPASSWORD == "ns":
            reply = input("Would you like the script to integrate with your GitHub account (Y or N)? >>> ")
            reply = reply.upper()
            if reply == "Y":
                while True:
                    print("None of this data is transmitted to anywhere other then GitHub for Issue Reporting.")
                    USERUSERNAME = input("GitHub Username: >>> ")
                    USERPASSWORD = getpass.getpass("GitHub Password: >>> ")
                    CONFIRMPASS = getpass.getpass("Confirm Password: >>> ")
                    if USERPASSWORD == CONFIRMPASS:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                        break
            elif reply == "N":
                USERUSERNAME = "dw"
                USERPASSWORD = "dw"
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
        runTypeSelected = False
        while runTypeSelected == False:
            runTypeSelected = True
            update = Updater()
            updateNeeded = update.checkForUpdates()
            gitPassword = len(USERPASSWORD) * "*"
            passwordhidden = len(password) * "*"
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
                    print("Type in an option: "+"Start, Settings, Help, Update, Quit")
                if dev == True:
                    print("Type in an option: "+"Start, Settings, Help, Update, Expirment, Quit")
            else:
                if dev == True:
                    if uploadable == True:
                        print("Type in an option: "+"Start, Settings, Help, Upload, Expirment, Quit")
                    else:
                        print("Type in an option: "+"Start, Settings, Help, Expirment, Quit")
                else:
                    print("Type in an option:"+" Start, Settings, Help, Quit")
            runTypeInput = input("I choose: >>> ")
            runTypeInput = runTypeInput.upper()
            if updateNeeded == True:
                if runTypeInput == "UPDATE":
                    update.update()
            if runTypeInput == "HELP":
                print("Welcome to the help menu!")
                while True:
                    helpInput = input("Choose an option: pageID, How to Quit when Running, Quit: >>> ")
                    helpInput = helpInput.upper()
                    if helpInput == "HOW TO QUIT WHEN RUNNING":
                        print("In order to quit the bot while it is running, simply close the open chrome window.")
                    if helpInput == "PAGEID":
                        print("The page ID is a number contained in the URL of a quizlet set. It tells the bot what quizlet set to go to. "+"Example:"+"https://quizlet.com/"+"5000321"+"<--PAGEID"+"/cool-flash-cards/.") 
                    elif helpInput == "QUIT":
                        break
            if runTypeInput == "EXPIRMENT":
                print("Starting GUI...")
                from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
                from PyQt5.QtCore import QCoreApplication
                class Example(QWidget):
                    def __init__(self):
                        super().__init__()

                        self.initUI()
                    def initUI(self):
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
                    print("Development Version is not higher than current release.")
                    uploadable = False
                codeGood = os.system('pyflakes main.py')
                if codeGood == 0 and uploadable:
                    uploadable = True
                else:
                    print("Pyflakes returned an error!")
                    uploadable = False
                if uploadable == True:
                    print("Code checks complete! All code seems good!")
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
                    sleep(1)
                    browser.find_element_by_xpath('//div[@onclick][3]').click()
                    sleep(1)
                    browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
                    sleep(1.5)
                    browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
                    sleep(1)
                    browser.get('https://pastebin.com/edit/hHLndhTS')
                    sleep(1)
                    browser.find_element_by_xpath('//textarea').click()
                    sleep(1)
                    timesRanDelete = 0
                    while not timesRanDelete == titlenumber:
                        browser.find_element_by_xpath('//textarea').send_keys(Keys.BACKSPACE)
                        timesRanDelete = timesRanDelete + 1
                    sleep(1)
                    browser.find_element_by_xpath('//textarea').send_keys(str(version))
                    sleep(1)
                    browser.find_element_by_name('submit').click()
                    sleep(1)
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
            if runTypeInput == "START":
                if match == False and gravity == False and learn == False and flashcards == False and write == False and spell == False and test == False:
                   title = 'Choose bots to run (press SPACE to mark and ENTER to continue):'
                   options = ['Match', 'Gravity', 'Learn', 'Flashcards', 'Write', 'Spell', 'Test']
                   selected = pick(options, title, multi_select=True, min_selection_count=1)
                   if "Match" in str(selected):
                      match = True
                   else:
                       match = False
                   if "Gravity" in str(selected):
                      gravity = True
                   else:
                       gravity = False
                   if "Learn" in str(selected):
                      learn = True
                   else:
                       learn = False
                   if "Flashcards" in str(selected):
                      flashcards = True
                   else:
                       flashcards = False
                   if "Write" in str(selected):
                      write = True
                   else:
                       write = False
                   if "Spell" in str(selected):
                      spell = True
                   else:
                       spell = False
                   if "Test" in str(selected):
                       test = True
                   else:
                       test = False
                if gravity == True:
                    if diff == "ns":
                        while True:
                            print("Choose a difficulty for the Gravity Bot: Easy, Medium, Hard")
                            diffOption = input("I choose: >>> ")
                            diffOption = diffOption.upper()
                            if diffOption == "EASY":
                                diff = 0
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                print("You have set the difficulty to easy for the Gravity Bot.")
                                break
                            elif diffOption == "MEDIUM":
                                diff = 1
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                print("You have set the difficulty to medium for the Gravity Bot.")
                                break
                            elif diffOption == "HARD":
                                diff = 2
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                print("You have set the difficulty to hard for the Gravity Bot.")
                                break
                    if maxScore == "ns":
                        while True:
                            maxScore = input("What should be the target score for the Gravity Bot? >>> ")
                            try:
                                maxScore = int(maxScore)
                                if maxScore < 0:
                                    maxScore = dict(maxScore)
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                break
                            except:
                                print("Enter a number please.")
                if timesQuizlet == "ns":
                    chooseRunType = input("Would you like to run the bot infinitely (Y or N)? >>> ")
                    if chooseRunType == "y" or chooseRunType == "Y":
                        if not timesQuizlet == "dw":
                            timesQuizlet = "dw"
                    if (chooseRunType == "n" or chooseRunType == "N"):
                        timesChoosen = False
                        while timesChoosen == False:
                            timesChoosen = True
                            timesQuizlet = input("How many quizes would you like to do? >>> ")
                            try:
                                timesQuizlet = int(timesQuizlet)
                                if not timesQuizlet < 0:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            except ValueError:
                                timesChoosen = False
                            if timesQuizlet < 0:
                                timesChoosen = False        
                if pageID == "ns":
                    print("PageID Location: "+"https://quizlet.com/"+"5000321"+"<--PAGEID"+"/cool-flash-cards/.") 
                    IDError = False
                    while True:
                        print("Paste in the URL of the Quizlet set you would like to start from, this can be from any section or game in the quizlet set or just type in the PageID yourself.")
                        pageIDURL = input("PageID or URL: >>> ")
                        pageIDTemp = re.findall('\d+', pageIDURL)
                        if pageIDTemp == None:
                            print("Invalid pageID or URL.")
                            IDError = True
                        if IDError == False:
                            try:
                                testList = int(pageIDTemp[1])
                                IDError = True
                                print("Multiple Values detected in URL or number.")  
                            except:
                                IDError = False
                            try:
                                pageIDTemp = int(pageIDTemp[0])
                            except:
                               print("ID is not an integer.") 
                               IDError = True  
                        if IDError == False:
                            pageID = int(pageIDTemp)
                            print("PageID has been successfully identified as: "+str(pageID)+".")
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            break 
                        IDError = False      
                if timesQuizlet == "dw":
                    started = True
                    oneQuiz = False
                if not timesQuizlet == "dw" and not timesQuizlet == "ns":
                    started = True
                    oneQuiz = True
            if runTypeInput == "SETTINGS":
                doneChanging = False
                while doneChanging == False:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                    if dev == False:
                        settingsoption = input("Type an option: "+"General, Gravity, Quit: >>> ")
                    else:
                        settingsoption = input("Type an option: "+"General, Gravity, Dev, Quit: >>> ")
                    settingsoption = settingsoption.upper()
                    if settingsoption == "QUIT": 
                        runTypeSelected = False
                        print("Leaving...")
                        break
                    if dev == True and settingsoption == "DEV":
                        while True:
                            devOption = input("Type an option: "+"Create Issue, Print Info, Run Code, Quit: >>> ")
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
                                    print("Choose a option: Easy, Medium, Hard")
                                    diffOption = input("I choose: >>> ")
                                    diffOption = diffOption.upper()
                                    if diffOption == "EASY":
                                        diff = 0
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        break
                                    elif diffOption == "MEDIUM":
                                        diff = 1
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        break
                                    elif diffOption == "HARD":
                                        diff = 2
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
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
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        break
                                    except:
                                        print("Enter a number please.")
                            elif gravityOption == "QUIT":
                                break
                    if settingsoption == "GENERAL":
                        while True:
                            print("Choose an option:"+" About, Login, GitHub Integration, PageID, Path to ChromeDriver, Bots to Run, Times to Run OQBRTA, Advanced, Quit")
                            generalChoose = input("I Choose: >>> ")
                            generalChoose = generalChoose.upper()
                            if generalChoose == "ADVANCED":
                                while True:
                                    advancedChoose = input("Choose an option: "+"Reset, Quit: >>> ")
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
                                    aboutChoose = input("Choose an option: "+"Version, Data, Quit: >>> ")
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
                                        if username == "nw" and password == "nw":
                                            print("You have disabled login.")
                                        if not username == "ns" and not username == "dw" and not password == "ns" and not password == "dw" and not username == "nw" and not password == "nw":
                                            print("The email is set to:",username)
                                        if not password == "ns" and not username == "dw" and not password == "dw" and not username == "ns" and not password == "nw" and not username == "nw":
                                            print("The password is: "+passwordhidden)
                                            seePassword = input("Would you like to see the password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass("Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == password):
                                                    print("The password is:", password)
                                                else:
                                                    print("Incorrect password.")
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
                                            print("The password is: "+gitPassword)
                                            seePassword = input("Would you like to see the GitHub password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass("Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == USERPASSWORD):
                                                    print("The password is:", USERPASSWORD+".")
                                                else:
                                                    print("Incorrect password.")
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
                                        enabledString = "You have enabled: "
                                        botsEnabled = False
                                        if match == True:
                                            enabledString = enabledString + "Match, "
                                            botsEnabled = True
                                        if gravity == True:
                                            enabledString = enabledString + "Gravity, "
                                            botsEnabled = True
                                        if learn == True:
                                            enabledString = enabledString + "Learn, "
                                            botsEnabled = True
                                        if flashcards == True:
                                            enabledString = enabledString + "Flashcards, "
                                            botsEnabled = True
                                        if write == True:
                                            enabledString = enabledString + "Write, "
                                            botsEnabled = True
                                        if spell == True:
                                            enabledString = enabledString + "Spell, "
                                            botsEnabled = True
                                        if test == True:
                                            enabledString = enabledString + "Test, "
                                            botsEnabled = True
                                        if botsEnabled == False:
                                            print("You have not picked which bots to run.")
                                        else:
                                            enabledString = enabledString[:-2]
                                            enabledString = enabledString + "."
                                            print(enabledString)
                            elif generalChoose == "LOGIN":
                                while True:
                                    if password == "dw" and username == "dw":
                                        loginSettings = input("What would you like to do? Enable Automatic Login, Disable Login or Quit: >>> ")
                                    elif password == "nw" and username == "nw":
                                        loginSettings = input("What would you like to do? Enable Manual Login or Quit: >>> ")
                                    else:
                                        loginSettings = input("What would you like to do? Change Email, Change Password, Disable Automatic Login or Quit: >>> ")
                                    loginSettings = loginSettings.upper()
                                    if username == "dw" and password == "dw" and loginSettings == "DISABLE LOGIN":
                                        username = "nw"
                                        password = "nw"
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    if username == "nw" and password == "nw" and loginSettings == "ENABLE MANUAL LOGIN":
                                        username = "dw"
                                        password = "dw"
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    if password == "dw" and username == "dw" and loginSettings == "ENABLE AUTOMATIC LOGIN":
                                        passwordChoosen = False
                                        while passwordChoosen == False:
                                            print("All the info you type in will be only stored on this machine and typed into the login screen.")
                                            print("Please make sure that your quizlet account is linked to the Google Account you enter.")
                                            username = input("Google Account Email: >>> ")
                                            password = getpass.getpass("Google Account Password: >>> ")
                                            confirmpassword = getpass.getpass("Confirm Password: >>> ")
                                            if confirmpassword == password:
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                                passwordChoosen = True
                                            else:
                                                print("Passwords do not match!")
                                                passwordChoosen = False
                                    if not password == "dw" and not username == "dw":
                                        if loginSettings == "DISABLE AUTOMATIC LOGIN":
                                            username = "dw"
                                            password = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        if loginSettings == "CHANGE PASSWORD":
                                            passwordVerified = False
                                            while passwordVerified == False:
                                                passwordVerified = True
                                                print("The password currently is: "+passwordhidden)
                                                verifypassword = getpass.getpass("Please enter your password to continue: >>> ")
                                                if verifypassword == password:
                                                    print("Correct!")
                                                    seePassword = input("Would you like to see the password (Y or N)? >>> ")
                                                    seePassword = seePassword.upper()
                                                    if seePassword == "Y":
                                                        print("The password currently is:", password)
                                                    else:
                                                        print("The password currently is: "+passwordhidden)
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
                                        gitSettings = input("What would you like to do? "+"Enable GitHub Integration, Quit: >>> ")
                                        disabled = True
                                    else:
                                        gitSettings = input("What would you like to do? "+"Change Username, Change Password, Disable GitHub Integration, Quit: >>> ")
                                        disabled = False
                                    gitSettings = gitSettings.upper()
                                    if gitSettings == "ENABLE GITHUB INTEGRATION" and disabled == True:
                                        while True:
                                            print("None of this data is transmitted to anywhere other then GitHub for Issue Reporting.")
                                            USERUSERNAME = input("GitHub Username: >>> ")
                                            USERPASSWORD = getpass.getpass("GitHub Password: >>> ")
                                            CONFIRMPASS = getpass.getpass("Confirm Password: >>> ")
                                            if USERPASSWORD == CONFIRMPASS:
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                                break
                                    if disabled == False:
                                        if gitSettings == "CHANGE USERNAME":
                                            print("The GitHub Username is currently set to:", USERUSERNAME+".")
                                            USERUSERNAME = input("I would like to change the GitHub Username to: >>> ")
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
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
                                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                                        break
                                            else:
                                                print("Incorrect Password!")
                                        if gitSettings == "DISABLE GITHUB INTEGRATION":
                                            USERUSERNAME = "dw"
                                            USERPASSWORD = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                            disabled = True
                                    if gitSettings == "QUIT":
                                        break
                            elif generalChoose == "PAGEID":
                                if pageID == "ns":
                                    print("PageID has not been set.")
                                else:
                                    print("PageID is set to:", pageID)
                                IDError = False
                                while True:
                                    print("Paste in the URL of the Quizlet set you would like to start from, this can be from any section or game in the quizlet set or just type in the PageID yourself.")
                                    pageIDURL = input("PageID or URL: >>> ")
                                    pageIDTemp = re.findall('\d+', pageIDURL)
                                    if pageIDTemp == None:
                                        print("Invalid pageID or URL.")
                                        IDError = True
                                    if IDError == False:
                                        try:
                                            testList = int(pageIDTemp[1])
                                            IDError = True
                                            print("Multiple Values detected in URL or number.")  
                                        except:
                                            IDError = False
                                        try:
                                            pageIDTemp = int(pageIDTemp[0])
                                        except:
                                           print("ID is not an integer.") 
                                           IDError = True  
                                    if IDError == False:
                                        pageID = int(pageIDTemp)
                                        print("PageID has been successfully identified as: "+str(pageID)+".")
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        break 
                                    IDError = False     
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
                               enabledString = "You have enabled: "
                               botsEnabled = False
                               if match == True:
                                   enabledString = enabledString + "Match, "
                                   botsEnabled = True
                               if gravity == True:
                                   enabledString = enabledString + "Gravity, "
                                   botsEnabled = True
                               if learn == True:
                                   enabledString = enabledString + "Learn, "
                                   botsEnabled = True
                               if flashcards == True:
                                   enabledString = enabledString + "Flashcards, "
                                   botsEnabled = True
                               if write == True:
                                   enabledString = enabledString + "Write, "
                                   botsEnabled = True
                               if spell == True:
                                   enabledString = enabledString + "Spell, "
                                   botsEnabled = True
                               if test == True:
                                   enabledString = enabledString + "Test, "
                                   botsEnabled = True
                               if botsEnabled == False:
                                   print("You have not picked which bots to run.")
                               else:
                                   enabledString = enabledString[:-2]
                                   enabledString = enabledString + "."
                                   print(enabledString)
                               input("Press Enter to continue...")
                               title = 'Choose bots to run (press SPACE to mark and ENTER to continue):'
                               options = ['Match', 'Gravity', 'Learn', 'Flashcards', 'Write', 'Spell', 'Test']
                               selected = pick(options, title, multi_select=True, min_selection_count=1)
                               if "Match" in str(selected):
                                  match = True
                               else:
                                   match = False
                               if "Gravity" in str(selected):
                                  gravity = True
                               else:
                                   gravity = False
                               if "Learn" in str(selected):
                                  learn = True
                               else:
                                   learn = False
                               if "Flashcards" in str(selected):
                                  flashcards = True
                               else:
                                   flashcards = False
                               if "Write" in str(selected):
                                  write = True
                               else:
                                   write = False
                               if "Spell" in str(selected):
                                  spell = True
                               else:
                                   spell = False
                               if "Test" in str(selected):
                                   test = True
                               else:
                                   test = False
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
                                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
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
                sleep(1)
                sys.exit()
            if updateNeeded == True:
                if not runTypeInput == "UPDATE" and not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
            else:
                if not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
        if started == True:
            def login():
                try:
                    browser.find_element_by_xpath('//div[@class="SiteHeader-signIn"]/button[2]').click()
                    sleep(1)
                    browser.find_element_by_xpath('//a[@class="UIButton UIButton--social UIButton--fill"]').click()
                    sleep(1)
                    if not username == "dw" and not password == "dw":
                        browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
                        sleep(1)
                        browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
                        sleep(1)
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
                    return True
                except:
                    return False
            problem = False
            loggedIn = False
            timesRan = 0
            chromedriver = path
            os.environ["webdriver.chrome.driver"] = chromedriver
            browser = webdriver.Chrome(chromedriver)
            browser.set_window_size(1600, 1000)
            if oneQuiz == False:
                while True:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                        restart = True
                        break
                    try:
                        browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                        sleep(1)
                        if not loggedIn and username != "nw" and password != "nw":
                            login = login()
                            if login == False:
                                failed = True
                                loggedIn = False
                            else:
                                loggedIn = True
                        button = browser.find_element_by_xpath('//div[@class="ModeControls-back"]/a')
                        button.click()
                        failed = False
                        sleep(1)
                        elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                        ans = []
                        rep = []
                        for element in elements1:
                            pair = element.find_elements_by_tag_name('span')
                            ans.append(pair[0].text)
                            rep.append(pair[1].text)
                    except:
                        failed = True
                    if gravity and not failed:
                        if failed == False:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/gravity")
                                sleep(1)
                                browser.find_element_by_xpath("//div[@class='GravitySplashView']/button").click()
                                sleep(0.1)
                                if diff == 0:
                                    browser.find_element_by_xpath('//input[@value="BEGINNER"]').click()
                                if diff == 1:
                                    browser.find_element_by_xpath('//input[@value="INTERMEDIATE"]').click()
                                if diff == 2:
                                    browser.find_element_by_xpath('//input[@value="EXPERT"]').click()
                                failedDropDown = 0
                                try:
                                    select = Select(browser.find_element_by_xpath('//select[@class="UIDropdown-select"]'))
                                except:
                                    failedDropDown = failedDropDown + 1
                                try:
                                    select.select_by_visible_text('Definition')
                                except:
                                    failedDropDown = failedDropDown + 1
                                if failedDropDown == 2:
                                    complain("An error occured clicking on the dropdown, this is the element's data: "+str(select))
                                browser.find_element_by_xpath("//div[@class='GravityOptionsView-nextButtonWrapper']/button").click()
                                sleep(0.1)
                                browser.find_element_by_xpath("//div[@class='GravityDirectionsView-startButton']/button").click()
                                sleep(0.2)
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
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    getScore = browser.find_element_by_xpath('html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                except:
                                    pass
                                while not found:
                                    try:
                                        asteroid = browser.find_element_by_class_name("GravityTerm-content")
                                        found = True
                                    except:
                                        found = False
                                answer = ''
                                while True:
                                    try:
                                        checkBrowser = browser.current_url
                                        chromeOpen = True
                                    except:
                                        chromeOpen = False
                                    if chromeOpen == False:
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        restart = True
                                        break
                                    try:
                                        asteroidText = asteroid.find_element_by_xpath("(//div[@class='GravityTerm-content'])/div/span").text
                                    except:
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
                                try:
                                    browser.find_element_by_xpath("//div[@class='GravityTypingPrompt-inputWrapper']/textarea").send_keys(answer+Keys.ENTER)
                                except:
                                    break
                            if restart == True:
                                break
                            if maxScore <= score:
                                failed = False
                                successesG = successesG + 1
                    if match and not failed:
                        if failed == False:
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                browser.find_element_by_xpath("//div[@class='MatchModeInstructionsModal-button']").click()
                                tiles = browser.find_elements_by_xpath("//div[@class='MatchModeQuestionGridTile']")
                                sleep(0.2)
                                tileNumber = 0 
                            except:
                                pass
                            while len(tiles) > 0:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                sleep(0.01)
                                currentTerm = tiles[0].text
                                tiles[0].click()
                                if currentTerm in ans:
                                    index = ans.index(currentTerm)
                                    myPairText = rep[index]
                                    pairIndex = 1
                                    while pairIndex < len(tiles):
                                        try:
                                            checkBrowser = browser.current_url
                                            chromeOpen = True
                                        except:
                                            chromeOpen = False
                                        if chromeOpen == False:
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                            restart = True
                                            break
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
                                        try:
                                            checkBrowser = browser.current_url
                                            chromeOpen = True
                                        except:
                                            chromeOpen = False
                                        if chromeOpen == False:
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                            restart = True
                                            break
                                        if tiles[pairIndex].text == myPairText:
                                            tiles[pairIndex].click()
                                            tiles.pop(pairIndex)
                                            break
                                        pairIndex += 1
                                tiles.pop(0)
                            sleep(0.5)
                            try:
                                browser.find_element_by_xpath('//button[@class="UIButton UIButton--hero"]')
                                successes = successes + 1
                            except:
                                failures = failures + 1   
                    if learn and not failed:
                       try:
                           checkBrowser = browser.current_url
                           chromeOpen = True
                       except:
                           chromeOpen = False
                       if chromeOpen == False:
                           save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                           restart = True
                           break
                       if failed == False:
                           try:
                               browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                               sleep(1)
                               browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                               browser.find_element_by_xpath('(//div[@class="AssistantOptionsModal-col"])[2]/label/input').click()
                               browser.find_element_by_xpath('(//div[@class="AssistantOptionsModal-col"])[3]/label/input').click()
                               browser.find_element_by_xpath('(//div[@class="UIModalHeader-closeIconButton"])/span/button').click()
                               sleep(0.5)
                               browser.find_element_by_xpath('(//div[@class="AssistantLearnIntroView-getStartedButton"])/button').click()
                               sleep(0.6)
                               browser.find_element_by_xpath('(//div[@class="AssistantLearnQuestionInfoView-gotItButton"])/button').click()
                               sleep(0.8) 
                           except:
                                pass
                           while True:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                failed = True
                                break
                            try:
                                cardword = browser.find_element_by_xpath("//span[contains(@class, 'TermText')]")
                                cardtext = cardword.text
                                if cardtext in ans:
                                    index = ans.index(cardtext)
                                    answer = rep[index]
                                elif cardtext in rep:
                                    index = rep.index(cardtext)
                                    answer = ans[index]
                                else:
                                    complain("Script Incorrectly Indentified Text in Write")
                                browser.find_element_by_xpath('//textarea').send_keys(answer+Keys.ENTER)
                                try:
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    if cardtext in ans:
                                        index = ans.index(cardtext)
                                        answer1 = rep[index]
                                    if cardtext in rep:
                                        index = rep.index(cardtext)
                                        answer2 = ans[index]
                                    browser.find_element_by_xpath('//textarea').send_keys(Keys.BACKSPACE * len(answer))
                                    browser.find_element_by_xpath('//textarea').send_keys(answer1+Keys.ENTER)
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    browser.find_element_by_xpath('//textarea').send_keys(answer2+Keys.ENTER)
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    complain("Could not go past wrong answer screen. List is as follows: "+str(ans)+str(rep)+".")
                                except:
                                    pass
                                sleep(0.1)
                                browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                sleep(0.5)
                            except:
                                try:
                                    browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                    sleep(0.5)
                                    progress = browser.find_element_by_class_name("ProgressSegmentedSemicircle-percent").text
                                    progress = progress.replace('%', '')
                                    progress = int(progress)
                                    if progress >= 100:
                                        try:
                                            sleep(0.5)
                                            browser.find_element_by_xpath('(//div[@class="AssistantEndView-finish"])/button').click()
                                            sleep(0.2)
                                        except:
                                            pass
                                        break
                                except:
                                    pass
                    if flashcards and not failed:
                        try:
                            checkBrowser = browser.current_url
                            chromeOpen = True
                        except:
                            chromeOpen = False
                        if chromeOpen == False:
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            restart = True
                            break
                        if failed == False:
                            browser.get("https://quizlet.com/"+str(pageID)+"/flashcards")
                            nextButton = browser.find_element_by_class_name("nextButton")
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                nextButton.click()
                                try:
                                    browser.find_element_by_xpath('//div[text()="THE END"]')
                                    break
                                except:
                                    pass
                            sleep(0.5)
                    if write and not failed:
                        if failed == False:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/write")
                                sleep(1)
                                termlist = browser.find_element_by_xpath('(//div[@class="LearnModeProgressBar-value"])[1]').text
                            except:
                                pass
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    termtext = browser.find_element_by_xpath('(//div[@class="LearnModeInputView-prompt"])/div/span').text
                                    if termtext in ans:
                                        index = ans.index(termtext)
                                        answer = rep[index]
                                    elif termtext in rep:
                                        index = rep.index(termtext)
                                        answer = ans[index]
                                    else:
                                        complain("Script Incorrectly Indentified Text in Write")
                                    browser.find_element_by_xpath("//textarea").send_keys(answer+Keys.ENTER)
                                    sleep(0.1)
                                    browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                    sleep(0.1)
                                except:
                                    complete = browser.find_element_by_xpath('(//div[@class="LearnModeProgressBar-value"])[1]').text
                                    if complete == "0":
                                        break
                    if spell and not failed:
                       if failed == False:
                           try:
                               browser.get("https://quizlet.com/"+str(pageID)+"/spell")
                               sleep(1)
                               try:
                                   browser.find_element_by_xpath('(//div[@class="UIDiv SpellModeGameAnalysisView-startOverButton js-spellRestartButton"])/button')
                                   stop = True
                               except:
                                   pass
                               browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                               sleep(0.2)
                               browser.find_element_by_xpath('((//span[@class="UIToggle-option"])/input)[3]').click()
                               sleep(0.5)
                               try:
                                   browser.switch_to_alert().accept()
                                   sleep(0.5)
                               except:
                                    try:
                                        browser.find_element_by_xpath('(//div[@class="UIModalHeader-closeIconButton"])/span/button').click()
                                    except:
                                        complain("Could not accept alert or close options.")
                               sleep(5)
                           except:
                            pass
                           while True:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                failed = True
                                break
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                break
                            try:
                                if stop:
                                    break
                            except:
                                pass
                            try:
                                sleep(0.8)
                                cardword = browser.find_element_by_xpath('(//div[@class="SpellModeInputView-prompt"])/span')
                                cardtext = cardword.text
                                if cardtext in ans:
                                       index = ans.index(cardtext)
                                       answer = rep[index]
                                elif cardtext in rep:
                                   index = rep.index(cardtext)
                                   answer = ans[index]
                                browser.find_element_by_xpath("//textarea").send_keys(answer+Keys.ENTER)
                            except:
                                try:
                                    browser.find_element_by_xpath('(//div[@class="SpellModeRoundAnalysisView-headerCell js-spellCheckpointContinue"])/button').click()
                                except:
                                    pass
                                try:
                                    browser.find_element_by_xpath('(//div[@class="UIDiv SpellModeGameAnalysisView-startOverButton js-spellRestartButton"])/button')
                                    break
                                except:
                                    pass
                                sleep(1)
                    if test and not failed:
                        if failed == False:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                break
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/test")
                                sleep(1)
                                browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                                sleep(0.2)
                                checkboxes = browser.find_elements_by_xpath('(//li[@class="TestModeOptions-listOption"])/label/input')
                                checkboxes[1].click()
                                checkboxes[2].click()
                                checkboxes[3].click()
                                browser.find_element_by_xpath('//button[@type="submit"]').click()
                                questions = browser.find_elements_by_xpath('(//span[@class="TestModeTermText"])/span/span')
                                inputs = browser.find_elements_by_xpath("//textarea")
                            except:
                                pass
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    currentQuestion = questions[0]
                                    currentQuestionText = currentQuestion.text
                                    if currentQuestionText in ans:
                                       index = ans.index(currentQuestionText)
                                       answer = rep[index]
                                    elif currentQuestionText in rep:
                                       index = rep.index(currentQuestionText)
                                       answer = ans[index]
                                    else:
                                        complain("Script Incorrectly Indentified Text in Write")
                                    inputs[0].send_keys(answer)
                                    questions.pop(0)
                                    inputs.pop(0)
                                except:
                                    browser.find_element_by_xpath('(//div[@class="UIDiv TestModePage-button"])/button').click()
                                    break
                    if chromeOpen:
                        pageID = pageID + 1
                    failed = False
                    extracted = False
            if oneQuiz == True:
                timesRan = 0
                while not timesRan == timesQuizlet:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                        restart = True
                        break
                    try:
                        browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                        sleep(1)
                        if not loggedIn and username != "nw" and password != "nw":
                            login = login()
                            if login == False:
                                failed = True
                                loggedIn = False
                            else:
                                loggedIn = True
                        button = browser.find_element_by_xpath('//div[@class="ModeControls-back"]/a')
                        button.click()
                        failed = False
                        sleep(1)
                        elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                        ans = []
                        rep = []
                        for element in elements1:
                            pair = element.find_elements_by_tag_name('span')
                            ans.append(pair[0].text)
                            rep.append(pair[1].text)
                    except:
                        failed = True
                    if gravity and not failed:
                        if failed == False:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/gravity")
                                sleep(1)
                                browser.find_element_by_xpath("//div[@class='GravitySplashView']/button").click()
                                sleep(0.1)
                                if diff == 0:
                                    browser.find_element_by_xpath('//input[@value="BEGINNER"]').click()
                                if diff == 1:
                                    browser.find_element_by_xpath('//input[@value="INTERMEDIATE"]').click()
                                if diff == 2:
                                    browser.find_element_by_xpath('//input[@value="EXPERT"]').click()
                                failedDropDown = 0
                                try:
                                    select = Select(browser.find_element_by_xpath('//select[@class="UIDropdown-select"]'))
                                except:
                                    failedDropDown = failedDropDown + 1
                                try:
                                    select.select_by_visible_text('Definition')
                                except:
                                    failedDropDown = failedDropDown + 1
                                if failedDropDown == 2:
                                    complain("An error occured clicking on the dropdown, this is the element's data: "+str(select))
                                browser.find_element_by_xpath("//div[@class='GravityOptionsView-nextButtonWrapper']/button").click()
                                sleep(0.1)
                                browser.find_element_by_xpath("//div[@class='GravityDirectionsView-startButton']/button").click()
                                sleep(0.2)
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
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    getScore = browser.find_element_by_xpath('html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                except:
                                    pass
                                while not found:
                                    try:
                                        asteroid = browser.find_element_by_class_name("GravityTerm-content")
                                        found = True
                                    except:
                                        found = False
                                answer = ''
                                while True:
                                    try:
                                        checkBrowser = browser.current_url
                                        chromeOpen = True
                                    except:
                                        chromeOpen = False
                                    if chromeOpen == False:
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                        restart = True
                                        break
                                    try:
                                        asteroidText = asteroid.find_element_by_xpath("(//div[@class='GravityTerm-content'])/div/span").text
                                    except:
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
                                try:
                                    browser.find_element_by_xpath("//div[@class='GravityTypingPrompt-inputWrapper']/textarea").send_keys(answer+Keys.ENTER)
                                except:
                                    break
                            if restart == True:
                                break
                            if maxScore <= score:
                                failed = False
                                successesG = successesG + 1
                    if match and not failed:
                        if failed == False:
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                browser.find_element_by_xpath("//div[@class='MatchModeInstructionsModal-button']").click()
                                tiles = browser.find_elements_by_xpath("//div[@class='MatchModeQuestionGridTile']")
                                sleep(0.2)
                                tileNumber = 0 
                            except:
                                pass
                            while len(tiles) > 0:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                sleep(0.01)
                                currentTerm = tiles[0].text
                                tiles[0].click()
                                if currentTerm in ans:
                                    index = ans.index(currentTerm)
                                    myPairText = rep[index]
                                    pairIndex = 1
                                    while pairIndex < len(tiles):
                                        try:
                                            checkBrowser = browser.current_url
                                            chromeOpen = True
                                        except:
                                            chromeOpen = False
                                        if chromeOpen == False:
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                            restart = True
                                            break
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
                                        try:
                                            checkBrowser = browser.current_url
                                            chromeOpen = True
                                        except:
                                            chromeOpen = False
                                        if chromeOpen == False:
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                            restart = True
                                            break
                                        if tiles[pairIndex].text == myPairText:
                                            tiles[pairIndex].click()
                                            tiles.pop(pairIndex)
                                            break
                                        pairIndex += 1
                                tiles.pop(0)
                            sleep(0.5)
                            try:
                                browser.find_element_by_xpath('//button[@class="UIButton UIButton--hero"]')
                                successes = successes + 1
                            except:
                                failures = failures + 1   
                    if learn and not failed:
                       try:
                           checkBrowser = browser.current_url
                           chromeOpen = True
                       except:
                           chromeOpen = False
                       if chromeOpen == False:
                           save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                           restart = True
                           break
                       if failed == False:
                           try:
                               browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                               sleep(1)
                               browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                               browser.find_element_by_xpath('(//div[@class="AssistantOptionsModal-col"])[2]/label/input').click()
                               browser.find_element_by_xpath('(//div[@class="AssistantOptionsModal-col"])[3]/label/input').click()
                               browser.find_element_by_xpath('(//div[@class="UIModalHeader-closeIconButton"])/span/button').click()
                               sleep(0.5)
                               browser.find_element_by_xpath('(//div[@class="AssistantLearnIntroView-getStartedButton"])/button').click()
                               sleep(0.6)
                               browser.find_element_by_xpath('(//div[@class="AssistantLearnQuestionInfoView-gotItButton"])/button').click()
                               sleep(0.8) 
                           except:
                                pass
                           while True:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                failed = True
                                break
                            try:
                                cardword = browser.find_element_by_xpath("//span[contains(@class, 'TermText')]")
                                cardtext = cardword.text
                                if cardtext in ans:
                                    index = ans.index(cardtext)
                                    answer = rep[index]
                                elif cardtext in rep:
                                    index = rep.index(cardtext)
                                    answer = ans[index]
                                else:
                                    complain("Script Incorrectly Indentified Text in Write")
                                browser.find_element_by_xpath('//textarea').send_keys(answer+Keys.ENTER)
                                try:
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    if cardtext in ans:
                                        index = ans.index(cardtext)
                                        answer1 = rep[index]
                                    if cardtext in rep:
                                        index = rep.index(cardtext)
                                        answer2 = ans[index]
                                    browser.find_element_by_xpath('//textarea').send_keys(Keys.BACKSPACE * len(answer))
                                    browser.find_element_by_xpath('//textarea').send_keys(answer1+Keys.ENTER)
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    browser.find_element_by_xpath('//textarea').send_keys(answer2+Keys.ENTER)
                                    browser.find_element_by_xpath('(//div[@class="AssistantWrittenQuestionCopyAnswerView-correctAnswerLabel"])/h6/span')
                                    complain("Could not go past wrong answer screen. List is as follows: "+str(ans)+str(rep)+".")
                                except:
                                    pass
                                sleep(0.1)
                                browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                sleep(0.5)
                            except:
                                try:
                                    browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                    sleep(0.5)
                                    progress = browser.find_element_by_class_name("ProgressSegmentedSemicircle-percent").text
                                    progress = progress.replace('%', '')
                                    progress = int(progress)
                                    if progress >= 100:
                                        try:
                                            sleep(0.5)
                                            browser.find_element_by_xpath('(//div[@class="AssistantEndView-finish"])/button').click()
                                            sleep(0.2)
                                        except:
                                            pass
                                        break
                                except:
                                    pass
                    if flashcards and not failed:
                        try:
                            checkBrowser = browser.current_url
                            chromeOpen = True
                        except:
                            chromeOpen = False
                        if chromeOpen == False:
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                            restart = True
                            break
                        if failed == False:
                            browser.get("https://quizlet.com/"+str(pageID)+"/flashcards")
                            nextButton = browser.find_element_by_class_name("nextButton")
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                nextButton.click()
                                try:
                                    browser.find_element_by_xpath('//div[text()="THE END"]')
                                    break
                                except:
                                    pass
                            sleep(0.5)
                    if write and not failed:
                        if failed == False:
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/write")
                                sleep(1)
                                termlist = browser.find_element_by_xpath('(//div[@class="LearnModeProgressBar-value"])[1]').text
                            except:
                                pass
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    termtext = browser.find_element_by_xpath('(//div[@class="LearnModeInputView-prompt"])/div/span').text
                                    if termtext in ans:
                                        index = ans.index(termtext)
                                        answer = rep[index]
                                    elif termtext in rep:
                                        index = rep.index(termtext)
                                        answer = ans[index]
                                    else:
                                        complain("Script Incorrectly Indentified Text in Write")
                                    browser.find_element_by_xpath("//textarea").send_keys(answer+Keys.ENTER)
                                    sleep(0.1)
                                    browser.find_element_by_tag_name("body").send_keys(Keys.ENTER)
                                    sleep(0.1)
                                except:
                                    complete = browser.find_element_by_xpath('(//div[@class="LearnModeProgressBar-value"])[1]').text
                                    if complete == "0":
                                        break
                    if spell and not failed:
                       if failed == False:
                           try:
                               browser.get("https://quizlet.com/"+str(pageID)+"/spell")
                               sleep(1)
                               try:
                                   browser.find_element_by_xpath('(//div[@class="UIDiv SpellModeGameAnalysisView-startOverButton js-spellRestartButton"])/button')
                                   stop = True
                               except:
                                   pass
                               browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                               sleep(0.2)
                               browser.find_element_by_xpath('((//span[@class="UIToggle-option"])/input)[3]').click()
                               sleep(0.5)
                               try:
                                   browser.switch_to_alert().accept()
                                   sleep(0.5)
                               except:
                                    try:
                                        browser.find_element_by_xpath('(//div[@class="UIModalHeader-closeIconButton"])/span/button').click()
                                    except:
                                        complain("Could not accept alert or close options.")
                               sleep(5)
                           except:
                            pass
                           while True:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                failed = True
                                break
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                break
                            try:
                                if stop:
                                    break
                            except:
                                pass
                            try:
                                sleep(0.8)
                                cardword = browser.find_element_by_xpath('(//div[@class="SpellModeInputView-prompt"])/span')
                                cardtext = cardword.text
                                if cardtext in ans:
                                       index = ans.index(cardtext)
                                       answer = rep[index]
                                elif cardtext in rep:
                                   index = rep.index(cardtext)
                                   answer = ans[index]
                                browser.find_element_by_xpath("//textarea").send_keys(answer+Keys.ENTER)
                            except:
                                try:
                                    browser.find_element_by_xpath('(//div[@class="SpellModeRoundAnalysisView-headerCell js-spellCheckpointContinue"])/button').click()
                                except:
                                    pass
                                try:
                                    browser.find_element_by_xpath('(//div[@class="UIDiv SpellModeGameAnalysisView-startOverButton js-spellRestartButton"])/button')
                                    break
                                except:
                                    pass
                                sleep(1)
                    if test and not failed:
                        if failed == False:
                            try:
                                checkBrowser = browser.current_url
                                chromeOpen = True
                            except:
                                chromeOpen = False
                            if chromeOpen == False:
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                restart = True
                                break
                            try:
                                browser.get("https://quizlet.com/"+str(pageID)+"/test")
                                sleep(1)
                                browser.find_element_by_xpath('(//div[@class="ModeControls-action"])/button').click()
                                sleep(0.2)
                                checkboxes = browser.find_elements_by_xpath('(//li[@class="TestModeOptions-listOption"])/label/input')
                                checkboxes[1].click()
                                checkboxes[2].click()
                                checkboxes[3].click()
                                browser.find_element_by_xpath('//button[@type="submit"]').click()
                                questions = browser.find_elements_by_xpath('(//span[@class="TestModeTermText"])/span/span')
                                inputs = browser.find_elements_by_xpath("//textarea")
                            except:
                                pass
                            while True:
                                try:
                                    checkBrowser = browser.current_url
                                    chromeOpen = True
                                except:
                                    chromeOpen = False
                                if chromeOpen == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, match, gravity, learn, flashcards, write, spell, test, diff)
                                    restart = True
                                    failed = True
                                    break
                                try:
                                    currentQuestion = questions[0]
                                    currentQuestionText = currentQuestion.text
                                    if currentQuestionText in ans:
                                       index = ans.index(currentQuestionText)
                                       answer = rep[index]
                                    elif currentQuestionText in rep:
                                       index = rep.index(currentQuestionText)
                                       answer = ans[index]
                                    else:
                                        complain("Script Incorrectly Indentified Text in Write")
                                    inputs[0].send_keys(answer)
                                    questions.pop(0)
                                    inputs.pop(0)
                                except:
                                    browser.find_element_by_xpath('(//div[@class="UIDiv TestModePage-button"])/button').click()
                                    break
                    extracted = False
                    timesRan = timesRan + 1
                    if not timesRan == timesQuizlet and chromeOpen:
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
