from Tkinter import *
import datetime

def greet_user():
    now = datetime.datetime.now()
    d = now.date()
    t = now.time()
    print "Hello today's date and time are: {}".format(now)
    select_branch(now) #call select_branch function and pass in the now variable

def select_branch(now):
    try:
        location = raw_input("Please enter a branch name to check avialability. (London, New York): ").lower()
    except:
        print("I'm sorry there is no information found for that city.")
        location = raw_input("Please enter a branch name to check avialability. (London, New York): ").lower()

    if location == 'london':
        london_branch(now)

    if location == 'new york':
        newYork_branch(now)
    else:
        print(" I am sorry but {} is not a valid selection.".format(location))

def london_branch(now):
    if now.time >= 17 and now.time <21:
        print 'The London branch is open!'
    else:
        print 'The London branch is currently closed.'

def newYork_branch(now):
    if now.time >= 6 and now.time <18:
        print 'The New York branch is open!'
    else:
        print 'The New York branch is currently closed.'

if __name__ == "__main__":
    greet_user() #start with the greet_user function
        






