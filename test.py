"""str="Mike Acosta"
print(str[:])
print(str[2:])
print(str[::-1])
print(str[1:7:2])
print(str[-6:-10:-2])
"""
#reverseg
"""for t in range(1,10):
    for i in range(10,t-1,-1):
        print(f"{t}", end=" ")
    print()"""

#outer loop
"""for x in range(1,6):
    for y in range(6,11):
        print(f"{x}{y}", end=" ")
    print()"""

#conditional nested looping
"""input = int(input())
for x in range(0, input+1):
    for y in range(1, input+1):
        if x % 2 == 0:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()"""
#optional
"""while (True):
    print("Enter number: ")
    z=int(input())
    if z<=0:
        break"""
#kalimutan ko ano to
"""print("Enter string: ")
str=input()

for z in str:
    print(z)

for z in range(len(str)):
    print(str[z])"""

#using switch case
"""while(True):
    print("Enter String: ")
    str = input().lower()
    vowel = ['a','e','i','o','u']
    for z in range(len(str)):
        letter = str[z]
        match str[z]:
            case "a":
                print(f"{letter} = Vowel")
                print()
            case "e":
                print(f"{letter} = Vowel")
                print()
            case "i":
                print(f"{letter} = Vowel")
                print()
            case "o":
                print(f"{letter} = Vowel")
                print()
            case "u":
                print(f"{letter} = Vowel")
                print()
            case _:
                print(f"{letter} = consonant")
                print()"""


"""while True:
    text = input("Enter String: ").lower()
    vowels = ["a","e","i","o","u"]

    for letter in text:
        if letter.isalpha():  # check only letters
            if letter in vowels:
                print(f"{letter} = Vowel\n")
            else:
                print(f"{letter} = Consonant\n")"""

# Write a program that asks the user to enter their full name.
# Print the first 3 letters.
# Print the last 3 letters.
# Print the name in reverse.
# Print every 2nd character in the name.

"""name = input("Enter your name: ")

print(name[:3])
print(name[-3:])
print(name[::-1])
print(name[2::2])"""

# 2. Nested loops
# Print a multiplication table from 1 to 5.

    #static
"""for x in range(1,6):
    for y in range(1,6):
        print(f"{x}x{y}={x*y}", end=" ")
    print()"""

    #Dynamic
"""number =int(input("Enter Table size: "))
for x in range(1,number+1):
    for y in range(1,number+1):
        print(f"{x}x{y}={x*y}", end=" ")
    print()"""

# 3. Conditional nested looping
# Ask the user for a number n.
# Even rows = *
# Odd rows = 0

"""input = int(input())
for x in range(0, input+1):
    for y in range(1, input+1):
        if x % 2 == 0:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()"""

"""random =print([1,2,3,4,5,6,7,8,9,10])
for x in range(1, random+1):
    for y in range(1, random+1):
        print(f"{x}" end=" ")
    print()"""

"""import random
tries = 0
life = input("Number of Try: ")
life = int(life)
num = random.randint(1,20)
while True:
     guess = input("Enter A number: ")
     guess = int(guess)
     if num == guess:
          print("===== [ CONGRATS NAK ]=====")
          print(f"Life Remaining: {life}")
          break
     elif life == 0:
          print("TANGA AMPOTA UBOS NA BUHAY MO BOBO")
     elif num<guess:
          life -= 1
          print("TOO HIGH")
          print(f"Life Remaining: {life}")
     elif num>guess:
          life -= 1
          print("TOO LOW")
          print(f"Life Remaining: {life}")
     else:
          life -= 1
          print(f"")
          print(f"Life Remaining: {life}")"""



"""import random
num = random.randint(5,15)
while True:
    guess = input("enter guess number: ") 
    guess = int(guess)

    if num == guess:
        for i in range(guess,):
            for space in range(guess-i):
                print("*", end='') 
            print()
        print("your right!")
    else:
        print("mali po")"""

"""for t in range(1,10):
    for i in range(10,t-1,-1):
        print(f" ", end=" * ")
    print()"""

"""rows = input("Enter row: ")
rows = int(rows)

for i in range(rows):
    for space in range(rows-i):
        print(" ", end='')
    for star in range(i):
        print("*", end=' ')
    print()"""