"""This module consists of functions displaying menu"""
from os import system
import console_colors as cons
import sys


def printer(localization = "mainmenu"):
    """This functions prints the interface for the given location"""
    try:
        system("cls")
        with open("Graphics\\"+ localization +".txt", "r") as printer:
            for line in printer:
                print(line, end='')
            printer.close()
    except FileNotFoundError:  # this one is made for printing leaderboard
        system("cls")
        print("1.Back")
        with open(localization +".txt", "r") as printer:
            for line in printer:
                print(line, end='')
            printer.close()


def matchUI(strikes, word, valid, invalid, displayword = False, player = 0):
    """This function prints interface during the actual match"""
    system("cls")
    if player == 1:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_BLUE | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print(" " * 38, "PLAYER 1")
        cons.set_text_attr(default_colors)
    elif player == 2:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_YELLOW | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print(" " * 38, "PLAYER 2")
        cons.set_text_attr(default_colors)
    elif player == 3:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_YELLOW | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print(" " * 38, "COMPUTER")
        cons.set_text_attr(default_colors)
    if player == 0:
        with open("Graphics\\"+"strike"+str(strikes)+".txt", "r") as printer:
            for line in printer:
                print(" "*35 + line, end='')
        printer.close()
        print("\n")
    elif player == 1:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_BLUE | default_bg |
                           cons.FOREGROUND_INTENSITY)
        with open("Graphics\\"+"strike"+str(strikes)+".txt", "r") as printer:
            for line in printer:
                print(" "*35 + line, end='')
        printer.close()
        print("\n")
        cons.set_text_attr(default_colors)
    elif player == 2 or player == 3:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_YELLOW | default_bg |
                           cons.FOREGROUND_INTENSITY)
        with open("Graphics\\" + "strike" + str(strikes) + ".txt", "r") as printer:
            for line in printer:
                print(" " * 35 + line, end='')
        printer.close()
        print("\n")
        cons.set_text_attr(default_colors)


    if not displayword:
        print(" "*(37 - len(word)), end = '')
        for letter in word:
            if letter in valid:
                print(letter, end='  ')
            else:
                print("_", end='  ')
        print("\n")
    if displayword:
        print(" " * (37 - len(word)), end='')
        for letter in word:
            if letter in word:
                print(letter, end='  ')
        print("\n")

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countletter = 0
    countline = 0
    for letter in letters:
        if letter in valid:
            default_colors = cons.get_text_attr()
            default_bg = default_colors & 0x0070
            default_fg = default_colors & 0x0007
            cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                               cons.FOREGROUND_INTENSITY)
            if countline < 3:
                print(letter.rjust(10), end='')
                sys.stdout.flush()
            elif countline >= 3:
                print(letter.rjust(13), end='')
                sys.stdout.flush()
            cons.set_text_attr(default_colors)
        elif letter in invalid:
            default_colors = cons.get_text_attr()
            default_bg = default_colors & 0x0070
            default_fg = default_colors & 0x0007
            cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
            if countline < 3:
                print(letter.rjust(10), end='')
                sys.stdout.flush()
            elif countline >= 3:
                print(letter.rjust(13), end='')
                sys.stdout.flush()
            cons.set_text_attr(default_colors)
        else:
            if countline < 3:
                print(letter.rjust(10), end='')
                sys.stdout.flush()
            elif countline >= 3:
                print(letter.rjust(13), end='')
                sys.stdout.flush()
        countletter += 1
        if countletter == 7:
            print("\n")
            countline += 1
            countletter = 0
    print("\n")
    print("Press '1' if you want to leave to main. If you haven't finished the game your progress will be lost!")

def customwordsmenu(words1, words2):
    """"This function prints menu for custom game settings"""
    printer("hangmanemote")
    print("1.", end = '')
    sys.stdout.flush()
    if words1:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("Include", end = '')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print("/", end ='')
        sys.stdout.flush()
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("exclude", end = '')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print(" base words")

    elif not words1:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("Include", end='')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print("/", end = '')
        sys.stdout.flush()
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("exclude", end = '')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print(" base words")
    print("2.", end='')
    sys.stdout.flush()
    if words2:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("Include", end='')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print("/", end='')
        sys.stdout.flush()
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("exclude", end='')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print(" custom words")

    elif not words2:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("Include", end='')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print("/", end='')
        sys.stdout.flush()
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("exclude", end='')
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
        print(" custom words")
    print("3.Add custom words")
    print("4.Clear custom words(deletes all custom words ever given to the program")
    print("5.Done")


def customtimemenu(limit, display):
    """This function prints customtimemenu"""
    printer("hangmanemote")
    print("1.", end ='')
    sys.stdout.flush()
    if limit:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("Time limit")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    elif not limit:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("Time limit")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    print("2.", end = '')
    sys.stdout.flush()
    if display:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("Time display")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    if not display:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("Time display")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    print("3.Done")


def customtimelimit(time, limit):
    """This functions prints screen of enabling and modifying time limit"""
    printer("hangmanemote")
    print("1.", end='')
    sys.stdout.flush()
    if not time:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("Time limit")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    elif time:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("Time limit")
        sys.stdout.flush()
        cons.set_text_attr(default_colors)
    print("2.Limit:", limit)
    print("3.Done")


