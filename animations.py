import time
import platform    # Used by clear_screen
import subprocess  # Used by clear_screen
from time import sleep

# System independent clear screen function
# https://stackoverflow.com/questions/18937058/#42877403
def start_animations():
    def clear_screen():
        command = "cls" if platform.system().lower()=="windows" else "clear"
        return subprocess.call(command) == 0

    def smoke():
        # You could use the random package for a more realistic effect
        # https://docs.python.org/3/library/random.html

        shift = 15 + smoke.shift
        print(" "*(shift+2)+"(")
        print(" "*(shift  )+")")
        print(" "*(shift+2)+"(")
        print(" "*(shift  )+")")

        # Next shift using current direction
        smoke.shift += smoke.direction

        # Change direction if out of limits
        if smoke.shift>3 or smoke.shift<-2:
            smoke.direction *= -1

    def house():
        print("     __________| |____")
        print("    /                 \\")
        print("   /    Welcome to     \\")
        print("  /   MovieSchmmovie    \\")
        print("  |   By: Upasana T.    |")
        print("  |     ____     ___    |")
        print("  |    |    |   |___|   |")
        print("__|____|____|___________|__")
        print()

    # MAIN CODE

    smoke.shift = 0
    smoke.direction = 1 # could be 1 or -1


    # print('\033[2J') # One possible method to clear the screen
    clear_screen()

    # Infinite loop. Use CTR-C to stop
    start_time = time.time()
    while time.time() - start_time < 10:
        smoke()
        house()
        time.sleep(1)
        clear_screen()
   

# start_animations()
# importing the necessary packages
import time
import sys
import os
  
# Function for implementing the loading animation
def load_animation(load_str):
  
    # String to be displayed when the application is loading
    # load_str = "Welcome to the MovieSchmmovie"
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")

def bye_animations():
    def printByeRocket():
        print(
    """
             _
            /^\\
            |-|
            | |
            |B|
            |Y|
            |E|
            |!|
           /| |\\
          / | | \\
         |  | |  |
        `-\\"\\"\\"-`
    """)
        
    printByeRocket()
    
    delay = 300
    for i in range(60):
        print()
        sleep(delay/1000)
        delay = delay * 0.9


def hi_animations():
    def printHiRocket():
        print(
    """
             _
            /^\\
            |-|
            | |
            |H|
            |I|
            |!|
            | |
           /| |\\
          / | | \\
         |  | |  |
        `-\\"\\"\\"-`
    """)
        
    printHiRocket()
    
    delay = 300
    for i in range(60):
        print()
        sleep(delay/1000)
        delay = delay * 0.9




