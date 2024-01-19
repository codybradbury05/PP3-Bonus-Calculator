import gspread
from google.oauth2.service_account import Credentials
import time
import statistics

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bonus Calculator')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

labour = SHEET.worksheet('labour')

labour_data = labour.get_all_values()

def get_period_sales():
    """
    Ask the user for the weekly sales during the period.
    """
    while True:
        print("Please enter each weeks total sales.\n")
        time.sleep(1)
        print("4 Weeks of sales must be inputted, seperated by commas\n")
        time.sleep(1)
        print("For Example: 16543,12365,12765,9000\n")
        time.sleep(1)

        sales_input = input("Enter your weekly sales here:\n")

        sales_data = sales_input.split(",")

        if validate_sales(sales_data):
            print("Weekly Sales data valid :)")
            break

    return sales_data


def validate_sales(values):
    """
    Converts strings into integers and raises an error if strings
    won't convert into int and/or if there isnt 4 values.
    """

    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"Exaclty 4 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    time.sleep(1)
    print("Updating sales worksheet...\n")
    time.sleep(1)
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully. \n")

def total_sales(sales_data):
    """
    Adds each weekly sale to tally a total sales.
    """
    print("Tallying your sales for the period...\n")
    time.sleep(1)
    sum_sales = print(f"Your sales for the period: {sum(sales_data)}")
    time.sleep(1)

def get_labour_data():
    while True:
        print("Please enter each weeks total labour.\n")
        time.sleep(1)
        print("4 Weeks of labour must be inputted, seperated by commas\n")
        time.sleep(1)
        print("For Example: 21.5,22.9,27.8,21.1\n")
        time.sleep(1)

        labour_input = input("Enter your weekly labour here:\n")

        labour_data = labour_input.split(",")

        if validate_labour(labour_data):
            print("Weekly labour data valid :)")
            break

    return labour_data


def validate_labour(values):
    """
    Converts strings into integers and raises an error if strings
    won't convert into int and/or if there isnt 4 values.
    """

    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"Exaclty 4 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


def update_labour_worksheet(labour_data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    time.sleep(1)
    print("Updating labour worksheet...\n")
    time.sleep(1)
    labour_worksheet = SHEET.worksheet("labour")
    labour_worksheet.append_row(labour_data)
    print("Labour worksheet updated successfully. \n")


def average_labour(labour_data):
    """
    Adds each weekly labour to tally a total labour.
    """
    print("Tallying your labour for the period...\n")
    time.sleep(1)
    mean_labour = print(f"Your labour for the period: {statistics.mean(labour_data)}")
    time.sleep(1)

def calculate_bonus(labour_data, sales_data):
    """
    Calculates percentage of bonus, must hit labour target to achieve bonus.
    Max bonus is 1% of sales.
    """
    print("Please answer these questions correctly to total your bonus.")
    bonus_deductions = 0
    time.sleep(1)
    training_input = input("Is all online training completed?(Y/N): ")
    if training_input == "N":
        bonus_deductions += 1
    time.sleep(1)
    complaints_input = input("Are complaints lower than 1.2/1000 orders?(Y/N): ")
    if complaints_input == "N":
        bonus_deductions += 1
    time.sleep(1)
    insurance_input = input("If/All insurance claims filled out?(Y/N): ")
    if insurance_input == "N":
        bonus_deductions += 1
    time.sleep(1)
    gps_input = input("Is GPS usage greater than or equal to 95%?(Y/N): ")
    if gps_input == "N":
        bonus_deductions += 1
    time.sleep(1)

    if statistics.mean(labour_data) > 21.0:
        print("Sorry you haven't hit your bonus :(")
    elif bonus_deductions == 0:
        total_bonus = sum(sales_data) * 0.01
        print(f"Your total bonus is {total_bonus}!")
    elif bonus_deductions == 1:
        total_bonus = sum(sales_data) * 0.0075
        print(f"Your total bonus is {total_bonus}!")
    elif bonus_deductions == 2:
        total_bonus = sum(sales_data) * 0.005
        print(f"Your total bonus is {total_bonus}!")
    elif bonus_deductions == 3:
        total_bonus = sum(sales_data) * 0.0025
        print(f"Your total bonus is {total_bonus}!")
    elif bonus_deductions == 4:
        total_bonus = sum(sales_data) * 0.01
        print("Sorry you haven't hit your bonus :(")

    
    

        
        

    


def main():
    data = get_period_sales()
    sales_data = [int(num) for num in data]
    ldata = get_labour_data()
    labour_data = [int(num) for num in ldata]
    update_sales_worksheet(sales_data)
    total_sales(sales_data)
    update_labour_worksheet(labour_data)
    average_labour(labour_data)
    calculate_bonus(labour_data, sales_data)



print("Welcome to your bonus calculator!\n")

time.sleep(1)

main()

