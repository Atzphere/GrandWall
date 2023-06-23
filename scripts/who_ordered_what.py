import csv
import os
from termcolor import colored
import keyboard

filename = "../data/Sorting Copy of Summer 2023 GrandWall Order Form Spreadsheet - Form responses 1.csv"

colors = ("green", "yellow", "red", "blue", "magenta",
          "cyan", "white", "light_blue")

with open(filename, "r") as f:
    orders = list(csv.DictReader(f))
    del orders[0]

fug = '''What is your VOC Membership ID? To find this you have to login to your VOC account.
1. Go to https://www.ubc-voc.com
2. Go to "Member's Section" at the top of the page
3. Click on "Login"
4. Input your "Username" and "Password"
5. Go to "Member's Section" at the top of the page
6. Click on "Edit Account"
7. Find your "Member ID" bullet point (it should be the last bullet point)'''

def is_workable_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for num, item in enumerate(list(orders[0].keys())[2:]):
    os.system("cls")
    print("==== Item: {}' ====".format(item))
    for order in orders:
        if is_workable_integer(order[item]):
            amount = order[item]
            print(("{}: ({})" + colored(" (x{})", colors[(int(amount) - 1) % len(colors)]))
                .format(order["Name:"], order["Email address"], amount))
    input("Press Enter to continue...")
