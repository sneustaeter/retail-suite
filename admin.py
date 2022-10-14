# admin.py
# Author: Saxon Neustaeter
# Date: 10/14/2022
# Description: Admin functions
import os
from hashlib import sha256

userFileLoc = "users.tdf"
userList = []

def populate_user_list():
    userFile = open(userFileLoc, "r")
    for x in userFile:
        userList.append(x)
    userFile.close()

def admin_menu():
    print("==================== ADMIN MENU ====================")
    print("Please slect an option from the list below:")
    print("\t1) View Users")
    print("\t2) Add User")
    print("\t3) Remove User")
    print("\t4) Edit User")
    
def view_users():
    os.system("cls")
    print("==================== USER LIST ====================")
    for x in userList:
        y = x.split(":")
        print("UID: " + y[0])
        print("\tName: " + y[1])
        print("\tDepartment: " + y[2])
        print("\tHire Date: " + y[3])
        print("\tPassword: " + y[4])



def add_user():
    os.system("cls")
    print("==================== ADD USER ====================")
    uid = input("Enter the User ID(UID) for the new user: ")
    cont = "no"
    while cont == "no":
        pass1 = sha256(input("Enter the password for the new user: ").encode("utf-8")).hexdigest()
        pass2 = sha256(input("Confirm the password for the new user: ").encode("utf-8")).hexdigest()
        if (pass1 == pass2):
            print("The passwords match")
            cont = "yes"
        else:
            print("The passwords do not match, try again")



populate_user_list()
view_users()