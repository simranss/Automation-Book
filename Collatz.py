#collatz function
def collatz(a):

    # even
    if a % 2 == 0:
        b = a // 2
        print(b)
        return b
    
    # odd
    elif a % 2 == 1:
        b = (3 * a) + 1
        print(b)
        return b

    else:
        return a


#Input the number
try:
    number = int(input("Enter a positive integer: "))

    if number > 0:
        c = number
        while True:
            c = collatz(c)
            if c == 1:
                break
    else:
        print("Enter a positive integer")
except ValueError:
    print("Enter an integer")

