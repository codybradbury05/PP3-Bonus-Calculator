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

def main():
    get_period_sales()


print("Welcome to your bonus calculator!\n")

time.sleep(1)

main()

