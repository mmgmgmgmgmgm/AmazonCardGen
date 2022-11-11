import ctypes
import os
import random
import string
import sys
import time

import pyfiglet
import requests
from colorama import Fore

print(f'''{Fore.BLUE}
▄▄▄      ▒███████▒  ██████  ▄████▄       ▄████ ▓█████  ███▄    █ 
▒████▄    ▒ ▒ ▒ ▄▀░▒██    ▒ ▒██▀ ▀█      ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██  ▀█▄  ░ ▒ ▄▀▒░ ░ ▓██▄   ▒▓█    ▄    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░██▄▄▄▄██   ▄▀▒   ░  ▒   ██▒▒▓▓▄ ▄██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
 ▓█   ▓██▒▒███████▒▒██████▒▒▒ ▓███▀ ░   ░▒▓███▀▒░▒████▒▒██░   ▓██░ -Close the window to shut down the program
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░ ░▒  ░ ░  ░  ▒        ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░   ▒   ░ ░ ░ ░ ░░  ░  ░  ░           ░ ░   ░    ░      ░   ░ ░ 
      ░  ░  ░ ░          ░  ░ ░               ░    ░  ░         ░ 
          ░                 ░                                        
Amazon Storecard Generator Made by: RebootedOrbit#0533, discord server: https://discord.gg/EsvpGV7vHv                       
                               ''')


print(f"{Fore.BLUE}[?][/] Enter to start generating.")
check2 = input(f'{Fore.RED}[?]>')

#60457811 - use this bin if you dong got another

BIN = check2

print(f"{Fore.BLUE}[/] Starting.")
time.sleep(3)
while True:

        cc = ('').join(random.choices(string.digits, k=8))


print(f"{Fore.GREEN}[>] {cc} is a valid Store Card!")
f = open("cards.txt",'a')
f.write(f"{card}\n")

                



