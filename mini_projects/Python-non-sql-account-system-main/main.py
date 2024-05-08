import numpy as np

accountinfo =  np.array([["Juan", "John", "Quan", "Game"],
                         ["pass","hello","joke", "lame"],
                         ["bigg", "bigg", "bigg", "bigg"]], 
                        dtype=str) # do not actually use this for accounts. bigg is a subsitute for uuids
user = input("Enter username (Case Sensitive): ")
passw = input("Enter password (Case Sensitive): ")
y=0 #this will help find what row the user is in
for x in accountinfo[0]: #goes through rows
    if x == user: #x is the string in the certain row its at
        if accountinfo[1,y] == passw and accountinfo[2,y] == "bigg": #y is the row, 1 and 2 are always the same since there will only ever be 3 columns
            print("user, pass, and HWID is correct")
            quit() #do whatever you want here when they log in
    else:
        y=y+1 #add to the row, follows x
else:
    print("username, password, or HWID was incorrect") #if it's not correct then it will print here
    quit()
#hope this is easy to understand


