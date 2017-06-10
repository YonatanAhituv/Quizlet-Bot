issueRead = False
def complain(error, body=None, assignee=None, milestone=None, labels=["bug"]):
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
            except:
                print("Failed to create file. ):")
            print("Exiting...")
            import time
            time.sleep(1)
            sys.exit()
    else:
        createissue = input("Would you like the script to create an issue for you (Y or N)? >>> ")
        if createissue == "y" or createissue == "Y":
            print("None of this data is transmitted, it is just used to create an issue on GitHub.")
            gitHubLoggedIn = False
            while gitHubLoggedIn == False:
                gitHubLoggedIn = True
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
                    time.sleep(1)
                    sys.exit()
                else:
                    print('Could not create Issue "%s"' % error)
                    print('Response:', r.content)
        else:
            import time
            time.sleep(1)
            sys.exit()
try:
    # TODO: Phase out all bool based while loops, switch to a while true and break model instead
    # TODO: Phase out all giant, if nots, replace with if, elif, and else
    imported = False
    while imported == False:
        import inspect
        import time
        import sys
        import json
        import urllib
        import shutil
        import platform
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
                    time.sleep(1)
                    sys.exit()
                else:
                    time.sleep(1)
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
            fname = os.path.basename(__file__)
            reply = requests.get('https://raw.githubusercontent.com/AtomicCoding/Quizlet-Bot/master/main.py')
            code = reply.text
            with open('update.py', 'w+') as w1:
                w1.write(code)
            with open(fname, 'r') as f1:
                oldcode = f1.read()
                with open('update.py', 'r') as f2:
                    newcode = f2.read()
                    if not oldcode == newcode:
                        f2.close()
                        w1.close()
                        os.remove("update.py")
                        return True
                    if oldcode == newcode:
                        f2.close()
                        w1.close()
                        os.remove("update.py")
                        return False
        def update(self):
            fname = os.path.basename(__file__)
            titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
            title = titleget.text
            print("Updating to:",title+"...")
            reply = requests.get('https://raw.githubusercontent.com/AtomicCoding/Quizlet-Bot/master/main.py')
            code = reply.text
            with open('update.py', 'w+') as w1:
                w1.write(code)
                with open('update.py', 'r') as f2:
                    newcode = f2.read()
            with open(fname, 'w+') as f:
                f.write(newcode)
                f2.close()
                w1.close()
                os.remove('update.py')
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
        time.sleep(1)
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
            recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "timesQuizlet": "ns", "username": "ns", "password": "ns"}
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
                    recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "timesQuizlet": "ns", "username": "ns", "password": "ns"}
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
                    pageID = int(pageID)
                    successes = int(successes)
                    failures = int(failures)
                    try:
                        timesQuizlet = int(timesQuizlet)
                    except:
                        pass
                    recover = {"pageID": pageID, "successes": successes, "failures": failures, "path": path, "timesQuizlet": timesQuizlet, "username": username, "password": password}
                    with open ('info.json', 'r+') as myfile:
                        recover=myfile.write(json.dumps(recover))
                    sys.exit()
        if not osis == 0 and not osis == 1 and not osis == 2:
            complain("Unknown OS detected called:"+str(userplatform))
        def save(info, pageID1, successes1, failures1, path1, timesQuizlet1, username1, password1):
            info["pageID"] = pageID1
            info["successes"] = successes1
            info["failures"] = failures1
            info["path"] = path1
            info["timesQuizlet"] = timesQuizlet1
            info["username"] = username1
            info["password"] = password1
            with open ('info.json', 'r+') as myfile:
                info=myfile.write(json.dumps(info))
        pageID = info["pageID"]
        successes = info["successes"]
        failures = info["failures"]
        path = info["path"]
        timesQuizlet = info["timesQuizlet"]
        username = info["username"]
        password = info["password"]
        if timesQuizlet == "nw":
            timesQuizlet = "dw"
        if username == "nw":
            username = "dw"
        if password == "nw":
            password = "dw"
        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
        checkedforchrome = False
        if not os.path.exists(path):
            path = "ns"
            save(info, pageID, successes, failures, path, timesQuizlet, username, password)
        def reset():
            os.remove("info.json")
        if path == "ns":
            if (osis == 1):
                my_file = directory+"/"+"chromedriver.exe"
            else:
                my_file = directory+"/"+"chromedriver"
            if os.path.exists(my_file):
                path = my_file
                save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_win32.zip"
                                file_name = "chromedriver_win32.zip"
                            if (userplatform == "DARWIN" or userplatform == "MAC"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_mac64.zip"
                                file_name = "chromedriver_mac64.zip"
                            if (userplatform == "LINUX"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip"
                                file_name = "chromedriver_linux64.zip"
                            if (userplatform == "LINUX32"):
                                downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux32.zip"
                                file_name = "chromedriver_linux32.zip"
                            with urllib.request.urlopen(downloadurl) as response, open(file_name, 'wb') as out_file:
                                shutil.copyfileobj(response, out_file)
                            print("Downloaded! Please unzip the file and restart the script.")
                            time.sleep(1)
                            sys.exit()
                    if (chromeinstalled == "n" or chromeinstalled == "N"):
                            print("Goodbye!")
                            time.sleep(1)
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
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                        passwordChoosen = True
                    else:
                        print("Passwords do not match!")
                        passwordChoosen = False
        runTypeSelected = False
        while runTypeSelected == False:
            runTypeSelected = True
            update = Updater()
            updateNeeded = update.checkForUpdates()
            passwordhidden = len(password) * "•"
            if updateNeeded == True:
                print("Type in an option: Start, Settings, Update, Quit")
            else:
                print("Type in an option: Start, Settings, Quit")
            time.sleep(0.1)
            runTypeInput = input("I choose: >>> ")
            time.sleep(0.1)
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
            if runTypeInput == "START":
                if timesQuizlet == "ns":
                    chooseRunType = input("Would you like to do infinite quizes (Y or N)? >>> ")
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
                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                                save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                            except ValueError:
                                pageIDChoosen = False
                        started = True
                        oneQuiz = True
            if runTypeInput == "SETTINGS":
                doneChanging = False
                while doneChanging == False:
                    save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                    settingsoption = input("Type an option: About, Data, Quit: >>> ")
                    settingsoption = settingsoption.upper()
                    if settingsoption == "ABOUT":
                        if osis == 0:
                            print("This is OQBRTA, V: 3.7.1 and you are running MacOS.")
                        if osis == 1:
                            print("This is OQBRTA, V: 3.7.1 and you are running Windows.")
                        if osis == 2:
                            print("This is OQBRTA, V: 3.7.1 and you are running Linux.")
                        if not osis == 0 and not osis == 1 and not osis == 2:
                            print("This is OQBRTA, V: 3.7.1 and you are running an unknown OS called:", userplatform+".")
                    if settingsoption == "DATA":
                        dataChangeTypeChoosen = False
                        while dataChangeTypeChoosen == False:
                            datachangeType = input("Type an option: Edit, View, Reset, Quit: >>> ")
                            datachangeType = datachangeType.upper()
                            if not datachangeType == "EDIT" and not datachangeType == "VIEW" and not datachangeType == "RESET" and not datachangeType == "QUIT":
                                dataChangeTypeChoosen = False
                            if datachangeType == "QUIT":
                                dataChangeTypeChoosen = True
                            if datachangeType == "VIEW":
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
                            if datachangeType == "RESET":
                                usersure = input("Are you sure (Y or N)? >>> ")
                                if (usersure == "y" or usersure == "Y"):
                                    reset()
                                    restart = True
                                    dataChangeTypeChoosen = True
                                    doneChanging = True
                                if (usersure == "n" or usersure == "N"):
                                    dataChangeTypeChoosen = False
                            if datachangeType == "EDIT":
                                dataChanged = False
                                while dataChanged == False:
                                    whattochange = input("Type a variable: PageID, ChromeDriver Path, Times to run OQBRTA, Automatic Login, Quit: >>> ")
                                    whattochange = whattochange.upper()
                                    if whattochange == "PAGEID":
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
                                                save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                                            except ValueError:
                                                pageIDChoosen = False
                                        doneChanging = False
                                    if whattochange == "CHROMEDRIVER PATH":
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
                                            doneChanging = False
                                    if whattochange == "TIMES TO RUN OQBRTA":
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
                                                            save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                                                    except ValueError:
                                                        timesChoosen = False
                                                    if timesQuizlet < 0:
                                                        timesChoosen = False
                                            elif timesQuizletSettings == "QUIT" or timesQuizletSettings == "EXIT":
                                                break
                                            else:
                                                print("Invalid Option!")
                                    if whattochange == "AUTOMATIC LOGIN":
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
                                                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                                                    else:
                                                        print("Passwords do not match!")
                                                        passwordChoosen = True
                                            if not password == "dw" and not username == "dw":
                                                if loginSettings == "DISABLE AUTOMATIC LOGIN":
                                                    username = "dw"
                                                    password = "dw"
                                                    save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                                    if whattochange == "QUIT":
                                        dataChanged = True
                                    if not whattochange == "PAGEID" and not whattochange == "CHROMEDRIVER PATH" and not whattochange == "AUTOMATIC LOGIN" and not whattochange == "QUIT":
                                        doneChanging = False
                    if settingsoption == "QUIT":
                        print("Leaving...")
                        doneChanging = True
                        runTypeSelected = False
                    if not settingsoption == "ABOUT" and not settingsoption == "DATA" and not settingsoption == "QUIT":
                        doneChanging = False
            if runTypeInput == "QUIT":
                print("Goodbye!")
                time.sleep(1)
                sys.exit()
            if updateNeeded == True:
                if not runTypeInput == "UPDATE" and not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
            else:
                if not runTypeInput == "EXPIRMENT" and not runTypeInput == "START" and not runTypeInput == "QUIT" and not runTypeInput == "SETTINGS":
                    runTypeSelected = False
        if started == True:
            chromedriver = path
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
                time.sleep(2)
                try:
                    browser.find_element_by_xpath("html/body/div[5]/div/div[2]/div/div/div[1]/div[3]/div[1]/button").click()
                except:
                    browser.find_element_by_xpath("//a[@href][2]").click()
                time.sleep(2)
                browser.find_element_by_xpath("//a[@href='/google-oauth-redirector?from=%2Fsign-up&customParams=%7B%22signupOrigin%22%3A%22trophies-modal%22%7D']").click()
                if not username == "dw" and not password == "dw":
                    browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
                    time.sleep(1)
                    browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
                    time.sleep(1)
                else:
                    while True:
                        printed = False
                        if printed == False:
                            print("You can now login.")
                            printed = True
                        getBrowserUrl = browser.current_url
                        simpleURL = tldextract.extract(getBrowserUrl)
                        simpleURL = simpleURL.domain
                        if not simpleURL == "google":
                            break
            if oneQuiz == False:
                while True:
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                        restart = True
                        break
                    else:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
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
                        except:
                            failures = failures + 1
                            pageID = pageID + 1
            if oneQuiz == True:
                timesRan = 0
                while not timesRan == timesQuizlet:
                    try:
                        checkBrowser = browser.current_url
                        chromeOpen = True
                    except:
                        chromeOpen = False
                    if chromeOpen == False:
                        save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                        restart = True
                        break
                    else:
                        try:
                            save(info, pageID, successes, failures, path, timesQuizlet, username, password)
                            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
                            browser.find_element_by_id("start").click()
                            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
                            for term in terms:
                                click(term.get_attribute("data-id"))
                            successes = successes + 1
                            timesRan = timesRan + 1
                            if not loggedIn:
                                login()
                                loggedIn = True
                            time.sleep(2)
                        except:
                            failures = failures + 1
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
        ex = e+" on line: "+linenumber
        complain(str(ex))
