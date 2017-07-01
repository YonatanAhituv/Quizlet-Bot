version = 0
import requests, os, sys, time
class Updater:
    def __init__(self):
        pass
    def checkForUpdates(self):
        titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
        pasteV = titleget.text
        pasteV = float(pasteV)
        if pasteV == 5.0:
            return True
        else:
            return False
    def update(self):
        fname = os.path.basename(__file__)
        titleget = requests.get('https://pastebin.com/raw/hHLndhTS')
        title = titleget.text
        print("Updating to V.",title+"...")
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
update = Updater()
updateOut = update.checkForUpdates()
if not updateOut:
    print("Thank you for supporting and downloading OQBRTA. However, currently, OQBRTA is non-functional right now, this script is now only an updater. When 5.0 is released, this script will transform into OQBRTA. Thank you.")
else:
    print("Installing OQBRTA...")
    update.update()
    time.sleep(1)
    sys.exit()
