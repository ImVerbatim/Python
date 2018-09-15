#A.J. DelCimmuto
#HW #1




def printEgyptian(nr, dr):

    if dr == 0 or nr == 0:
        return

    if dr%nr == 0:
        print("1/", dr//nr)
        return
    if nr%dr == 0:
        print(nr // dr)
        return
    if nr > dr:
        print(nr // dr, " + ")
        printEgyptian(nr%dr,dr)
        return

    n = dr // nr + 1
    print("1/",n," + ")
    printEgyptian((nr*n-dr),(dr*n))


p = int(input("Enter a numerator: "))
q = int(input("Enter a denomenator: "))
print(p," / ", q, " = ")
printEgyptian(p,q)
