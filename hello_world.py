# simple python program to clear the windows terminal and print "Hello World" in color

# import the os module to later clear the screen
import os

# clear terminal screen
os.system("cls")

# set variables for colored letters
H = "\033[1;34mH\033[00m"  # makes a blue H
e = "\033[1;29me\033[00m"  # makes a light gray e
W = "\033[1;32mW\033[00m"  # makes a green W
o = "\033[1;33mo\033[00m"  # makes a yellow o
r = "\033[1;31mr\033[00m"  # makes a red r
l = "\033[1;36ml\033[00m"  # makes an aquamarine l
d = "\033[1;35md\033[00m"  # makes a violet d
ep = "\033[1;37m!\033[00m" # makes a white exclamation point

# display Hello World with World in color with clean line above and below
print(f"\n{H}{e}{l}{l}{o} {W}{o}{r}{l}{d}{ep}\n")