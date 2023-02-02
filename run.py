import gspread # to use google sheets
from google.oauth2.service_account import Credentials
import datetime # to check age
import math # to check decimal
import sys # to exit the program
import time # to add pauses
from os import system # to clear terminal

# Defines the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Adds credentials to the account and authorises the client sheet.
Code taken from Love Sandwiches.
"""
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("office-work")

# A greeting, instruction on what to do next
print("Hello, we are a recently opened bank,") 
print("thank you for starting your career with us.")
print("Your next step is to add yourself as an employee to our system.\n")

def clear():
    """
    Clears the terminal
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    system('clear')

def wait():
    """
    Adds pause before going on.
    https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
    """
    time.sleep(2.5)

def update_worksheet(data, worksheet):
    """
    Updates worksheet.
    Code taken from Love Sandwiches
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)

while True:
    try:
        """ 
        Asks for first name, checks for length, the input not being a number or null.
        Raises ValueError if input isn't valid.
        """
        first_name = input("\nPlease enter your first name(maximum 20 characters):\n")
        cap_first_name = first_name.capitalize()
        if len(first_name) < 1 or len(first_name) > 20 or first_name.isnumeric():
            raise ValueError
        break
    except ValueError:
        print("Please enter your first name, maximum 20 characters.")

while True:
    try:
        """ 
        Asks for first name, checks for length, the input not being a number or null.
        Raises ValueError if input isn't valid.
        """
        last_name = input("\nPlease enter your last name(maximum 20 characters):\n")
        cap_last_name = last_name.capitalize()
        if len(last_name) < 1 or len(last_name) > 20 or last_name.isnumeric():
            raise ValueError
        break
    except ValueError:
        print("Please enter your last name, maximum 20 characters.")

while True:
    try:
        """
        Asks for birth day, checks for input being a number between 1 and 31.
        If it's lower, higher, null or a string, raises ValueError.
        """
        age_day = int(input("\nPlease enter the day you were born:\n"))
        if age_day > 31 or age_day < 1:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and cannot be greater than 31.')

while True:
    try:
        """
        Asks for birth month, checks for input being a number between 1 and 12.
        If input is lower, higher, null or a string, raises ValueError.
        """
        age_month = int(input("\nPlease enter the month you were born:\n"))
        if age_month > 12 or age_month < 1:
            raise ValueError
        elif age_month == 2 and age_day > 29:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and must be between 1 and 12.')

while True:
    try:
        """
        Asks for birth year, calculates age of an employee.
        Checks for it to be between 18 and 80.
        If it's not, raises ValueError.
        If it is, updates birthday worksheet.
        """
        age_year = int(input("\nPlease enter the year you were born:\n"))
        date_of_birth = datetime.datetime(age_year, age_month, age_day)
        age = (datetime.datetime.now() - date_of_birth)
        days = int(age.days)
        converted_years = days/365
        employee_age = int(converted_years)
        if employee_age >= 18 and employee_age < 80:
            employee_birthday = cap_first_name + "," + cap_last_name + "," + str(age_day) + "," + str(age_month)
            employee_birthday = employee_birthday.split(",")
            employee_birthday_for_ws = [i.strip() for i in employee_birthday]
            update_worksheet(employee_birthday_for_ws, "Birthday")
        else:
            raise ValueError
        break
    except ValueError:
        print('Please try again, your age should be between 18 and 80.')

while True:
    try:
        """
        Asks for a role. Checks for length and input being a number or null.
        If data is valid, it is added to employees worksheet.
        If it isn't, raises a ValueError.
        """
        employee_role = input("\nPlease enter your job role(maximum 20 characters):\n")
        cap_employee_role = employee_role.capitalize()
        if len(employee_role) < 1 or len(employee_role) > 20 or employee_role.isnumeric():
            raise ValueError
        elif len(employee_role) > 1:
            employee_data = cap_first_name + "," + cap_last_name + "," + cap_employee_role
            employee_data = employee_data.split(",")
            employee_data_for_ws = [i.strip() for i in employee_data]
            update_worksheet(employee_data_for_ws, "Employees")
            print("\nThank you, the data provided is valid and is now added to our database.\n")
        break
    except ValueError:
        print("Please try again, your job role should be 20 characters maximum.")

def give_options():
    """
    Asks user what they want to do, checks user input to be a number between 1 and 4.
    If it is, clears terminal, waits a bit and does what the user chose.
    If it's not, raises ValueError.
    """
    print("\nWhat would you like to do?\n1. Request a day off.\n2. See your collegues' birthdays.\n3. See your collegues' names and roles.\n4. Exit.")
    while True:
        try:
            global user_input
            user_input = int(input("Please enter a number:\n"))
            if user_input >= 1 and user_input <= 4:
                print("\nPlease wait, we are processing your request...\n")
                wait()
                clear()
            elif user_input < 1 or user_input > 4:
                raise ValueError
            break
        except ValueError:
            print("\nPlease try again, enter a number between 1 and 4.\n")
    return user_input
    clear()
    wait()

def request_a_day_off(cap_first_name, cap_last_name):
    """
    Asks for starting and ending date and a reason for a day off. 
    If the data is valid, request a day off worksheet is updated, 
    waits a bit and asks what user wants to do next.
    """
    print("You are currently requesting a day off. We will need you to provide starting and ending date, and a reason.\n")
    while True:
        user_name = "Your name is " + cap_first_name + " " + cap_last_name + "."
        print(user_name)
        try:
            """
            Asks for starting date.
            If it's lower than 01.01, higher than 31.12, is integer,
            numbers after comma are higher than 12 and if there are 
            more than 2 numbers after comma, raises a ValueError.
            """
            starting_date = float(input("\nPlease enter a starting date (For example: 01.02):\n"))
            whole = math.floor(starting_date)
            frac = starting_date - whole
            needed_decimal = '0.23'
            if starting_date > 31.12 or starting_date < 01.01 or starting_date.is_integer() or frac > 0.12 or len(needed_decimal) > len(str(starting_date)):
                raise ValueError
            break
        except ValueError:
            print("Please try again, provide it like this: 01.02\n")
    while True:
        try:
            """
            Asks for ending date.
            If it's lower than 01.01, higher than 31.12, is integer,
            numbers after comma are higher than 12 or there are 
            more than 2 numbers after comma, raises a ValueError.
            """
            ending_date = float(input("\nPlease enter an ending date (For example: 01.02):\n"))
            whole_two = math.floor(ending_date)
            frac_two = ending_date - whole_two
            if ending_date > 31.12 or ending_date < 01.01 or ending_date.is_integer() or frac_two > 0.12 or len(needed_decimal) > len(str(ending_date)):
                raise ValueError
            break
        except ValueError:
            print("Please try again, provide it like this: 01.02")
    while True:
        try:
            """
            Asks for a reason.
            If it's length is higher than 25 or null, or if it's a number, raises ValueError.
            Otherwise, updates day off requests worksheet and thanks the user.
            """
            user_reason = input("\nPlease provide a reason (maximum 25 characters):\n")
            if len(user_reason) > 25 or len(user_reason) < 1 or user_reason.isnumeric():
                raise ValueError
            else:
                request_data = cap_first_name + "," + cap_last_name + "," + str(starting_date) + "," + str(ending_date) + "," + user_reason
                request_data = request_data.split(",")
                request_data_for_sw = [i.strip() for i in request_data]
                update_worksheet(request_data_for_sw, "Day Off Requests")
                print("\nThank you, data provided is valid and was added to our database.\n")
            break
        except ValueError:
            print("Please provide a reason, maximum 25 characters. You can write a number as long as it's not at the beginning.")
    wait()
    give_options()

def see_birthdays():
    """
    Prints out employees' names and birthdays. 
    Then waits and asks the user what they want to do.
    """
    birthdays = SHEET.worksheet("Birthday").get_all_values()
    for row in birthdays:
        first_name_birthday = row[0]
        last_name_birthday = row[1]
        age_day_birthday = row[2]
        age_month_birthday = row[3]
        employees_birthday = last_name_birthday + ", " + first_name_birthday + ": " + age_day_birthday + "." + age_month_birthday
        print(employees_birthday)
    wait()
    give_options()


def see_roles():
    """
    Prints out employees and their roles.
    Then waits and asks the user what they want to do.
    """
    employees = SHEET.worksheet("Employees").get_all_values()
    for row in employees:
        employee_fname = row[0]
        employee_lname = row[1]
        role = row[2]
        data_to_print = employee_lname + ", " + employee_fname + " - " + role
        print(data_to_print)
    wait()
    give_options()

def main(cap_first_name, cap_last_name):
    """
    Main function which calls other functions
    based on user input.
    """
    give_options()
    if user_input == 1:
        request_a_day_off(cap_first_name, cap_last_name)
    if user_input == 2:
        see_birthdays()
    if user_input == 3:
        see_roles()
    if user_input == 4:
        clear()
        sys.exit("You have exited the program. Thank you!")

# Calling the main function
main(cap_first_name, cap_last_name)