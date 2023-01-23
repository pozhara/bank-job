import gspread
from google.oauth2.service_account import Credentials
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("office-work")

print("Hello, we are a recently opened bank, thank you for starting your career with us. Your next step is to add yourself as an employee to our system.\n")

def update_worksheet(data, worksheet):
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)

while True:
    try:
        first_name = input("Please enter your first name: ")
        print(first_name)
        if len(first_name) < 1 or len(first_name) > 20 or first_name.isnumeric():
            raise ValueError
        break
    except ValueError:
        print("Please enter valid data.\n")

while True:
    try:
        last_name = input("Please enter your last name: ")
        print(last_name)
        if len(last_name) < 1 or len(last_name) > 20 or last_name.isnumeric():
            raise ValueError
        break
    except ValueError:
        print("Please enter valid data.\n")

while True:
    try: 
        age_day = int(input("Please enter the day you were born: "))
        print(age_day)
        if age_day > 31 or age_day < 1:
            raise ValueError
        break
    except ValueError:
        print('Value must be positive and cannot be greater than 31.\n')

while True:
    try: 
        age_month = int(input("Please enter the month you were born: "))
        print(age_month)
        if age_month > 12 or age_month < 1:
            raise ValueError
        break
    except ValueError:
        print('Value must be positive and must be between 1 and 12.\n')

while True:
    try: 
        age_year = int(input("Please enter the year you were born: "))
        print(age_year)
        date_of_birth = datetime.datetime(age_year, age_month, age_day)
        age = (datetime.datetime.now() - date_of_birth)
        days = int(age.days)
        converted_years = days/365
        employee_age = int(converted_years)
        if employee_age >= 18 and employee_age < 80:
            employee_birthday = first_name + "," + last_name + "," + str(age_day) + "," + str(age_month)
            employee_birthday = employee_birthday.split(",")
            employee_birthday_for_ws = [i.strip() for i in employee_birthday]
            update_worksheet(employee_birthday_for_ws, "Birthday")
        else:
            raise ValueError
        break
    except ValueError:
        print('Invalid data, your age should be between 18 and 80.\n')

while True:
    try:
        employee_role = input("Please enter your role: ")
        print(employee_role)
        if len(employee_role) < 1 or len(employee_role) > 20 or employee_role.isnumeric():
            raise ValueError
        elif len(employee_role) > 1:
            employee_data = first_name + "," + last_name + "," + employee_role
            employee_data = employee_data.split(",")
            employee_data_for_ws = [i.strip() for i in employee_data]
            update_worksheet(employee_data_for_ws, "Employees")
            print("Thank you, the data provided is valid and is now added to our database.\n")
        break
    except ValueError:
        print("Please enter valid data.\n")

def give_options():
    print("What would you like to do?\n1. Request a day off.\n2. See your collegues' birthdays.\n3.See your collegues' names and roles.\n")
    while True:
        try:
            global user_input
            user_input = int(input("Please enter a number: "))
            if user_input >= 1 and user_input <= 3:
                print("Please wait, we are processing your request...\n")
            elif user_input < 1 or user_input > 3:
                raise ValueError
            break
        except ValueError:
            print("Invalid data, please enter a number between 1 and 3.\n")
    return user_input

def request_a_day_off(first_name, last_name):
    print("You are currently requesting a day off. We will need you to provide starting and ending date, and a reason.\n")
    while True:
        print(f"Your name is {first_name} {last_name}.")
        try:
            starting_date = float(input("Please enter a starting date (For example: 12.02): "))
            print(starting_date)
            if starting_date > 31.12 or starting_date < 01.01:
                raise ValueError
            break
        except ValueError:
            print("Invalid data, please provide it like this 12.02.\n")
    while True:
        try:
            ending_date = float(input("Please enter an ending date (For example: 12.02): "))
            print(ending_date)
            if ending_date > 31.12 or ending_date < 01.01:
                raise ValueError
            break
        except ValueError:
            print("Invalid data, please provide it like this 12.02.\n")
    while True:
        try:
            user_reason = input("Please provide a reason (maximum 25 characters): ")
            print(user_reason)
            if len(user_reason) > 25 or len(user_reason) < 1 or user_reason.isnumeric():
                raise ValueError
            else:
                request_data = first_name + "," + last_name + "," + str(starting_date) + "," + str(ending_date) + "," + user_reason
                request_data = request_data.split(",")
                request_data_for_sw = [i.strip() for i in request_data]
                update_worksheet(request_data_for_sw, "Day Off Requests")
                print("Thank you, data provided is valid and was added to our database.\n")
            break
        except ValueError:
            print("Please provide valid data.\n")

def see_birthdays():
    birthdays = SHEET.worksheet("Birthday").get_all_values()
    for row in birthdays:
        first_name_birthday = row[0]
        last_name_birthday = row[1]
        age_day_birthday = row[2]
        age_month_birthday = row[3]
        employees_birthday = last_name_birthday + ", " + first_name_birthday + ": " + age_day_birthday + "." + age_month_birthday
        print(employees_birthday)

def see_roles():
    employees = SHEET.worksheet("Employees").get_all_values()
    for row in employees:
        employee_fname = row[0]
        employee_lname = row[1]
        role = row[2]
        data_to_print = employee_lname + ", " + employee_fname + " - " + role
        print(data_to_print)

def main(first_name, last_name):
    give_options()
    if user_input == 1:
        request_a_day_off(first_name, last_name)
    if user_input == 2:
        see_birthdays()
    if user_input == 3:
        see_roles()

main(first_name, last_name)