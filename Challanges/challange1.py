#################################################################
## This python file is for various coding challanges in python ##
#################################################################

#print ("Hello World")

#x = 5
#y = 7

#if(y > x):
    #print("Y is larger than X!")

#print(x + y)

#myString = "This is a string"
#fname = "Devin"
#lname = "Smith"

#print(myString)

#print(len(myString))

#print(myString[0])

#print("My name is {} {}, this is python!".format(fname, lname))

#print("My name is " + fname + " "  + lname)

#newName = fname.upper()

#print(newName)

#x **= 2

#print(x)

#if(x > 20 & y < 10):
    #print("This is [rinting because an and logical has been met!")

#print("Devin" in fname)

###############################
## This is pracricing tuples ##
###############################

#animal = ( "zebra", "alligator", "lion", "ox", "wolf")

#listofAnimals = list(animal)
#print(listofAnimals)

#testString = "Hello! I am pleased to meat you"
#newString = list(testString)
#print(newString)

#newString = testString.split()
#print(newString)

#print("This is printing out the tuple")
#for i in range(len(animal)):
    #print(animal[i])

#print("this is how many items are in the tuple")
#count = animal.count("wolf")
#print(count)

##############################
## This is pracricing lists ##
##############################

#myList = [2,3,4,5]
#list1 = [7,8,9,10]

#print("My list of ints will print.")
#for i in myList:
    #print(i)

#myList.append(6)

#print("This is my list with a 6 added to the end.")
#for i in myList:
    #print(i)

#myList.reverse()

#print("This is my list in reverse.")
#for i in myList:
    #print(i)

#newList = myList.copy()

#print("My is a copy of my list.")
#for i in newList:
    #print(i)

#for i in list1:
    #myList.append(i)

#print('This is two lists concatenated')
#for i in myList:
    #print(i)


#############################
## This is pracricing sets ##
#############################

#myset = {"wedge", "putter", "driver"}

#print(myset)

#myset.add("iron")

#print(myset)

#myset.remove("putter")

#print(myset)

#numSet1 = {1,2,3,4,5}

#numSet2 = {1,3,5,7,9}

#print(numSet1.difference(numSet2))
#print(numSet2.difference(numSet1))

######################################
## This is pracricing disctionaries ##
######################################


#################################
## This is pracricing modules ##
################################

#import datetime
#import random

#currentDate = datetime.datetime.now()

#print("The current dat and time is.")
#print(currentDate)

#print("this is a random number")
#print(random.randrange(1,100))


#####################################
## This is pracricing conditionals ##
#####################################

#num1 = 8

#if num1 == 10:
    #print("Num1 is equal to 10")

#elif num1 % 2 == 0:
    #print("Num1 is an even number")

#else:
    #print("Num1 is not equal to 10")

#string1 = "Loser"
#num2 = 5

#print(bool(string1))
#print(bool(num2))

##############################
## This is pracricing loops ##
##############################

#i = 0

#print("The following is a while loop")
#while i < 10:
    #i += 1
    #print("this is iteration numer {}".format(i))

    #if i == 5:
        #print("The loop has reached the 5ht iteration, it will now stop")
        #break

#print("The following is a for loop")
#for x in range(5):
    #print(x + 1)
    #if x == 2:
        #print("The loop has reached 3, it will now terminate")
        #break
    

#name = "Python"

#for i in enumerate(name):
    #print(i)

##################################
## This is pracricing functions ##
##################################

"""
def  myFunction():
    print("This fucntion was called")
    array = ["one", "two", "three", "four"]
    for i in array:
        print(i)

def getSum(num1, num2):
    answer = num1 + num2
    print("The answer is {}".format(answer))

print("I am about to call a function")
myFunction()

getSum(2,4)

getAdd = getSum(5,5)

"""


#######################################
## This is pracricing error handling ##
#######################################
"""
def readInfo():
    num1 = input("Pleaser enter a number: ")
    num2 = input("Please ener another number: ")
    compute(num1, num2)

def compute(num1, num2):
    try:
        num3 = int(num1) + int(num2)
        print("{} + {} = {}".format(num1, num2, num3))
    except:
        print("You did not enter an integer, try again!")
        readInfo()
readInfo()
"""

###########################################
## This is pracricing manipulating files ##
###########################################

import os
import time


path1 = "/"

dir_list1 = os.listdir(path1)

for i in dir_list1:
    print(i)


path2 = "/home"
print(os.path.join(path2, "devins/Desktop", "testfile.txt"))

path3 = "/home/devins/Desktop/testfile.txt"
mod_time1 = os.path.getmtime(path3)
local_time1 = time.ctime(mod_time1)

print("The last time the file was modified was {}".format(local_time1))

path4 = "/home/devins/Desktop/os_script"
dir_list2 = os.listdir(path4)
mod_time2 = os.path.getmtime(path4)
local_time2 = time.ctime(mod_time2)

for x in dir_list2:
    if x.endswith(".txt"):
        print("File Name: {} -- Mod Time: {}".format(x, local_time2))