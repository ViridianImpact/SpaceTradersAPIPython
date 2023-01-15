#B0undle55
#Play_Game.py
#starts a runtime to utilize the individual functions
#
#
#

#importing the functions \\\thinking about migrating to one project at some point
import requests
import json
from Account_Check import account_check

#my personal token
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'

def play_game():
    while True:
        print('Welcome to SpaceTraders')
        print('\n')
        print('1 - Check your account')
        print('\n')
        choice = input('Enter the number for the menu item you wish to select (q to quit): ')
        
        if choice == 'q':
            break
        elif choice == '1':
            account_check(token)