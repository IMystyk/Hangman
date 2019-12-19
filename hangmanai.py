from operator import itemgetter
def chooseletter(correct, incorrect, length):
    """This function chooses letter for computer"""
    with open("hangmanwords.txt", "r") as words:
        wordsl = list(words)
        count = 0
        for x in range(0, len(wordsl)):
            if count == len(wordsl) - 1:
                       wordsl[x] = wordsl[x]
            else:
                wordsl[x] = wordsl[x][:-1]
            count += 1
        words.close()
    words1 = []
    words2 = []
    for word in wordsl:
        if len(word) == length:
            words1.append(word)
    del wordsl
    if len(incorrect) != 0:
        for word in words1:
            for letter in incorrect:
                if letter not in word:  # the problem is with adding same word every letter checked
                    if
                    words2.append(word)
                    break
        words1 = []
    else:
        words2 = words1
        words1 = []
    if len(correct) != 0:
        for word in words2:
            for letter in correct:
                if letter in word:
                    words1.append(word)
                    break
    else:
        words1 = words2
    letters = "abcdefghijklmnopqrstuvwxyz"  # this might not be needed, will see about it later
    letters = list(letters)
    for letter in correct:
        letters.remove(letter)
    for letter in incorrect:
        letters.remove(letter)
    results = []
    for letter in letters:
        count = 0
        for word in words1:
            if letter in word:
                count += 1
        results.append([letter, count])
    if len(incorrect) == 11:
        print('LOSE')
    results = sorted(results, key = itemgetter(1), reverse = True)
    
    print("Words:", len(words1))
    print(results)


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
chooseletter("", "et", len('drink'))
if checkword('drink', ''):
    print('WIN')


