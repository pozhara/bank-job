import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("office-work")

employees = SHEET.worksheet("Employees")

def description():
    print("Hello, we are a recently opened bank, thank you for starting your career with us. Your next step is add yourself as an employee to our system.\n")

def get_user_input():
    while True:
        print("What would you like to do?\n1. Add youself as an employee\n2. Request a time off\n3. See everyone's birthdays\n4. See everyone's names and roles")
        print("Please enter a letter below to choose and hit ENTER.")
        choice = input()
        try:
            global user_choice
            user_choice = int(choice)
            if user_choice > 3 or user_choice < 1:
                print("Please enter a valid number\n")
            if choice is str():
                print("Please enter a valid number\n")
            print("We are processing your request...\n")
            return user_choice
            break
        except ValueError:
            print("Please enter a valid number\n")
            break

def add_employee():
    print("We will need you to provide your first and last name, date of birth and role. Please note that you can write maximum 20 characters and your age should be above 18.")
    first_name = input("Please enter your first name: ")
    print(first_name)
    last_name = input("Please enter your last name: ")
    print(last_name)
    age_day = int(input("Please enter your birth day: "))
    print(age_day)
    age_month = int(input("Please enter your birth month's number: "))
    print(age_month)
    age_year = int(input("Please enter your birth year: "))
    print(age_year)

    if check_string(first_name) and check_string(last_name) and check_birth(age_day, age_month, age_year):
        print("Thank you, the data you provided is valid. It is now added to our database.\n")

def check_birth(age_day, age_month, age_year):
    while True:
        try:
            if age_day > 32 or age_day < 0:
                print("Invalid data, birth day should be between 1 and 31.\n")
            elif age_month > 13 or age_month < 0:
                print("Invalid data, birth month should be between 1 and 12.\n")
            elif age_year > 2015:
                print("Sorry, we can't hire you because you are underage.\n")
            elif age_day < 32 and age_day > 0 and age_month < 13 and age_month > 0 and age_year < 2015:
                return True
            else:
                raise ValueError("Please enter valid data for your date of birth.\n")
            break
        except ValueError:
            print("Please enter valid data for your date of birth.\n")
            break

def check_string(value):
    while True:
        try:
            if len(value) > 20:
                print("Invalid data, please shorten first and last name to 20 characters or less both.\n")
            elif len(value) == 0:
                print("Invalid data, please try again.\n")
            elif len(value) < 21:
                return True
            else:
                raise ValueError("Invalid data, please shorten first and last name to 20 characters or less both.\n")
            break
        except ValueError:
            print("Please enter a valid number\n")
            break


def main():
    description()
    get_user_input()
    if user_choice == 1:
        add_employee()

main()