from termcolor import colored as cl
from os import system as SYS
from random import choice as lchoi, randint as rint
from time import sleep as sl

SYS("color")
SYS("cls")

userbase = {
    "cardnum":{
        "0123 4567 8910 1112":{
            "name":"Charming",
            "sex":"m",
            "age":"18",
            "balance":10000
        },
        "2111 0198 7654 3210":{
            "name":"Cinderella",
            "sex":"f",
            "age":"18",
            "balance":10000
        }
    }
}

symbols = ["❥", "ꕥ", "♡", "✎", "☄", "✥"]

def generateline():
    line = []
    symbol1 = lchoi(symbols)
    symbol2 = lchoi(symbols)
    symbol3 = lchoi(symbols)
    line.append(symbol1)
    line.append(symbol2)
    line.append(symbol3)
    matchcount = 0
    for i in line:
        v = i
        line.remove(i)
        for n in line:
            if i == n:
                matchcount += 1
                line.remove(n)
        line.append(v)
    line.clear()
    line.append(symbol1)
    line.append(symbol2)
    line.append(symbol3)
    if matchcount == 0:
        sysmsg(str(line))
        breakln()
        #Loss
    elif matchcount == 1:
        sysmsg(str(line))
        breakln()
        #2x Win
    elif matchcount == 2:
        sysmsg(str(line))
        breakln()
        #3x Win
    else:
        sysmsg("huh?")
    return matchcount

def readline():
    matchcount = generateline()

    if matchcount == 0:
        sysmsg("LOSS!")
        return 0
    elif matchcount == 1:
        sysmsg("2x WIN!")
        return 1
    elif matchcount == 2:
        sysmsg("3x WIN!")
        return 2
    else:
        sysmsg("Broken")
        return 3

def sysmsg(str):
    print(cl("SLOT MACHINE:", "white", "on_green", attrs=["bold"]) + " " + str)

def sysreq(str):
    op = input(cl("SLOT MACHINE:", "white", "on_green", attrs=["bold"]) + " " + str + "?\n" + cl("USER:", "white", "on_yellow", attrs=["bold"]) + " ")
    return op

def account_inpt_verify(str):
    splstr = str.split()
    verify_count = 0
    for n in splstr:
        if n.isnumeric() == True:
            verify_count += 1
    if verify_count == 4:
        return True
    else:
        return False

def breakln():
    print(" ")


sysmsg("Hello! Welcome to the Slot Machines!")

breakln()

conf_acc = False
inptacc = ""
while conf_acc == False:
    inptacc = sysreq("Please enter the account number (Format: XXXX XXXX XXXX XXXX)")
    breakln()
    inptacc_conf = sysreq(str("Is this correct? (" + inptacc + ") (Type 'yes' to confirm)"))
    if inptacc_conf == "yes":
        ver_acc = account_inpt_verify(inptacc)
        if ver_acc == True:
            if str(inptacc) in userbase["cardnum"]:
                conf_acc = True
            else:
                breakln()
                sysmsg("This card number (" + inptacc + ") does not exist on our servers.")
                breakln()
        else:
            breakln()
            sysmsg("This card number (" + inptacc + ") was inputted incorrectly.")
            breakln()

userdetails = ((userbase["cardnum"])[str(inptacc)])

breakln()

sysmsg("Welcome back, " + str(userdetails["name"]) + ", we missed you!")

playinggame = True
currentbalance = float(str(userdetails["balance"]))
newbalance = currentbalance
while playinggame == True:
    sysmsg("You currently have $" + str(newbalance) + " in your account!")

    breakln()

    bettingamnt_conf = False
    bettingamnt = " "
    while bettingamnt_conf == False:
        bettingamnt_isnum = False
        while bettingamnt_isnum == False:
            bettingamnt = sysreq("How much would you like to bet?")
            if bettingamnt.isnumeric() == True:
                bettingamnt_isnum = True
        bettingamntconf = sysreq(str("You would like to bet $" + bettingamnt + " (Type 'yes' to confirm)"))
        if bettingamntconf == "yes":
            bettingamnt_conf = True

    breakln()

    sysmsg(str("The betting amount of $" + bettingamnt + " has been selected!"))

    SYS("cls")

    sysmsg("Generating your line!")

    sl(float(rint(1,5)/2))

    breakln()

    multiplier = readline()

    if multiplier == 0:
        newbalance = newbalance - float(bettingamnt)
    if multiplier == 1:
        newbalance = newbalance + (float(bettingamnt) * 2)
    if multiplier == 2:
        newbalance = newbalance + (float(bettingamnt) * 3)
    if multiplier == 3:
        sysmsg("BROKEN")

    sysmsg(str("Your new balance is: $" + str(newbalance) + "!"))
    
    breakln()

    stopplayingreq = sysreq("Would you like to stop playing? (Type 'yes' to confirm)")
    if stopplayingreq == "yes":
        playinggame = False