"""This module consists of functions displaying menu"""
from os import system

def mainmenu():
    """This function prints main menu"""
    system("cls")
    with open("Graphics\\Hangman_emote.txt", "r") as hangmanpicture:
        for line in hangmanpicture:
            print(line, end='')
        hangmanpicture.close()
    print("\n 1.Play")
    print(" 2.Leaderboard")
    print(" 3.Quit")