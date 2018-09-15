import math



def check(piVal, guess, error):
    iterations = 0;
    while abs(piVal - guess) >= error:
        guess = guess + math.sin(guess)
        iterations += 1
        print(guess)
    return iterations

def newtonian(piVal,Error):
    guess = 0
    while abs(piVal - guess) <= Error:
        if cos(guess) == -1

return



piValue = 3.141592653589793
guess = 3
Error = 0.000000000000001
print("Iterations: ", check(piValue, guess, Error))
