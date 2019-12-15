"""That's where all magic happens"""
import sys
sys.path.insert(1, 'Modules')
import display
import menu
import msvcrt



loc = "mainmenu"
while True:
    display.printer(loc)
    print('')  # this print only exists so that the last line of a file is printed before select triggers
    select = str(msvcrt.getch(), "utf-8")
    loc = menu.menumenagement(loc, select)

