words = open('words.txt',encoding='ascii').read().upper().split()


def step(word):
    for aWord in words:
        for letter in aWord: 
            if checkLetters(word,letter):
                aWord.replace(letter,"")
                continue
            else:
                break
    return aWord
            


def checkLetters(word,letter):
    i = 0 
    while i < len(word):
        if letter == word[i]:
            return True
        return False





print(step("apple"))




