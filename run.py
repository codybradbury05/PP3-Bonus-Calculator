import gspread
from google.oauth2.service_account import Credentials
import time

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
    print(f"Your sales for the period: {sum(sales_data)}")
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


def main():
    data = get_period_sales()
    sales_data = [int(num) for num in data]
    ldata = get_labour_data()
    labour_data = [int(num) for num in ldata]
    update_sales_worksheet(sales_data)
    total_sales(sales_data)
    update_labour_worksheet(labour_data)


print("Welcome to your bonus calculator!\n")

time.sleep(1)

main()

