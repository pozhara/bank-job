# Bank Job

Bank Job is a program that lets a user register as an employee in a newly opened bank. Then gives options on what to do next: request time off, see colleagues birthdays or roles, or exit. 

# Existing features

## Introduction and registering to be an employee

This section contains brief introduction to make program's theme clear. Then asks user to register in the system.

Inputs ask for first and last name, date of birth and job role. 

String inputs are checked for:
-length being higher than 20 and lower than 1;
-being a number or null;
-being an unalphabetic character.

Number inputs are checked for:
-birth day being higher than 31 or lower than 1;
-birth month being higher than 12 or lower than 1;
-then program calculates exact age based on the year input, if user is underage or older than 80, then they have to try again.

![Photo of this section](images/register.jpg)

Then worksheet gets updated and the menu appears that asks user what they want to do. Options are:
1. Request time off.
2. See your colleagues' birthdays.
3. See your colleagues' names and roles.
4. Exit.

## Request time off

Program states user's name, that they are requesting time off and what information will be needed (starting date, ending date and a reason).

Dates are checked for:
-being higher than 31.12 or lower than 01.01;
-being an integer;
-numbers after comma being exactly two and being higher than 12;
-being null.

Reason is checked for:
-length being higher than 25 or lower than 1;
-being numeric or having special characters;
-being null.

![Photo of request time off option](images/request.jpg)

Once the user completes requesting, worksheet is updated and program gets a random number between 1 and 10 to approve or disapprove the request.
If even number comes up, user gets approval.
If uneven number does, user gets disapproval and gets asked if they want to challenge it. 

Challenge input is checked for:
-being anything other than Y or N.

If their input is Y, they get a message that someone will contact them soon and then the menu appears, asking user what they want to do.
If their input was N, they get a thank you message and the menu appears.

![Photo of request approval](images/request-validation.jpg)

## See your colleagues' birthdays