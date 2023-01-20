#B0undle55
#Play_Game.py
#starts a runtime to utilize the individual functions
#
#
#

#importing the functions \\\thinking about migrating to one project at some point
import requests
import json
from Status_Check import status_check
from Account_Check import account_check
from Location_Check import location_check
from Marketplace_Check import marketplace_check
from Purchase_Script import purchase
from Flight_Plan_Check import flight_plan_check
from Flight_Plans_Choice import flight_plans_choice
from Sale_Script import sale
from Loan_Type_Check import loan_type_check
from My_Location import my_location
from Loan_Choice import loan_choice
from Ships_Type_Check import ships_type_check
from Ship_Choice import ship_choice
from Username_Claim import username_claim

#load personal token
token = input('What is your Account ID?: ')
shipID = ' '

#check game status
status_check()

#intro
print('Welcome to SpaceTraders')
print('\n')

#current location reminder
my_location(token)
print('\n')

#game loop
def play_game():
    
    #menu
    while True:
        print('1 - Check your account')
        print('2 - Search nearby planets')
        print('3 - Check the marketplace')
        print('4 - Make a purchase')
        print('5 - Create a flight plan')
        print('6 - Check a flight plan')
        print('7 - Make a sale')
        print('8 - Check available loans')
        print('9 - Check current locations')
        print('10 - Take out a loan')
        print('11 - Check available ships')
        print('12 - Purchase a ship')
        print('13 - Claim a new username')
        print('\n')
        choice = input('Enter the number for the menu item you wish to select (q to quit): ')
        print('\n')
        
        #switch
        if choice == 'q' or choice < '0' :
            print('goodbye!')
            break
        elif choice == '1':
            account_check(token)
            print('\n')
            
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
            shipID = input('What is your Ship ID?: ')
            print('\n')
            good = input('What good are you looking to purchase?: ')
            print('\n')
            quantity = input('How many?: ')
            print('\n')
            purchase(token, shipID, good, quantity)
            print('\n')
            
        elif choice == '5':
            shipID = input('What is your Ship ID?: ')
            print('\n')
            destination = input('Where would you like to fly?: ')
            print('\n')
            flight_plans_choice(token, shipID, destination)
            print('\n')
            
        elif choice == '6':
            flightID = input('What is the Flight ID?: ')
            print('\n')
            flight_plan_check(token, flightID)
            print('\n')
            
        elif choice == '7':
            shipID = input('What is your Ship ID?: ')
            print('\n')
            good = input('What good are you looking to sell?: ')
            print('\n')
            quantity = input('How many?: ')
            print('\n')
            sale(token, shipID, good, quantity)
            print('\n')
            
        elif choice == '8':
            print('\n')
            loan_type_check(token)
            print('\n')
            
        elif choice == '9':
            print('\n')
            my_location(token)
            print('\n')
            
        elif choice == '10':
            print('\n')
            loan = input('What type of loan are you looking to take out? ')
            loan_choice(token, loan)
            print('\n')
            
        elif choice == '11':
            print('\n')
            ship = input('What type of ship are you looking for? ')
            print('\n')
            ship_type_choice(token, ship)
            print('\n')
            
        elif choice == '12':
            print('\n')
            location = input('Where are you looking to purchase from? ')
            print('\n')
            ship = ('What ship did you want to purchase? ')
            print('\n')
            ship_choice(token, location, ship)
            print('\n')
            
        elif choice == '13':
            print('\n')
            username = input('What username do you want to claim? ')
            print('\n')
            username_claim(username)
            print('\n')
            
play_game()