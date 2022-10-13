# main.py
# Author: Saxon Neustaeter
# Date: 10/13/2022
# Description: Basic retail suite written in python
import os
os.system("cls")

def main_menu():
    print("==================== MAIN MENU ====================")
    print("Please slect an option from the list below:")
    print("\t1) Inventory")
    print("\t2) Sales")
    print("\t3) Admin")
    print("\t4) Reports")
    print("\t5) Receiving")
    print("\t6) Pricing")
    usr = input()
    
    match usr:
        case "1":
            return "Inventory"
            
        case "2":
            return "Sales"
            
        case "3":
            return "Admin"
            
        case "4":
            return "Reports"
            
        case "5":
            return "Receiving"
            
        case "6":
            return "Pricing"
            
        case _:
            return "Enter a number from the list dumbfuck"

def inventory_menu():
    print("==================== INVENTORY MENU ====================")

def sales_menu():
    print("==================== SALES MENU ====================")
    
def admin_menu():
    print("==================== ADMIN MENU ====================")
    
def reports_menu():
    print("==================== REPORTS MENU ====================")
    
def receiving_menu():
    print("==================== RECEIVING MENU ====================")
    
def pricing_menu():
    print("==================== PRICING MENU ====================")


print(main_menu())