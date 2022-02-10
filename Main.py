import ctypes
import os

try:
    import random
    import string
    import threading
    import requests
    from requests.auth import HTTPProxyAuth
    import requests
    import time
    import colorama
    from termcolor import colored
    from colorama import Fore, Back, Style
    colorama.init()
    import easygui
except Exception as e:
    print(e)

time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Flex#8888")

print(colored("""

              
              ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
              ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
              ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
              ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
              ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
              ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                              
                                                              Dev: Flex#8629
              


""", "blue"))


global codeschecked
codeschecked = 0
global goodcoeds
goodcoeds = 0
usegenratorfile = False
global kill
kill = False
colorama.init()
global proxycount
proxycount = 0
try:
    filetoopen = open("proxy.txt", "r")
except:
    print("Proxy File Not Found ! >> proxy.txt")
    input("Enter To Close")
proxies = filetoopen.readlines()
global proxylength
proxylength = 0
for line in proxies:
    proxylength += 1

ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Flex#8629  | Loaded {} Proxies".format(proxylength))

print(Fore.RED + "[1] Generate Random Codes To Check " + Fore.RESET + Fore.WHITE + "|" + Fore.RESET + Fore.GREEN + " [2] Import Codes From File")
print("\n")
print(Fore.MAGENTA + "Enter Choice: " + Fore.RESET + Fore.GREEN, end="")
useanswer = input("")
time.sleep(0.3)
os.system("cls")

if useanswer == "1":
    usegenratorfile = False
else:
    if useanswer == "2":
        global usercount
        usercount = 0
        usegenratorfile = True
        path = easygui.fileopenbox()
        try:
            filetoopen = open(path, "r")
        except:
            print(path + " Not Found..")

        global codes
        codes = filetoopen.readlines()
        codescount = 0
        for line in codes:
            codescount += 1
        print(colored("Loaded {} Codes".format(codescount) , "magenta"))


def starting():
    global usercount, proxycount

    while not kill:

        if usegenratorfile:
            usercount += 1
            if usercount > codescount - 1:
                print("Finished")
                kil = True
            proxycount += 1
            if proxycount > proxylength - 2:
                proxycount = 0

            codetocheck = codes[usercount]
            checkcode(codetocheck, proxies[proxycount])
        else:

            codetocheck = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            proxycount += 1
            if proxycount > proxylength - 2:
                proxycount = 0

            checkcode(codetocheck, proxies[proxycount])
            # randomcode


def checkcode(code, proxy):
    global goodcoeds, codeschecked

    proxy2 = {
        'http': 'https://{}'.format(proxy),
        'https': 'http://{}'.format(proxy)
    }
    try:
        sendrequest = requests.session().get(
            "https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true".format(
                code), proxies=proxy2)
        #print(sendrequest.text)
        if sendrequest.status_code == 200:
            goodcoeds += 1
            filetowrite = open("Valid Codes.txt", "a")
            filetowrite.writelines("https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true".format(code))
            filetowrite.close()
        else:
            if "Unknown Gift Code" in sendrequest.text:
                codeschecked += 1




    except Exception as e:

        pass


def getrs():
    global codeschecked
    while not kill:


        try:
            oldint = codeschecked
            time.sleep(1)
            rs = codeschecked - oldint
            print(colored("Invalid [{}] | ".format(codeschecked), "red"),
                  colored("Threads: [{}] | ".format(rs), "cyan"), colored("Claimed: [{}]".format(goodcoeds), "green"),
                  end="\r")
        except Exception as e:
            print()


print(colored("""


              ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
              ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
              ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
              ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
              ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
              ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                                              Dev: Flex#8629



""", "blue"))


print(Fore.RED + "Enter Threads: " + Fore.RESET + Fore.GREEN, end="")
threadscount = input("")
threadss = int(threadscount)
if threadss > 300:
    threadss = 300
for i in range(threadss):
    x = threading.Thread(target=starting)
    x.start()

x = threading.Thread(target=getrs)
x.start()
