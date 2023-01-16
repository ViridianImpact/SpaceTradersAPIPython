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
from Location_Check import location_check
from My_Location import my_location
from Purchase_Script import purchase
from Marketplace_Check import marketplace_check
'''
from Sale_script import sale
from Flight_Plan_Check import flight_plan_check
from Flight_Plans_Choice import flight_plans_choice
from Loan_Choice import loan_choice
from Loan_Type_Check import loan_type_check
from Ship_Choice import ship_choice
from Ships_Type_Check import ships_type_check
'''
from Status_Check import status_check
'''
from Username_Claim import username_claim
'''

#my personal token
token = '4b0325e4-e972-4a4d-b67f-5cdd87d62f67'
shipID = 'clcwsbzgc107055215s63c83vr0d'

status_check()

print('Welcome to SpaceTraders')
print('\n')

my_location(token)
print('\n')

def play_game():
    while True:
        print('1 - Check your account')
        print('2 - Search nearby planets')
        print('3 - Check the marketplace')
        print('4 - Make a Purchase')
        print('9 - Check Current Locations')
        print('\n')
        choice = input('Enter the number for the menu item you wish to select (q to quit): ')
        
        if choice == 'q' or choice < '0' :
            print('goodbye!')
            break
        elif choice == '1':
            account_check(token)
        elif choice == '2':
            option = input('What type are you looking to filter on (type PLANETS or MOON): ')
            print('\n')
            location = input('What system do you want to search in?: ')
            print('\n')
            location_check(token, option, location)
            print('\n')
        elif choice == '3':
            location = input('What system do you want to search in?: ')
            print('\n')
            marketplace_check(token, location)
            print('\n')
        elif choice == '4':
            good = input('What good are you looking to purchase?: ')
            print('\n')
            quantity = input('How many?: ')
            print('\n')
            purchase(token, shipID, good, quantity)
        elif choice == '9':
            print('\n')
            my_location(token)
            print('\n')

play_game()