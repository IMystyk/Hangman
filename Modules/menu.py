"""This module menages user's choices in menu"""
import sys
import match
import msvcrt
import display
import time
import os

def menumenagement(loc = "mainmenu", choice = ""):
    """This function manages user interactions with interface"""
    localization = loc
    if loc == "mainmenu":
        if choice == "1":
            localization = "gamemode"
        elif choice == "2":
            localization = "leaderboard"
        elif choice == "3":
            gamequit()
            return localization
        else:
            return loc
    elif loc == "gamemode":
        if choice == "1": # normal
            localization = "match"
            game = True
            while game:
                game = match.matchsetup()
            localization = "mainmenu"
        elif choice == "2": # competitive
            localization = "competitivenick"
        elif choice == "3":
            localization = "custommenu"
            custom_settings()
            localization = "mainmenu"
        elif choice == "4": # PvP - not even started on that one
            localization = "PvP"
            match.PvPmatch()
            localization = "mainmenu"
        elif choice == "5": # PvE
            localization = "difficultyselection"
        elif choice == "6": # back
            localization = "mainmenu"
        else:
            return localization
    elif loc == "difficultyselection":
        if choice == "1":
            match.PvPmatch(player2 = 3, difficulty = 'easy')
        elif choice == "2":
            match.PvPmatch(player2 = 3, difficulty = 'normal')
        elif choice == "3":
            match.PvPmatch(player2 = 3, difficulty = 'hard')
        elif choice == "4":
            match.PvPmatch(player2 = 3, difficulty = 'impossible')
        elif choice == "5":
            localization = "gamemode"
        else:
            return localization
    elif loc == "leaderboard":
        if choice == "1":
            localization ="mainmenu"
    elif loc == "competitivenick":
        nick = str(input())
        if len(nick) > 15:
            print("Your nick is too long. Enter a shorter one:")
            menumenagement(loc)
        elif len(nick) < 1:
            print("Your nick is too short. Enter a longer one:")
        game = True
        while game:
            game = match.matchsetup(timelimit = True, nick = nick)
        localization = "mainmenu"

    return localization


def gamequit():
    """This function quits the game (not the match)"""
    print("Are you sure u want to quit the game?")
    print("Press 'Y' for YES or 'N' for NO")
    leavemenu = str(msvcrt.getch(), "utf-8")

    if leavemenu == 'N' or leavemenu == 'n':
        return 0
    elif leavemenu == 'Y' or leavemenu == 'y':
        sys.exit(0)
    else:
        gamequit()


def custom_settings(loc = "custommenu"):
    """This function takes user's settings for the custom game"""
    basewords = True
    customwords = False
    timedisplay = True
    timelimit = False
    limit = 120
    while loc != "gamemode":
        display.printer(loc)
        print('')  # this print only exists so that last line of the file is printed before select triggers
        select = str(msvcrt.getch(), "utf-8")
        if select == "1":
            game = True
            while game:
                game = match.matchsetup(basewords, customwords, timedisplay, timelimit, limit)
            return 0
        elif select == "2":
            while select != '5':
                display.customwordsmenu(basewords, customwords)
                select = str(msvcrt.getch(), "utf-8")
                if select == "1":
                    basewords = not basewords
                elif select == "2":
                    customwords = not customwords
                elif select == "3":
                    while True:
                        display.printer("addingcustom")
                        nword = input()
                        if nword == "/back":
                            break
                        elif customwordcheck(nword):
                            try:
                                f = open("customwords.txt", "r")
                                f.close()
                                with open("customwords.txt", "a") as cwords:
                                    cwords.write("\n" + nword)
                                    cwords.close()
                            except FileNotFoundError:
                                with open("customwords.txt", "w") as cwords:
                                    cwords.write(nword)
                                    cwords.close()
                            print("New word has been successfully added")
                            time.sleep(2)
                        elif not customwordcheck(nword):
                            print("Given word doesn't fulfil the requirements")
                            time.sleep(2)
                elif select == "4":  # make confirmation for it
                    print("Press '4' again to confirm that you want to delete your custom words")
                    confirm = str(msvcrt.getch(), "utf-8")
                    if confirm == '4':
                        try:
                            f = open("customwords.txt", "r")
                            f.close()
                            os.remove("customwords.txt")
                            print("Custom words file has been cleared")
                            time.sleep(3)
                        except FileNotFoundError:
                            print("No custom words have been given yet")
                            time.sleep(3)
                else:
                    pass  # this pass is there on purpose
        elif select == "3":
            while True:
                display.customtimemenu(timelimit, timedisplay)
                select = str(msvcrt.getch(), "utf-8")
                if select == "1":
                    timelimit, limit = customtimelimit(timelimit, limit)
                elif select == "2":
                    timedisplay = not timedisplay
                elif select == "3":
                    break
                else:
                    pass
        elif select == "4":
            loc = "gamemode"
        else:
            pass

    return 0

def customwordcheck(word):
    """This function checks whether given word is allowed or not"""
    result = True
    if len(word) >= 3 and len(word) <= 15:
        result = True
    else:
        return False
    word = word.lower()
    for letter in word:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            return False
    else:
        result = True
    return result


def customtimelimit(time, limit):
    """This function allows player to change time limit settings"""
    while True:
        display.customtimelimit(time, limit)
        select = str(msvcrt.getch(), "utf-8")
        if select == "1":
            time = not time
        elif select == "2":
            print("Enter new time limit (in seconds)")
            limit = int(input())
        elif select == "3":
            return time, limit
        else:
            pass
