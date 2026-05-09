'''
Jonathan Thompson
IS 303 - A02

Access Checker
This program determines access level based on role and time of day.

Inputs:
- User name (string)
- User Role (string)
- Time of day (integer)

Processes:
- Validate Role (must be admin/employee/visitor)
- Validate time (must be a number between 0-23)
- Determine access level based off role, clearance, and time inputs.
- Admin may enter any time
- Employee may enter from 8-22
- Visitor may enter from 9-20

Outputs:
- Print if access is accepted or denied along with role and time of day.
- Print error message if any input is invalid
'''


# Inputs

name = input("What is your name? ")
role = input("Are you an Admin, Employee or Visitor? ").lower()
time = input("What is the hour? (Use 24 hour clock. Example: If it is 9:59pm enter 21.) ")


# Role Input Validation

valid_role = False
if role == "admin" or role == "employee" or role =="visitor":
    valid_role = True
else:
    print("Invalid role. Please enter Admin, Employee, or Visitor.")


# Time Input Validation

valid_time = False
time = time.replace(".","",1)
time_is_int = time.isdigit()

if time_is_int == True:
    time = int(time)
    if time >= 0 and time <=23:
        valid_time = True
else:
    print("Invalid time. Please enter a whole number between 0 and 23.")


# Output Access Permissions

if valid_role == True and valid_time == True:

    if role == "visitor" and time >= 9 and time <= 20:
        print(f"Access Granted. Welcome {name}. Visitor hours are from 9-20. Thank you for visiting us today.")
    elif role == "employee" and time >= 8 and time <= 22:
        print(f"Access Granted. Welcome {name}. Employee hours are from 8-22.")
    elif role == "admin":
        print(f"Access Granted. Welcome {name}.")
    else:
        print("Access denied. Please come back during the appropriate time. Vistor hours are from 9-20. Employee hours are from 8-10. Thank you.")