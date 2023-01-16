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
    print("Hello, we are a recently opened bank, looking for qualified people to start their career with us.")


def get_user_input():
    while True:
        print("What would you like to do?\n1. Add youself as an employee\n2. Request a time off\n3. See everyone's birthdays")
        print("Please enter a number below to choose and hit ENTER.")
        choice = input()
    return choice

def main():
    description()
    get_user_input()

main()