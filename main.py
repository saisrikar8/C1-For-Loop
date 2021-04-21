'''
HOMEWORK:

## Guessing Game 

In this assignment you will create a guessing game using user input, random, and conditional statements. 

You, the computer, will choose a random number between 1 and 10, then prompt the user to guess the number. Using the user's guess and comparing it to the computer's number, give the user feedback such as "Too high" or "Too low" or "You got it" 

*Ex* 

> Guess the number I'm thinking of: 9
  Sorry too high!

Code:
import random

ranNum = random.randint(1,10)
playNum = int(input("Enter a number (1 - 10):\n"))

#Equal

if(ranNum == playNum):
  print("You got it")

#ranNum is greater than playNum
elif(ranNum > playNum):
  print("Too Low")
  print("It was " + str(ranNum))

#ranNum is greater than playNum
elif(ranNum < playNum):
  print("Too High")
  print("It was " + str(ranNum))









Review:

While Loop:
>> Repeats body statement until the condition becomes false
>>When the condition is false, it runs the "else" header(this header is optional)

Format("else" header is optional):

while (CONDITION):
  BODY STATEMENT

else:
  BODY STATEMENT

Exercise:
# Expected output: 1x Python, 2x bye, 3x Evergreen, 4x 2021

student = 10

while(student > 0):
  if (student >= 11):
    print("hello")

  elif (student >= 10):
    print("Python")

  elif (student > 7):
    print("bye")

  elif(student >= 5):
    print("Evergreen")
  
  else:
    print(2021)

  student -= 1




Exercise:
  import random
  print("Level 1: 1 - 10\nLevel 2: 1 - 100\nLevel 3: 1 - 1000")
  level = int(input("Choose your level (1,2,3): Level "))
  ranNum = random.randint(1,10**level)
  playNum = int(input("Enter a number (1 -" + str(10**level) + "):\n"))

  while (ranNum != playNum):
    #ranNum is greater than playNum
    if (ranNum > playNum):
      print("Too Low")

    #ranNum is greater than playNum
    elif(ranNum < playNum):
      print("Too High")
    
    playNum = input("Enter a number (1 - " + str(10**level) + "):\n")
  else:
    #Equal
    print("You got it")
  desire = input("Do you want to keep playing?:\n")

This could also work:

import random
desire = "yes"

while (desire == "Yes" or desire == "yes"):
  print("Level 1: 1 - 10\nLevel 2: 1 - 100\nLevel 3: 1 - 1000")
  level = int(input("Choose your level (1,2,3): Level "))
  ranNum = random.randint(1,10**level)
  playNum = int(input("Enter a number (1 -" + str(10**level) + "):\n"))

  while (ranNum != playNum):
    #ranNum is greater than playNum
    if (ranNum > playNum):
      print("Too Low")

    #ranNum is greater than playNum
    elif(ranNum < playNum):
      print("Too High")
    
    playNum = input("Enter a number (1 - " + str(10**level) + "):\n")
  else:
    #Equal
    print("You got it")
  desire = input("Do you want to keep playing?:\n")



--------------------------------------------------------------------------------------------------------
  For Loop:
Repeats a set of statements a certain number of times

Formula:

for LCV(loop control variable) in Sequence:
  Body Statement

Loop Control Variable(LCV)
An ordinary int variable that is initialized, tested, and changed as the loop executes.

Sequence:
An iteration statement

a. range(#)
b. list, tuple, dictionary


# Example
#[0,1,2,3,4]
for n in range(5):
  print(n)


range() function:

1 argument: range(#) -> range(stop)
2 argument: range(#,#) -> range(start, stop)
3 arguments: rrange(#, #, #) -> range(start, stop, step)


#Example
range(4) # 0,1,2,3
range(3,8) # 3, 4, 5, 6, 7
range(1,13,3) #1, 4, 7, 10

'''