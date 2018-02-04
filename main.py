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
            print(Style.RESET_ALL+"You are on an outdated version. Overriding...")
    if updateNeeded == True:
        print(Style.RESET_ALL+"ERROR: Cannot report issue due to outdated version, sorry.")
        sleep(1)
        sys.exit()
    else:
        import json
        with open ('info.json', 'r') as myfile:
            info=json.loads(myfile.read())
        USERUSERNAME = info["USERUSERNAME"]
        USERPASSWORD = info["USERPASSWORD"]
        if issueRead == False:
            print(Style.RESET_ALL+"An error has occured titled:", error+".")
        if issueRead == True:
            print(Style.RESET_ALL+"An error was read titled:", error+".")
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
                errorIssue = input(Style.RESET_ALL+"ERROR: COULD NOT IMPORT REQUESTS OR CONNECT TO THE INTERNET, WOULD YOU LIKE THE BOT TO SAVE THE ISSUE TO A FILE AND REPORT IT LATER (Y OR N)? >>> ")
                errorIssue = errorIssue.upper()
                if errorIssue == "Y":
                    import os, inspect
                    directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
                    os.chdir(directory)
                    try:
                        with open('issue.txt', 'w+') as w1:
                            w1.write(error)
                        print(Style.RESET_ALL+"Created File Successfully!")
                        print(Style.RESET_ALL+"Exiting...")
                        break
                    except:
                        print(Style.RESET_ALL+"Failed to create file. ):")
                        print(Style.RESET_ALL+"Exiting...")
                        break
                elif errorIssue == "N":
                    break
            from time import sleep
            from sys import exit
            sleep(1)
            exit()
        else:
            createissue = input(Style.RESET_ALL+"Would you like the script to create an issue for you (Y or N)? >>> ")
            if createissue == "y" or createissue == "Y":
                if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                    gitHubLoggedIn = False
                elif USERUSERNAME == "ns" and USERPASSWORD == "ns":
                    gitHubLoggedIn = False
                else:
                    gitHubLoggedIn = True
                while gitHubLoggedIn == False:
                    print(Style.RESET_ALL+"None of this data is transmitted, it is just used to create an issue on GitHub.")
                    gitHubLoggedIn = True
                    if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                        print(Style.RESET_ALL+"This is not saved, it's just used to report the issue.")
                        USERUSERNAME = input(Style.RESET_ALL+"What is your GitHub username? >>> ")
                        USERPASSWORD = getpass.getpass(Style.RESET_ALL+"What is your GitHub password? >>> ")
                        CONFIRMPASS = getpass.getpass(Style.RESET_ALL+"Confirm your password: >>> ")
                    if USERUSERNAME == "ns" and USERPASSWORD == "ns":
                        print(Style.RESET_ALL+"This is not saved, it's just used to report the issue.")
                        USERUSERNAME = input(Style.RESET_ALL+"What is your GitHub username? >>> ")
                        USERPASSWORD = getpass.getpass(Style.RESET_ALL+"What is your GitHub password? >>> ")
                        CONFIRMPASS = getpass.getpass(Style.RESET_ALL+"Confirm your password: >>> ")
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
                    print(Style.RESET_ALL+'Successfully created Issue "%s"' % error)
                    sleep(1)
                    sys.exit()
                else:
                    print(Style.RESET_ALL+'Could not create Issue "%s"' % error)
                    print(Style.RESET_ALL+'Response:', r.content)
                    sleep(1)
                    sys.exit()
            else:
                from time import sleep
                import sys
                sleep(1)
                sys.exit()
try:
    version = 5.8
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
            from colorama import Fore, Style, init
            init(autoreset=True)
            imported = True
        except ImportError:
            import pip
            imported = False
            userChoose = False
            while userChoose == False:
                askforinstall = input(Style.RESET_ALL+"Some packages were not found, would you like the script to install them for you (Y or N)? >>> ")
                askforinstall = askforinstall.upper()
                if askforinstall == "Y":
                    print(Style.RESET_ALL+"Installing...")
                    try:
                        from selenium.webdriver.common.keys import Keys
                    except ImportError:
                        install('selenium')
                    try:
                        from colorama import Style
                    except ImportError:
                        install('colorama')
                    try:
                        import tldextract
                    except ImportError:
                        install('tldextract')
                    try:
                        import requests
                    except ImportError:
                        install('requests')
                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Installed!")
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
            print(Style.RESET_ALL+Style.BRIGHT+Fore.GREEN+"Updating to V.",title+"...")
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
        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You are not connected to the internet, please connect and try again.")
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
            option = 'ns'
            diff = 'ns'
            recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "timesQuizlet": "ns", "username": "ns", "password": "ns", "USERUSERNAME": "ns", "USERPASSWORD": "ns", "maxScore": "ns", "successesG": 0, "failuresG": 0, "option": "ns", "diff": "ns"}
            with open ('info.json', 'r+') as myfile:
                recover=myfile.write(json.dumps(recover))
        try:
            with open ('info.json', 'r') as myfile:
                info=json.loads(myfile.read())
        except:
            jsonreset = input(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"ERROR: COULD NOT LOAD IN JSON, WOULD YOU LIKE TO TRY TO FIX THE JSON (Y or N)? >>> ")
            jsonreset = jsonreset.upper()
            if jsonreset == "Y":
                jsonfix = input(Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+"Would you like to reset the JSON or manually repair it? >>> ")
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
                    print(Style.RESET_ALL+Fore.YELLOW+"The JSON reads:", data+".")
                    pageID = input(Style.RESET_ALL+Fore.YELLOW+"PageID: >>> ")
                    successes = input(Style.RESET_ALL+Fore.YELLOW+"Successes: >>> ")
                    failures = input(Style.RESET_ALL+Fore.YELLOW+"Failures: >>> ")
                    path = input(Style.RESET_ALL+Fore.YELLOW+"Path: >>> ")
                    timesQuizlet = input(Style.RESET_ALL+Fore.YELLOW+"TimesQuizlet: >>> ")
                    username = input(Style.RESET_ALL+Fore.YELLOW+"Username: >>> ")
                    password = getpass.getpass(Style.RESET_ALL+Fore.YELLOW+"Password: >>> ")
                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"If you don't see any refrences to USERUSERNAME and PASSWORD, then just type in 'ns' for all of them.")
                    USERUSERNAME = input(Style.RESET_ALL+Fore.YELLOW+"USERUSERNAME: >>> ")
                    USERPASSWORD = getpass.getpass(Style.RESET_ALL+Fore.YELLOW+"USERPASSWORD: >>> ")
                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"If you don't see any refrences to maxScore, successesG, Option, Diff, and failuresG, then just type in 'ns' for all of them.")
                    maxScore = input(Style.RESET_ALL+Fore.YELLOW+"MaxScore: >>> ")
                    successesG = input(Style.RESET_ALL+Fore.YELLOW+"SuccessesG: >>> ")
                    failuresG = input(Style.RESET_ALL+Fore.YELLOW+"FailuresG: >>> ")
                    option = input(Style.RESET_ALL+Fore.YELLOW+"Option: >>> ")
                    diff = input(Style.RESET_ALL+Fore.YELLOW+"Diff: >>> ")
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
            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Updated JSON to include GitHub Integration! Please restart the script!")
            sleep(1)
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
            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Updated JSON to include a Gravity Bot! Please restart the script!")
            sleep(1)
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
                chromecheck = input(Style.RESET_ALL+Fore.BLUE+'Have you installed ChromeDriver (Y or N)? >>> ')
                if (chromecheck == "y" or chromecheck == "Y"):
                    path = input(Style.RESET_ALL+Fore.BLUE+"The path to chromedriver is: >>> ")
                    if not os.path.exists(path):
                        print(Style.RESET_ALL+Fore.RED+"Invalid Path.")
                        checkedforchrome = False
                    else:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        print(Style.RESET_ALL+Fore.GREEN+"Continuing...")
                if (not chromecheck == "Y" and not chromecheck == "y" and not chromecheck == "N" and not chromecheck == "n"):
                    print(Style.RESET_ALL+Fore.RED+Style.BRGIHT+"Invalid Option...Restarting...")
                    checkedforchrome = False
                if (chromecheck == "n" or chromecheck == "N"):
                    chromeinstalled = input(Style.RESET_ALL+Fore.BLUE+"Would you like the script to install it for you (Y or N)? >>> ")
                    if (chromeinstalled == "y" or chromeinstalled == "Y"):
                        while (osSelected == False):
                            osSelected = True
                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Downloading...")
                            if (userplatform == "WIN32" or userplatform == "WINDOWS"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip"
                                file_name = "chromedriver_win32.zip"
                            if (userplatform == "DARWIN" or userplatform == "MAC"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.33/chromedriver_mac64.zip"
                                file_name = "chromedriver_mac64.zip"
                            if (userplatform == "LINUX"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip"
                                file_name = "chromedriver_linux64.zip"
                            if (userplatform == "LINUX32"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux32.zip"
                                file_name = "chromedriver_linux32.zip"
                            with urllib.request.urlopen(downloadurl) as response, open(file_name, 'wb') as out_file:
                                shutil.copyfileobj(response, out_file)
                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Downloaded! Please extract the file to the script's directory and restart the script.")
                            sleep(1)
                            sys.exit()
                    if (chromeinstalled == "n" or chromeinstalled == "N"):
                            print(Style.RESET_ALL+Fore.GREEN+"Goodbye!")
                            sleep(1)
                            sys.exit()
        if (username == "ns" and password == "ns"):
            reply = input(Style.RESET_ALL+Fore.BLUE+'Would you like to have the script enter your username and password for you (Y or N)? >>> ')
            if (reply == "n" or reply == "N"):
                username = "dw"
                password = "dw"
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
            elif (reply == "Y" or reply == "y"):
                while passwordChoosen == False:
                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"All the info you type in will be only stored on this machine and typed into the login screen.")
                    username = input(Style.RESET_ALL+Fore.BLUE+"Email: >>> ")
                    password = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Password: >>> ")
                    confirmpassword = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm Password: >>> ")
                    if confirmpassword == password:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        passwordChoosen = True
                    else:
                        print(Style.RESET_ALL+Fore.RED+"Passwords do not match!")
                        passwordChoosen = False
        if USERUSERNAME == "ns" and USERPASSWORD == "ns":
            reply = input(Style.RESET_ALL+Fore.BLUE+"Would you like the script to integrate with your GitHub account (Y or N)? >>> ")
            reply = reply.upper()
            if reply == "Y":
                while True:
                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"None of this data is transmitted to anywhere other then GitHub for Issue Reporting.")
                    USERUSERNAME = input(Style.RESET_ALL+Fore.BLUE+"GitHub Username: >>> ")
                    USERPASSWORD = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"GitHub Password: >>> ")
                    CONFIRMPASS = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm Password: >>> ")
                    if USERPASSWORD == CONFIRMPASS:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                        break
            elif reply == "N":
                USERUSERNAME = "dw"
                USERPASSWORD = "dw"
                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
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
                    print(Style.RESET_ALL+Style.BRIGHT+"Type in an option: "+Fore.GREEN+"Start, Settings, Help, Update, Quit")
                if dev == True:
                    print(Style.RESET_ALL+Style.BRIGHT+"Type in an option: "+Fore.GREEN+Style.BRIGHT+"Start, Settings, Help, Update, Expirment, Quit")
            else:
                if dev == True:
                    if uploadable == True:
                        print(Style.RESET_ALL+Style.BRIGHT+"Type in an option: "+Fore.GREEN+Style.BRIGHT+"Start, Settings, Help, Upload, Expirment, Quit")
                    else:
                        print(Style.RESET_ALL+Style.BRIGHT+"Type in an option: "+Fore.GREEN+Style.BRIGHT+"Start, Settings, Help, Expirment, Quit")
                else:
                    print(Style.RESET_ALL+"Type in an option:"+Fore.GREEN+Style.BRIGHT+" Start, Settings, Quit")
            runTypeInput = input(Style.RESET_ALL+Fore.BLUE+"I choose: >>> ")
            runTypeInput = runTypeInput.upper()
            if updateNeeded == True:
                if runTypeInput == "UPDATE":
                    update.update()
            if runTypeInput == "HELP":
                print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Welcome to the help menu "+Style.RESET_ALL+Style.DIM+"(beta)"+Style.RESET_ALL+Fore.GREEN+"!")
                while True:
                    helpInput = input(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Choose an option: pageID, How to Quit when Running, Quit: >>> "+Style.RESET_ALL)
                    helpInput = helpInput.upper()
                    if helpInput == "HOW TO QUIT WHEN RUNNING":
                        print(Style.RESET_ALL+Fore.BLUE+"In order to quit the bot while it is running, simply close the open chrome window.")
                    if helpInput == "PAGEID":
                        print(Style.RESET_ALL+"The page ID is a number contained in the URL of a quizlet set. It tells the bot what quizlet set to go to. "+Style.BRIGHT+"Example:"+Style.RESET_ALL+Style.DIM+"https://quizlet.com/"+Style.RESET_ALL+Style.BRIGHT+"5000321"+Fore.GREEN+"<--PAGEID"+Style.RESET_ALL+Style.DIM+"/cool-flash-cards/.") 
                    elif helpInput == "QUIT":
                        break
            if runTypeInput == "EXPIRMENT":
                print(Style.RESET_ALL+Fore.BLUE+"Starting GUI...")
                from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
                from PyQt5.QtCore import QCoreApplication
                class Example(QWidget):

                    def __init__(self):
                        super().__init__()

                        self.initUI()


                    def initUI(self):
                        # sbtn = QPushButton('Start', self)
                        # sbtn.clicked.connect(print(Style.RESET_ALL+"Hello!"))
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
                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Version is not higher than current release.")
                    uploadable = False
                codeGood = os.system('pyflakes main.py')
                if codeGood == 0 and uploadable:
                    uploadable = True
                else:
                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Pyflakes returned an error!")
                    uploadable = False
                if uploadable == True:
                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Code checks complete! All code seems good!")
                    checked = True
                    if checked == True:
                        fname = os.path.basename(__file__)
                        with open(fname, 'r') as f1:
                            updatedcode = f1.read()
                        titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
                        title = titleget.text
                        titlenumber = len(title)
                        updateName = input(Style.RESET_ALL+Fore.BLUE+"What should the commit name be? >>> ")
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
                    else:
                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"ERROR: Pastebin Version is Newer.")
                        runTypeSelected = False
            if runTypeInput == "START":
                if option == "ns":
                    while True:
                        optionInput = input(Style.RESET_ALL+Fore.BLUE+"What game would you like the bot to complete? Gravity, Match, Gravity and Match: >>> ")
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
                            print(Style.RESET_ALL+"Invalid Option!")
                if option == 2 or option == 0:
                    if diff == "ns":
                        while True:
                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Choose a difficulty for the Gravity Bot: Easy, Medium, Hard")
                            diffOption = input(Style.RESET_ALL+Fore.BLUE+"I choose: >>> ")
                            diffOption = diffOption.upper()
                            if diffOption == "EASY":
                                diff = 0
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print(Style.RESET_ALL+Style.BRIGHT+"You have set the difficulty to easy for the Gravity Bot.")
                                break
                            elif diffOption == "MEDIUM":
                                diff = 1
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print(Style.RESET_ALL+Style.BRIGHT+"You have set the difficulty to medium for the Gravity Bot.")
                                break
                            elif diffOption == "HARD":
                                diff = 2
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                print(Style.RESET_ALL+Style.BRIGHT+"You have set the difficulty to hard for the Gravity Bot.")
                                break
                    if maxScore == "ns":
                        while True:
                            maxScore = input(Style.RESET_ALL+Fore.BLUE+"What should be the target score for the Gravity Bot? >>> ")
                            try:
                                maxScore = int(maxScore)
                                if maxScore < 0:
                                    maxScore = dict(maxScore)
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                break
                            except:
                                print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Enter a number please.")
                if timesQuizlet == "ns":
                    chooseRunType = input(Style.RESET_ALL+Fore.BLUE+"Would you like to run the bot infinitely (Y or N)? >>> ")
                    if chooseRunType == "y" or chooseRunType == "Y":
                        if not timesQuizlet == "dw":
                            timesQuizlet = "dw"
                    if (chooseRunType == "n" or chooseRunType == "N"):
                        timesChoosen = False
                        while timesChoosen == False:
                            timesChoosen = True
                            timesQuizlet = input(Style.RESET_ALL+Fore.BLUE+"How many quizes would you like to do? >>> ")
                            try:
                                timesQuizlet = int(timesQuizlet)
                                if not timesQuizlet < 0:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                            except ValueError:
                                timesChoosen = False
                            if timesQuizlet < 0:
                                timesChoosen = False        
                if pageID == "ns":
                    print(Style.RESET_ALL+Style.BRIGHT+"PageID Location: "+Style.RESET_ALL+Style.DIM+"https://quizlet.com/"+Style.RESET_ALL+Style.BRIGHT+"5000321"+Fore.GREEN+"<--PAGEID"+Style.RESET_ALL+Style.DIM+"/cool-flash-cards/.") 
                    IDError = False
                    while True:
                        pageIDURL = input(Style.RESET_ALL+Fore.BLUE+"Paste in the URL of the Quizlet set you would like to start from, this can be from any section or game in the set or type in the PageID yourself: >>> ")
                        pageID = re.findall('\d+', pageIDURL)
                        if pageID == None:
                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Invalid pageID or URL.")
                            IDError = True
                        if IDError == False:
                            try:
                                pageID = int(pageID[0])
                            except:
                               print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"PageID is not an integer.") 
                               IDError = True    
                        if IDError == False:
                            print(Style.RESET_ALL+Fore.GREEN+"PageID has been successfully identified as: "+Style.BRIGHT+str(pageID)+Style.RESET_ALL+".")
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                            break 
                        IDError = False     
                        started = True
                        oneQuiz = False
                    
                if timesQuizlet == "dw":
                    started = True
                    oneQuiz = False
                if not timesQuizlet == "dw" and not timesQuizlet == "ns":
                    started = True
                    oneQuiz = True
            if runTypeInput == "SETTINGS":
                doneChanging = False
                while doneChanging == False:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                    if dev == False:
                        settingsoption = input(Style.RESET_ALL+"Type an option: "+Fore.GREEN+Style.BRIGHT+"General, Gravity, Quit: >>> ")
                    else:
                        settingsoption = input(Style.RESET_ALL+"Type an option: "+Fore.GREEN+Style.BRIGHT+"General, Gravity, Dev, Quit: >>> ")
                    settingsoption = settingsoption.upper()
                    if settingsoption == "QUIT": 
                        runTypeSelected = False
                        print(Style.RESET_ALL+"Leaving...")
                        break
                    if dev == True and settingsoption == "DEV":
                        while True:
                            devOption = input(Style.RESET_ALL+Style.RESET_ALL+"Type an option: "+Fore.GREEN+Style.BRIGHT+"Create Issue, Print Info, Run Code, Quit: >>> ")
                            devOption = devOption.upper()
                            if devOption == "CREATE ISSUE":
                                issueName = input(Style.RESET_ALL+Fore.BLUE+"What would you like to name the issue? >>> ")
                                complain(issueName)
                            elif devOption == "PRINT INFO":
                                with open('info.json', 'r') as myfile:
                                    data=myfile.read().replace('\n', '')
                                print(Style.RESET_ALL+Style.BRIGHT+'Info reads:', data)
                            elif devOption == "RUN CODE":
                                codeRun = input(Style.RESET_ALL+Fore.BLUE+"What would you like to run? >>> ")
                                try:
                                    exec(codeRun)
                                except Exception as e:
                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Welp...your code failed, this is what happened:", e)
                            elif devOption == "QUIT":
                                break
                    if settingsoption == "GRAVITY":
                        while True:
                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Choose an option: Target Score, Difficulty, Quit")
                            gravityOption = input(Style.RESET_ALL+Fore.BLUE+"I choose: >>> ")
                            gravityOption = gravityOption.upper()
                            if gravityOption == "DIFFICULTY":
                                while True:
                                    if diff == "ns":
                                        print(Style.RESET_ALL+Fore.RED+"You have not set the difficulty for the Gravity Bot.")
                                    else:
                                        if diff == 0:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to easy for the Gravity Bot.")
                                        elif diff == 1:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to medium for the Gravity Bot.")
                                        elif diff == 2:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to hard for the Gravity Bot.")
                                        else:
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Something is corrupt! Oh no!")
                                            sleep(0.5)
                                            complain("Diff Variable is corrupt.")
                                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Choose a option: Easy, Medium, Hard")
                                    diffOption = input(Style.RESET_ALL+Fore.BLUE+"I choose: >>> ")
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
                                        print(Style.RESET_ALL+Fore.RED+"Invalid Option!")
                            if gravityOption == "TARGET SCORE":
                                if maxScore == "ns":
                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You have not set the target score for the Gravity Bot.")
                                else:
                                    print(Style.RESET_ALL+Fore.BLUE+"The target score for the Gravity Bot is:", str(maxScore)+".")
                                while True:
                                    maxScore = input(Style.RESET_ALL+Fore.BLUE+"What should be the target score for the Gravity Bot? >>> ")
                                    try:
                                        maxScore = int(maxScore)
                                        if maxScore < 0:
                                            maxScore = dict(maxScore)
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        break
                                    except:
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Enter a number please.")
                            elif gravityOption == "QUIT":
                                break
                    if settingsoption == "GENERAL":
                        while True:
                            print(Style.RESET_ALL+"Choose an option:"+Fore.GREEN+Style.BRIGHT+" About, Automatic Login, GitHub Integration, PageID, Path to ChromeDriver, Bots to Run, Times to Run OQBRTA, Advanced, Quit")
                            generalChoose = input(Style.RESET_ALL+Fore.BLUE+"I Choose: >>> ")
                            generalChoose = generalChoose.upper()
                            if generalChoose == "ADVANCED":
                                while True:
                                    advancedChoose = input(Style.RESET_ALL+"Choose an option: "+Fore.GREEN+Style.BRIGHT+"Reset, Quit: >>> ")
                                    advancedChoose = advancedChoose.upper()
                                    if advancedChoose == "RESET":
                                        usersure = input(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Are you sure (Y or N)? >>> ")
                                        if (usersure == "y" or usersure == "Y"):
                                            reset()
                                            restart = True
                                    elif advancedChoose == "QUIT":
                                        break
                            if generalChoose == "ABOUT":
                                while True:
                                    aboutChoose = input(Style.RESET_ALL+"Choose an option: "+Fore.GREEN+Style.BRIGHT+"Version, Data, Quit: >>> ")
                                    aboutChoose = aboutChoose.upper()
                                    if aboutChoose == "QUIT":
                                        break
                                    if aboutChoose == "VERSION":
                                        if osis == 0:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"This is OQBRTA, V.", version, "and you are running MacOS.")
                                        if osis == 1:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"This is OQBRTA, V.", version, "and you are running Windows.")
                                        if osis == 2:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"This is OQBRTA, V.", version, "and you are running Linux.")
                                        if not osis == 0 and not osis == 1 and not osis == 2:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"This is OQBRTA, V.", version, "and you are running an unknown OS called:", userplatform+".")
                                    elif aboutChoose == "DATA":
                                        if pageID == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"PageID has not been set.")
                                        else:
                                            print(Style.RESET_ALL+Fore.GREEN+"PageID is set to:",str(pageID))
                                        print(Style.RESET_ALL+Fore.GREEN+"There have been:",str(failures),"failures.")
                                        print(Style.RESET_ALL+Fore.GREEN+"There have been:",str(successes),"successes.")
                                        if path == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The path to ChromeDriver is not set.")
                                        else:
                                            print(Style.RESET_ALL+Fore.GREEN+"The path to ChromeDriver is set to:",path)
                                        if timesQuizlet == "dw":
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set OQBRTA to run infinitely.")
                                        if timesQuizlet == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You have not set how many times you want OQBRTA to run.")
                                        if not timesQuizlet == "ns" and not timesQuizlet == "dw":
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set OQBRTA to run:", timesQuizlet, "times.")
                                        if username == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The email is not set.")
                                        if username == "dw" and password == "dw":
                                            print(Style.RESET_ALL+Fore.GREEN+"You have disabled automatic password and email entering.")
                                        if not username == "ns" and not username == "dw" and not password == "ns" and not password == "dw":
                                            print(Style.RESET_ALL+Fore.GREEN+"The email is set to:",username)
                                        if not password == "ns" and not username == "dw" and not password == "dw" and not username == "ns":
                                            print(Style.RESET_ALL+Fore.GREEN+"The password is: "+Style.RESET_ALL+Style.DIM+passwordhidden)
                                            seePassword = input(Style.RESET_ALL+Fore.BLUE+"Would you like to see the password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == password):
                                                    print(Style.RESET_ALL+Fore.GREEN+"The password is:", password)
                                                else:
                                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Incorrect password.")
                                        if password == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The password is not set.")
                                        if USERUSERNAME == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The GitHub Username is not set.")
                                        if USERPASSWORD == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The GitHub Password is not set.")
                                        if USERUSERNAME == "dw" and USERPASSWORD == "dw":
                                            print(Style.RESET_ALL+Fore.GREEN+"You have disabled GitHub Integration.")
                                        if not USERUSERNAME == "dw" and not USERUSERNAME == "ns":
                                            print(Style.RESET_ALL+Fore.GREEN+"Your GitHub username is set to:", USERUSERNAME+".")
                                        if not USERPASSWORD == "dw" and not USERPASSWORD == "ns":
                                            print(Style.RESET_ALL+"The password is: "+Style.RESET_ALL+Style.DIM+gitPassword)
                                            seePassword = input(Style.RESET_ALL+Fore.BLUE+"Would you like to see the GitHub password (Y or N)? >>> ")
                                            seePassword = seePassword.upper()
                                            if seePassword == "Y":
                                                passwordprotect = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Enter the password to unhide the password: >>> ")
                                                if (passwordprotect == USERPASSWORD):
                                                    print(Style.RESET_ALL+Fore.GREEN+"The password is:", USERPASSWORD+".")
                                                else:
                                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Incorrect password.")
                                        if maxScore != "ns":
                                            print(Style.RESET_ALL+Fore.GREEN+"The target score for Gravity is set to:", str(maxScore)+".")
                                        else:
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The target score for Gravity is not set.")
                                        print(Style.RESET_ALL+Fore.GREEN+"There have been", str(successesG), "successes in the Gravity Bot.")
                                        print(Style.RESET_ALL+Fore.RED+"There have been", str(failuresG), "failures in the Gravity Bot.")
                                        if diff == 0:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to easy in the Gravity Bot.")
                                        elif diff == 1:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to medium in the Gravity Bot.")
                                        elif diff == 2:
                                            print(Style.RESET_ALL+Fore.GREEN+"You have set the difficulty to hard in the Gravity Bot.")
                                        else:
                                            print(Fore.RED+Style.BRIGHT+"Oh no! A variable is corrupt!")
                                            complain("Diff variable is corrupt.")
                                        if option == "ns":
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You have not decided which bot(s) to run.")
                                        else:
                                            if option == 0:
                                                print(Style.RESET_ALL+Fore.GREEN+"You have decided to only run the Gravity Bot.")
                                            if option == 1:
                                                print(Style.RESET_ALL+Fore.GREEN+"You have decided to only run the Match Bot.")
                                            if option == 2:
                                                print(Style.RESET_ALL+Fore.GREEN+"You have decided to run both the Gravity and Match Bots.")
                            elif generalChoose == "AUTOMATIC LOGIN":
                                while True:
                                    if password == "dw" and username == "dw":
                                        loginSettings = input(Style.RESET_ALL+Fore.BLUE+"What would you like to do? Enable Automatic Login or Quit: >>> ")
                                    else:
                                        loginSettings = input(Style.RESET_ALL+Fore.BLUE+"What would you like to do? Change Email, Change Password, Disable Automatic Login or Quit: >>> ")
                                    loginSettings = loginSettings.upper()
                                    if password == "dw" and username == "dw" and loginSettings == "ENABLE AUTOMATIC LOGIN":
                                        passwordChoosen = False
                                        while passwordChoosen == False:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"All the info you type in will be only stored on this machine and typed into the login screen.")
                                            username = input(Style.RESET_ALL+Fore.BLUE+"Email: >>> ")
                                            password = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Password: >>> ")
                                            confirmpassword = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm Password: >>> ")
                                            if confirmpassword == password:
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                                passwordChoosen = True
                                            else:
                                                print(Style.RESET_ALL+Fore.RED+"Passwords do not match!")
                                                passwordChoosen = False
                                    if not password == "dw" and not username == "dw":
                                        if loginSettings == "DISABLE AUTOMATIC LOGIN":
                                            username = "dw"
                                            password = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        if loginSettings == "CHANGE PASSWORD":
                                            passwordVerified = False
                                            while passwordVerified == False:
                                                passwordVerified = True
                                                print(Style.RESET_ALL+Fore.GREEN+"The password currently is: "+Style.RESET_ALL+Style.DIM+passwordhidden)
                                                verifypassword = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Please enter your password to continue: >>> ")
                                                if verifypassword == password:
                                                    print(Style.RESET_ALL+"Correct!")
                                                    seePassword = input(Style.RESET_ALL+Fore.BLUE+"Would you like to see the password (Y or N)? >>> ")
                                                    seePassword = seePassword.upper()
                                                    if seePassword == "Y":
                                                        print(Style.RESET_ALL+Fore.GREEN+"The password currently is:", password)
                                                    else:
                                                        print(Style.RESET_ALL+Fore.YELLOW+"The password currently is: "+Style.RESET_ALL+Style.DIM+passwordhidden)
                                                    passwordChanged = False
                                                    while passwordChanged == False:
                                                        password = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"I would like to change my password to: >>> ")
                                                        confirmpassword = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm: >>> ")
                                                        if confirmpassword == password:
                                                            print(Style.RESET_ALL+Fore.GREEN+"Changed!")
                                                            passwordChanged = True
                                                        else:
                                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Passwords do not match!")
                                                else:
                                                    passwordVerified = True
                                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Invalid Password!")
                                        if loginSettings == "CHANGE EMAIL":
                                            if username == "ns":
                                                print(Style.RESET_ALL+Fore.RED+"The email has not been set.")
                                            if not username == "ns" and not username == "dw":
                                                print(Style.RESET_ALL+Fore.GREEN+"The email is set to:", username)
                                            if not username == "dw":
                                                username = input(Style.RESET_ALL+Fore.BLUE+"I would like to set the email to: >>> ")
                                    if loginSettings == "QUIT":
                                        break
                            elif generalChoose == "GITHUB INTEGRATION":
                                while True:
                                    if USERUSERNAME == "dw" and USERUSERNAME == "dw":
                                        gitSettings = input(Style.RESET_ALL+"What would you like to do? "+Fore.GREEN+Style.BRIGHT+"Enable GitHub Integration, Quit: >>> ")
                                        disabled = True
                                    else:
                                        gitSettings = input(Style.RESET_ALL+"What would you like to do? "+Fore.GREEN+Style.BRIGHT+"Change Username, Change Password, Disable GitHub Integration, Quit: >>> ")
                                        disabled = False
                                    gitSettings = gitSettings.upper()
                                    if gitSettings == "ENABLE GITHUB INTEGRATION" and disabled == True:
                                        while True:
                                            print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"None of this data is transmitted to anywhere other then GitHub for Issue Reporting.")
                                            USERUSERNAME = input(Style.RESET_ALL+Fore.BLUE+"GitHub Username: >>> ")
                                            USERPASSWORD = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"GitHub Password: >>> ")
                                            CONFIRMPASS = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm Password: >>> ")
                                            if USERPASSWORD == CONFIRMPASS:
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                                break
                                    if disabled == False:
                                        if gitSettings == "CHANGE USERNAME":
                                            print(Style.RESET_ALL+Fore.GREEN+"The GitHub Username is currently set to:", USERUSERNAME+".")
                                            USERUSERNAME = input(Style.RESET_ALL+Fore.BLUE+"I would like to change the GitHub Username to: >>> ")
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        if gitSettings == "CHANGE PASSWORD":
                                            print(Style.RESET_ALL+Fore.GREEN+"The GitHub password is set to:", gitPassword+".")
                                            passwordProtect = getpass.getpass(Style.RESET_ALL+Fore.GREEN+"Enter your GitHub Password First: >>> ")
                                            if passwordProtect == USERPASSWORD:
                                                showPass = input(Style.RESET_ALL+Fore.BLUE+"Would you like to see the GitHub password (Y or N)? >>> ")
                                                showPass = showPass.upper()
                                                if showPass == "Y":
                                                    if passwordProtect == USERPASSWORD:
                                                        print(Style.RESET_ALL+Fore.GREEN+"The GitHub password is set to:", USERPASSWORD+".")
                                                while True:
                                                    USERPASSWORD = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"GitHub Password: >>> ")
                                                    CONFIRMPASS = getpass.getpass(Style.RESET_ALL+Fore.BLUE+"Confirm Password: >>> ")
                                                    if USERPASSWORD == CONFIRMPASS:
                                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                                        break
                                            else:
                                                print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Incorrect Password!")
                                        if gitSettings == "DISABLE GITHUB INTEGRATION":
                                            USERUSERNAME = "dw"
                                            USERPASSWORD = "dw"
                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                            disabled = True
                                    if gitSettings == "QUIT":
                                        break
                            elif generalChoose == "PAGEID":
                                if pageID == "ns":
                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"PageID has not been set.")
                                else:
                                    print(Style.RESET_ALL+Fore.GREEN+"PageID is set to:", pageID)
                                pageIDChoosen = False
                                while pageIDChoosen == False:
                                    pageIDChoosen = True
                                    pageID = input(Style.RESET_ALL+Fore.BLUE+"What would you like to set the pageID to? >>> ")
                                    try:
                                        pageID = int(pageID)
                                        if pageID < 0:
                                            pageID = dict(pageID)
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    except ValueError:
                                        pageIDChoosen = False
                            elif generalChoose == "PATH TO CHROMEDRIVER":
                                if path == "ns":
                                    print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The path to ChromeDriver has not been set.")
                                else:
                                    print(Style.RESET_ALL+Fore.GREEN+"The path to ChromeDriver is set to:", path)
                                    checkedforchrome = False
                                    while (checkedforchrome == False):
                                            checkedforchrome = True
                                            path = input(Style.RESET_ALL+Fore.BLUE+"I would like to set the path to ChromeDriver to: >>> ")
                                            if not os.path.exists(path):
                                                print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Invalid Path!")
                                                checkedforchrome = False
                            elif generalChoose == "BOTS TO RUN":
                                while True:
                                    if option == 0:
                                        print(Style.RESET_ALL+Fore.GREEN+"You have decided to only run the Gravity Bot.")
                                    elif option == 1:
                                        print(Style.RESET_ALL+Fore.GREEN+"You have decided to only run the Match Bot.")
                                    elif option == 2:
                                        print(Style.RESET_ALL+Fore.GREEN+"You have decided to run both the Gravity and Match Bots.")
                                    else:
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You have not set what bots to run.")
                                    optionInput = input(Style.RESET_ALL+"Choose a bot:"+Fore.GREEN+Style.BRIGHT+" Gravity, Match, Gravity and Match: >>> ")
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
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Invalid Option!")
                            elif generalChoose == "TIMES TO RUN OQBRTA":
                                while True:
                                    if timesQuizlet == "dw":
                                        print(Style.RESET_ALL+Fore.GREEN+"You have decided to run OQBRTA infinitely.")
                                    if not timesQuizlet == "dw" and not timesQuizlet == "ns":
                                        print(Style.RESET_ALL+Fore.GREEN+"You have decided to run OQBRTA", timesQuizlet, "times.")
                                    if timesQuizlet == "ns":
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"You have not set the amount of times you would like to run OQBRTA.")
                                    timesQuizletSettings = input(Style.RESET_ALL+Fore.BLUE+"What would you like to do? Run OQBRTA infinitely, Run OQBRTA a specific amount of times or Quit: >>> ")
                                    timesQuizletSettings = timesQuizletSettings.upper()
                                    if timesQuizletSettings == "RUN OQBRTA INFINITELY" or timesQuizletSettings == "RUN INFINITELY" or timesQuizletSettings == "INFINITELY":
                                        if not timesQuizlet == "dw":
                                            timesQuizlet = "dw"
                                    elif timesQuizletSettings == "RUN OQBRTA A SPECIFIC AMOUNT OF TIMES" or timesQuizletSettings == "SPECIFIC AMOUNT" or timesQuizletSettings == "SPECIFIC":
                                        timesChoosen = False
                                        while timesChoosen == False:
                                            timesChoosen = True
                                            timesQuizlet = input(Style.RESET_ALL+Fore.BLUE+"How many quizes would you like to do? >>> ")
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
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"Invalid Option!")
                            elif generalChoose == "QUIT":
                                break
            if runTypeInput == "QUIT":
                print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"Goodbye!")
                sleep(1)
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
                                sleep(1)
                                button = browser.find_element_by_xpath('//div[@class="ModeControls-back"]/a')
                                button.click()
                                failed = False
                            except:
                                failuresG = failuresG + 1
                                failed = True
                            if failed == False:
                                try:
                                    sleep(1)
                                    elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                                    ans = []
                                    rep = []
                                    for element in elements1:
                                        pair = element.find_elements_by_tag_name('span')
                                        ans.append(pair[0].text)
                                        rep.append(pair[1].text)
                                    extracted = True
                                    if not loggedIn:
                                        browser.find_element_by_xpath('//button[1]/span').click()
                                        sleep(0.1)
                                        browser.find_element_by_xpath('//div[@class="UIRow"][1]/div/a').click()
                                        if not username == "dw" and not password == "dw":
                                            browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
                                            sleep(1)
                                            browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
                                            sleep(1)
                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print(Style.RESET_ALL+"You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/gravity")
                                    sleep(1)
                                    browser.find_element_by_xpath("//div[@class='GravitySplashView']/button").click()
                                    sleep(0.1)
                                    if diff == 0:
                                        browser.find_element_by_xpath('//input[@value="BEGINNER"]').click()
                                    if diff == 1:
                                        browser.find_element_by_xpath('//input[@value="INTERMEDIATE"]').click()
                                    if diff == 2:
                                        browser.find_element_by_xpath('//input[@value="EXPERT"]')
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
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        restart = True
                                        break
                                    # try:
                                    getScore = browser.find_element_by_xpath('html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                    while not found:
                                        try:
                                            asteroid = browser.find_element_by_class_name("GravityTerm-content")
                                            found = True
                                        except:
                                            found = False
                                    answer = ''
                                    while True:
                                        try:
                                            asteroidText = asteroid.find_element_by_xpath("//span[@class='TermText notranslate lang-en']").text
                                        except:
                                            print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
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
                                        print(Style.RESET_ALL+Fore.RED+Style.BRIGHT+"The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
                                        break
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
                                        sleep(1)
                                        browser.find_element_by_xpath('//div[@class="SiteHeader-signIn"]/button[2]').click()
                                        sleep(0.3)
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
                                                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                                    sleep(0.5)
                                    try:
                                        browser.find_element_by_xpath('//span[@class="ModeControls-backText"]/span').click()
                                        failed = False
                                    except:
                                        failed = True
                                    if failed == False:
                                        sleep(0.5)
                                        elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                                        ans = []
                                        rep = []
                                        for element in elements1:
                                            pair = element.find_elements_by_tag_name('span')
                                            ans.append(pair[0].text)
                                            rep.append(pair[1].text)
                                        failed = False
                                if failed == True:
                                    failures = failures + 1
                                if failed == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                    browser.find_element_by_xpath("//div[@class='MatchModeInstructionsModal-button']").click()
                                    tiles = browser.find_elements_by_xpath("//div[@class='MatchModeQuestionGridTile']")
                                    sleep(0.2)
                                    tileNumber = 0
                                    while len(tiles) > 0:
                                        sleep(0.01)
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
                                    sleep(0.5)
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
                                sleep(1)
                                browser.find_element_by_xpath('//div[@class="ModeControls-back"]/a').click()
                                failed = False
                            except:
                                failuresG = failuresG + 1
                                failed = True
                            if failed == False:
                                try:
                                    sleep(1)
                                    elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                                    ans = []
                                    rep = []
                                    for element in elements1:
                                        pair = element.find_elements_by_tag_name('span')
                                        ans.append(pair[0].text)
                                        rep.append(pair[1].text)
                                    extracted = True
                                    if not loggedIn:
                                        browser.find_element_by_xpath('//button[1]/span').click()
                                        sleep(0.1)
                                        browser.find_element_by_xpath('//div[@class="UIRow"][1]/div/a').click()
                                        if not username == "dw" and not password == "dw":
                                            browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
                                            sleep(1)
                                            browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
                                            sleep(1)
                                        if username == "dw" and password == "dw":
                                            printed = False
                                            while True:
                                                if printed == False:
                                                    print(Style.RESET_ALL+"You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True
                                    browser.get("https://quizlet.com/"+str(pageID)+"/gravity")
                                    sleep(1)
                                    browser.find_element_by_xpath("//div[@class='GravitySplashView']/button").click()
                                    sleep(0.1)
                                    if diff == 0:
                                        browser.find_element_by_xpath('//input[@value="BEGINNER"]').click()
                                    if diff == 1:
                                        browser.find_element_by_xpath('//input[@value="INTERMEDIATE"]').click()
                                    if diff == 2:
                                        browser.find_element_by_xpath('//input[@value="EXPERT"]')
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
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                        restart = True
                                        break
                                    # try:
                                    getScore = browser.find_element_by_xpath('html/body/div[2]/main/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/span[2]')
                                    score = getScore.text
                                    score = score.replace(",", "")
                                    score = int(score)
                                    found = False
                                    asteroid = None
                                    while not found:
                                        try:
                                            asteroid = browser.find_element_by_class_name("GravityTerm-content")
                                            found = True
                                        except:
                                            found = False
                                    answer = ''
                                    while True:
                                        try:
                                            asteroidText = asteroid.find_element_by_xpath("//span[@class='TermText notranslate lang-en']").text
                                        except:
                                            print(Style.RESET_ALL+Style.BRIGHT+Fore.RED+"The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
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
                                    browser.find_element_by_xpath("//div[@class='GravityTypingPrompt-inputWrapper']/textarea").send_keys(answer+Keys.ENTER)
                                    # except:
                                    #     print(Style.RESET_ALL+"The Gravity Bot encountered an error, this is most likely due to a foreign language being used.")
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
                                        sleep(0.3)
                                        browser.find_element_by_xpath('//div[@class="SiteHeader-signIn"]/button[2]').click()
                                        sleep(0.3)
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
                                                    print(Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+"You can now login.")
                                                    printed = True
                                                getBrowserUrl = browser.current_url
                                                simpleURL = tldextract.extract(getBrowserUrl)
                                                simpleURL = simpleURL.domain
                                                if not simpleURL == "google":
                                                    break
                                        loggedIn = True

                                    browser.get("https://quizlet.com/"+str(pageID)+"/learn")
                                    sleep(0.5)
                                    try:
                                        browser.find_element_by_xpath('//span[@class="ModeControls-backText"]/span').click()
                                        failed = False
                                    except:
                                        failed = True
                                    if failed == False:
                                        sleep(0.5)
                                        elements1 = browser.find_elements_by_class_name("SetPageTerm-content")
                                        ans = []
                                        rep = []
                                        for element in elements1:
                                            pair = element.find_elements_by_tag_name('span')
                                            ans.append(pair[0].text)
                                            rep.append(pair[1].text)
                                        failed = False
                                if failed == True:
                                    failures = failures + 1
                                if failed == False:
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password, USERUSERNAME, USERPASSWORD, maxScore, successesG, failuresG, option, diff)
                                    browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                                    browser.find_element_by_xpath("//div[@class='MatchModeInstructionsModal-button']").click()
                                    tiles = browser.find_elements_by_xpath("//div[@class='MatchModeQuestionGridTile']")
                                    sleep(0.2)
                                    tileNumber = 0
                                    while len(tiles) > 0:
                                        sleep(0.01)
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
                                    sleep(0.5)
                                    successes = successes + 1
                            except:
                                failures = failures + 1
                        extracted = False
                        timesRan = timesRan + 1
                        if not timesRan == timesQuizlet:
                            pageID = pageID + 1
                    if timesRan == timesQuizlet:
                        print(Style.RESET_ALL+"Complete.")
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
