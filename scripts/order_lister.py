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


for num, order in enumerate(orders):
    os.system("cls")
    print("==== (#{}) {}'s Order' ====".format(num, order["Name:"]))
    email = order["Email address"]
    membership_id = order[fug]
    del order[fug]
    ordered_items = filter(
        lambda item: True if item[1] != "" and item[1].isnumeric() else False,
        order.items())
    for item, amount in ordered_items:
        print(("{}:" + colored(" (x{})", colors[(int(amount) - 1) % len(colors)]))
              .format(item.strip("\n"), amount))
    print("\nEmail: {}\n".format(email)
          + "VOCID: https://www.ubc-voc.com/members/show_extended?target_id={}"
          .format(membership_id))
    input("Press Enter to continue...")

