"""HWxx.py: Short Description of what the HWxx program does."""
__author__ = "A.J. Delcimmuto" # Your name
__credits__ = [""] # Your list of helpers
__email__ = "delcimaj@mail.uc.edu" # Your email address

"""Required questions for lab 1"""

## Boolean Operators ##

# Q4
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if x > 0 and y > 0:
        return True
    else:
        return False


## while Loops ##

# Q9
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    i = 1;
    while i <= n:
        if n % i == 0:
            print(i)
        i = i + 1


# Q10
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    curr = 0
    next = 1
    if n <= 1:
        curr = n
    else:     
        while n > 0:
            prev = curr
            curr = next
            next = curr + prev
            n -= 1
    return curr
    

    
    
    
