words = open('words.txt',encoding='ascii').read().upper().split()


def step(word):
    for aWord in words:    #iterate through the list of words 
        for letter in word:    #iterate through the letters of the 
            if checkLetters(aWord,letter) != -1:
                aWord.replace(i,"")
                continue
            else:
                break
    return aWord
            


def checkLetters(aWord,letter):
    i = 0 
    while i < len(aWord):
        if letter == aWord[i]:
            return i
        return -1




print(step("apple"))




