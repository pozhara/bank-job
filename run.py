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
        print("What would you like to do?\n1. Add youself as an employee\n2. Request a time off\n3. See everyone's birthdays")
        print("Please enter a letter below to choose and hit ENTER.")
        choice = input()
        try: 
            user_choice = int(choice)
            print("We are processing your request...\n")
            if user_choice > 3:
                print("Please enter a valid number\n")
            break
        except ValueError:
            print("Please enter a valid number\n")
            break
    return user_choice

def main():
    description()
    get_user_input()

main()