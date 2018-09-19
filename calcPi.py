import math



def check(piVal, guess, error):
    iterations = 0;
    while abs(piVal - guess) >= error:
        guess = guess + math.sin(guess)
        iterations += 1
    return iterations
    




def newtonian(piVal, Error):
    guess = 3
    iterations = 0
    while abs(piVal - guess) >= Error:
        guess = guess - (math.sin(guess) / math.cos(guess))
        iterations = iterations + 1
  
    return iterations


piValue = 3.141592653589793
guess = 3
Error = 0.000000000000001
print("Iterative method: ", check(piValue, guess, Error))
print("Newtonian method: ", newtonian(piValue, Error))
