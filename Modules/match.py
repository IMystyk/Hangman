"""And here we finally get to play"""
from random import randint
import display
import msvcrt
import time
import console_colors as cons
from operator import itemgetter


def matchsetup(basewords = True, customwords = False, timedisplay = True, timelimit = False, limit = 120, nick = "", pvp = False, player = 0):
    """This function prepares the match and starts it when it's rdy"""
    if basewords and not customwords:
        with open("hangmanwords.txt", "r") as lottery:
            countLines = 0
            for line in lottery:
                countLines += 1
            index = randint(1, countLines)
            i = 1
            temp = ""
            lottery.seek(0)
            for line in lottery:
                if i == index:
                    temp = line
                i += 1
        lottery.close()
        winner = ""
        tlen = len(temp)-1
        count = 0
        if index < countLines:
            for letter in temp:
                if count == tlen:
                    break
                winner += letter
                count += 1
        elif index == countLines:
            winner = temp
    elif customwords and not basewords:
        try:
            with open("customwords.txt", "r") as lottery:
                countLines = 0
                for line in lottery:
                    countLines += 1
                index = randint(1, countLines)
                i = 1
                temp = ""
                lottery.seek(0)
                for line in lottery:
                    if i == index:
                        temp = line
                    i += 1
            lottery.close()
            winner = ""
            tlen = len(temp) - 1
            count = 0
            if index < countLines:
                for letter in temp:
                    if count == tlen:
                        break
                    winner += letter
                    count += 1
            elif index == countLines:
                winner = temp
        except FileNotFoundError:
            print("\nNo custom words have been given to the program! Returning to main menu")
            time.sleep(4.5)
            return False
    elif basewords and customwords:  # try to do this with temporary file
        with open("hangmanwords.txt", "r") as lottery:
            countLinesb = 0
            blines = []
            for line in lottery:
                countLinesb += 1
                blines.append(line)
            lottery.close()
        try:
            clines = []
            with open("customwords.txt", "r") as lottery:
                countLinesc = 0
                for line in lottery:
                    countLinesc += 1
                    clines.append(line)
                lottery.close()
        except FileNotFoundError:
            pass
        lines = blines + clines
        index = randint(0, len(lines)-1)
        temp = lines[index]
        winner = ""
        tlen = len(temp) - 1
        count = 0
        if index < len(lines) - 1:
            for letter in temp:
                if count == tlen:
                    break
                winner += letter
                count += 1
        elif index == len(lines) - 1:
            winner = temp
    elif not basewords and not customwords:
        print("\nNo words have been given to the program! Returning to main menu")
        time.sleep(4.5)
        return False

    winner = winner.upper()
    if pvp:
        return match(winner, timedisplay, timelimit, limit, nick, pvp, player = player)
    return match(winner, timedisplay, timelimit, limit, nick)


def checkletter(word, char):
    """This function checks whether given character is in the word"""
    correct = False
    for letter in word:
        if char == letter:
            correct = True
            break
    return correct

def checkword(word, correct):
    """This function checks whether player has already guessed the word"""
    win = False
    wordl = list(word)
    for letter in wordl:
        if letter in correct:
            win = True
        else:
            win = False
            break

    return win


def score(nick, time, strikes):
    """This function calculates player's score and saves it to the leaderboard"""
    score = 100000//(time*0.5) - strikes * 900
    currentplayer = [1, nick, str(time)+"s", str(strikes), str(score)]
    playerlistr = []
    try:
        with open("leaderboard.txt", "r") as referee:
            for line in referee:
                playerlistr.append(line.split())
            playerlistr[0] = currentplayer
        referee.close()
    except (FileNotFoundError, IndexError):
        playerlistr.append(currentplayer)
    finally:
        with open("leaderboard.txt", "w") as referee:
            playerlistw = sorted(playerlistr, key=itemgetter(4), reverse = True)
            count = 1
            referee.write("Place".rjust(5) + "Player".rjust(15)+"Time".rjust(8) + "Strikes".rjust(9) + "Score".rjust(9) + "\n")
            for player in playerlistw:
                referee.write(str(count).rjust(5) + player[1].rjust(15) + player[2].rjust(8) + player[3].rjust(9) + player[4].rjust(9))
                count += 1
                if count <= len(playerlistw):
                    referee.write("\n")
        referee.close()

    return score


def matchquit():
    """This function allows player to quit a match without closing the program"""
    print("Press '1' again if you want to quit to main menu. Your progress will not be saved")
    leavematch = str(msvcrt.getch(), "utf-8")

    if leavematch == '1':
        return True
    else:
        return False


def match(word, timedisplay, timelimit, limit, nick, pvp = False, player = 0, st = 0, cor = "", incor = "", ptime = 0):
    """This function menages the match"""
    strikes = st
    correct = cor
    incorrect = incor
    result = ""
    start_time = time.time()
    nextgame = True
    while strikes < 11:
        miss = 1
        display.matchUI(strikes, word, correct, incorrect, player = player)
        if checkword(word, correct):
            break
        guess = str(msvcrt.getch(), "utf-8")
        if timelimit and time.time() - start_time >= limit:
            break
        if guess == '1':
            if matchquit():
                nextgame = False
                break
        guess = guess.upper()
        if guess not in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            continue
        if checkletter(word, guess) and guess not in correct:
            correct += guess
            miss = 0
        elif not checkletter(word, guess) and guess not in incorrect:
            incorrect += guess
            strikes += 1
            miss = 0
            if strikes == 11:
                break
        if pvp:
            if miss:
                continue
            gametime = ptime + time.time() - start_time
            display.matchUI(strikes, word, correct, incorrect, player=player)
            time.sleep(1)
            if checkword(word, correct):
                break
            return word, timedisplay, timelimit, limit, nick, pvp, player, strikes, correct, incorrect, gametime, False
    if not nextgame and not pvp:
        return nextgame
    if not pvp:
        finaltime = time.time() - start_time
        finaltime = round(finaltime, 2)
    if pvp:
        finaltime = time.time() - start_time + ptime
        finaltime = round(finaltime, 2)
    if pvp and not nextgame:
        return word, timedisplay, timelimit, limit, nick, pvp, player, strikes, correct, incorrect, finaltime, True, True
    if strikes == 11:
        display.matchUI(strikes, word, correct, incorrect, True, player = player)
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("\n")
        print(" " * 35, "U LOST :(")
        print("\n")
        cons.set_text_attr(default_colors)
    elif checkword(word, correct):
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg |
                           cons.FOREGROUND_INTENSITY)
        print("\n")
        print(" " * 35, "U WON :)")
        print("\n")
        cons.set_text_attr(default_colors)
        result = "win"
    elif timelimit and finaltime >= limit:
        display.matchUI(strikes, word, correct, incorrect, True, player = player)
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        default_fg = default_colors & 0x0007
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg)
        print("\n")
        print(" " * 35, "U LOST :(")
        print("\n")
        cons.set_text_attr(default_colors)
        print("U ran out of time!")
        print("\n")
    if timedisplay:
        print("Your time was %d minutes and %.2f seconds" %(int(finaltime//60), finaltime%60))
    if nick != "" and result == "win":
        print("Your score is:", score(nick, finaltime, strikes))
    print("\nPress enter to start next match")
    input()
    if pvp:
        return word, timedisplay, timelimit, limit, nick, pvp, player, strikes, correct, incorrect, finaltime, True, False
    return nextgame

class PvP:

    def __init__(self, word, timedisplay, timelimit, limit, nick, pvp, player, strikes, correct, incorrect, gametime):
        self.word = word
        self.timedisplay = timedisplay
        self.timelimit = timelimit
        self.limit = limit
        self.nick = nick
        self.pvp = pvp
        self.player = player
        self.strikes = strikes
        self.correct = correct
        self.incorrect = incorrect
        self.gametime = gametime
    def read(self):
        return match(self.word, self.timedisplay, self.timelimit, self.limit, self.nick, self.pvp, self.player, self.strikes, self.correct, self.incorrect, self.gametime)


def PvPmatch():
    """This function menages PvP match.
     I am completely aware that I use list as well as class which makes it only more complicated,
     but I just rly wanted to use class"""
    while True:
        temp1 = list(matchsetup(pvp = True, player = 1))
        match1 = PvP(temp1[0], temp1[1], temp1[2], temp1[3], temp1[4], temp1[5], temp1[6], temp1[7], temp1[8], temp1[9], temp1[10])
        temp2 = list(matchsetup(pvp = True, player = 2))
        match2 = PvP(temp2[0], temp2[1], temp2[2], temp2[3], temp2[4], temp2[5], temp2[6], temp2[7], temp2[8], temp2[9], temp2[10])

        while True:
            match1 = PvP(temp1[0], temp1[1], temp1[2], temp1[3], temp1[4], temp1[5], temp1[6], temp1[7], temp1[8], temp1[9], temp1[10])
            temp1 = list(match1.read())
            if temp1[11]:
                break
            temp2 = list(match2.read())
            match2 = PvP(temp2[0], temp2[1], temp2[2], temp2[3], temp2[4], temp2[5], temp2[6], temp2[7], temp2[8], temp2[9], temp2[10])
            if temp2[11]:
                break
        try:
            if temp1[12]:
                break
        except IndexError:
            if temp2[12]:
                break



