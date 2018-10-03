__author__ = "Bart Simpson" # A.J. DelCimmuto
__credits__ = ["Lisa Simpson", "Santa's Little Helper"] # No One
__email__ = "bs123@mail.uc.edu" # delcimaj@mail.uc.edu



words = open('words.txt',encoding='ascii').read().upper().split()


def step(word):
    answer = []
    for aWord in words:   #iterate through the list of words 

        saveWord = aWord  #save the word because the program edits the word to eliminate repeated characters

        letterCount = 0   #count the ammount of times a letter appears in a word

        for letter in word: #iterate through the letters of the input word

            if letter in aWord:    #check if letter is in a word in the list

                letterCount += 1      #count how many times the letters match        
                    
                aWord = aWord.replace(letter,'',1) #remove each letter that matches. This allows for multiple letter inputs such as "APPLE" (two P's)

            else:
           
                break
                

        if letterCount >= len(word) and len(saveWord) == len(word) + 1:
            
            answer.append(saveWord)  #add to list
                
    return answer
        


print(step("APPLE"))




