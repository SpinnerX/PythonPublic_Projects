import os
import glob
import time
import re
from termcolor import colored

def menu_display():
    print("""
    ===========BANK===========
    |   1. Create Account    |
    |   2. Login Account     |
    |   3. Admin Login       |
    |   0. Leave Program     |
    ==========================
    """)


def user_account_display(username):
    print(f"""
    ==========={username} Account============
    |   1. Setup Personal Information       |
    |   2. Check Checking/Savings Account   |
    |   3. Display Personal Information     |
    |   0. Logout                           |
    =========================================
    """)


def accountManagers_Menu(Admin_Name):
    print(f"""
    ========{Admin_Name} Account=======
    |   1. Search Accounts           |
    |   2. Search User               |
    |   3. Display Active Accounts   |
    |   4. Display recent or lowest  |
    |   0. Admin Logout              |
    |   NOTE: Add rename, maybe?     |
    |                                |
    ==================================
    """)


# yes_responds_file_path = f'/Users/aaronher/Desktop/Dev_1 Support Responds/yes responsive'
yes_responds_file_path = f'Dev_1_Support_Responds/yes responsive'
# email_file_path = f'/Users/aaronher/Desktop/Dev_1 Support Responds/email responsive'
email_file_path = f'Dev_1_Support_Responds/email responsive'
# phone_file_path = f'/Users/aaronher/Desktop/Dev_1 Support Responds/phone responsive'
phone_file_path = f'Dev_1_Support_Responds/phone responsive'
# checkings_respond = f'/Users/aaronher/Desktop/Dev_1 Support Responds/checkings Responsive'
checkings_respond = f'Dev_1_Support_Responds/checkings Responsive'
# savings_respond = f'/Users/aaronher/Desktop/Dev_1 Support Responds/savings Responsive'
savings_respond = f'Dev_1_Support_Responds/savings Responsive'
# date_of_birth_filePath = f'/Users/aaronher/Desktop/Dev_1 Support Responds/birthDate responsive'
date_of_birth_filePath = f'Dev_1_Support_Responds/birthDate responsive'
name_respond = f'/Users/aaronher/Desktop/Dev_1 Support Responds/name responsive'
accountNumber_File_Path = f'/Users/aaronher/Desktop/Dev_1 Support Responds/account number responsive'

# Opening files
open_yes_responsive = open(yes_responds_file_path, 'rb').read().decode()
open_email_file_path = open(email_file_path, 'rb').read().decode()
open_contact_information = open(phone_file_path, 'rb').read().decode()
open_checkings = open(checkings_respond, 'rb').read().decode()
open_savings = open(savings_respond, 'rb').read().decode()
open_birthDate = open(date_of_birth_filePath, 'rb').read().decode()
open_name = open(name_respond, 'rb').read().decode()
open_acctNumber_FilePath = open(accountNumber_File_Path, 'rb').read().decode()


# accountNumber_File_Path = f'/Users/aaronher/Desktop/Dev_1 Support Responds/account number responsive'
# open_acctNumber_FilePath = open(accountNumber_File_Path, 'rb').read().decode()

# To locate the files in the directory.
def file_path(username):
    filePath = f'/Users/aaronher/Desktop/DEV_1/{username}'
    return filePath


# Read file paths based on the clients username!
def read_file_path(username):
    open_file_path = open(file_path(username), 'rb')
    Read_file_path = open_file_path.read().decode()
    return Read_file_path


# For admin usages here below!
def directory():
    # Directory = '/Users/aaronher/Desktop/DEV_1/'
    Directory = 'DEV_1/'
    return Directory

def search_Files_InDirectory():
    # Directory = os.path.dirname('/Users/aaronher/Desktop/DEV_1/*')
    Directory = os.path.dirname('DEV_1/*')
    return Directory

def adminSearch_Directory():
    # Directory = '/Users/aaronher/Desktop/DEV_1/*'
    Directory = 'DEV_1/*'
    return Directory


def admin_file_path(admin_fullName):
    # filePath = f'/Users/aaronher/Desktop/DEV_1/{admin_fullName}'
    filePath = f'DEV_1/{admin_fullName}'
    return filePath


def read_file_path(admin_fullName):
    open_FilePath = open(admin_file_path(admin_fullName), 'rb')
    read_filePath = open_FilePath.read().decode()  # Decoding the binary file
    return read_filePath


class Client:  # Parent Class

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0

    # Initiating getters & setters here!
    def get_first(self):
        return self.first_name

    def set_first(self, first):
        self.first_name = first

    def get_last(self):
        return self.last_name

    def set_last(self, last):
        self.last_name = last

    def get_age(self):
        return self.age

    def set_age(self, a):
        self.age = a

    def full_name_age(self):
        return f"First: {self.first_name}\nLast: {self.last_name}\nAge: {self.age}"


# NOTE: This is for inheritance, when putting the project together!
# class Account(Client)

# Inherits from the client class
class General_Account(Client):
    def __init__(self):
        super(Client).__init__()
        self.acct_number = ""
        self.email = ""
        self.username = ""
        self.password = ""
        self.user_first = Client().first_name
        self.user_last = Client().last_name
        self.age = 0
        self.balance = 0
        self.contactInformation = 0
        self.date_of_birth, self.year, self.month, self.day = "", "", "", ""
        self.the_boolean = False  # Boolean

    def get_email(self):
        return self.email

    def set_email(self, set_email):
        self.email = set_email

    def get_balance(self):
        return self.balance

    def set_balance(self, set_balance):
        self.balance = set_balance

    # Confirm if user wants to setup new account!
    def user_confirmation(self):
        user_response = str(input("Continue to create account(y/n): "))

        if user_response in open_yes_responsive:
            self.the_boolean = True  # Set the response to true here!
            while self.the_boolean:
                print("Create Account goes here!")
                break
            else:
                return "Send user to the main menu here!"

    # Create account, in account is/not existed or created
    def create_Account(self):
        self.username = str(input("Enter new username: "))

        # file_path = f'/Users/aaronher/Desktop/DEV_1/{self.username}'

        if os.path.isfile(file_path(self.username)):
            return "User already exists"
        else:
            with open(file_path(self.username), 'wb') as binaryFile_open:
                self.password = str(input("Enter new password: "))
                binaryFile_open.write(str("Username: " + self.username).encode())
                binaryFile_open.write("\n".encode())
                binaryFile_open.write(str("Password: " + self.password).encode())
                binaryFile_open.close()
        # User full name goes here!
        print("Create first & last name here!")
        # Main() # Send user to the main menu here!

    # Login page here!
    def login(self):
        self.username = str(input("Enter username: "))

        if os.path.isfile(file_path(self.username)):
            self.check_password(self.username)
        else:
            return "User does not exist."

    # Check if password exists process
    def check_password(self, username):

        with open(file_path(username), 'rb') as binaryFile_Open:
            self.password = str(input("Emter password: "))
            read_password = binaryFile_Open.read().decode()

            # To check if password exists!
            if self.password in read_password:
                print("""
                \n
                Access Granted!
                Loading Account...
                \n
                """)
                self.account(username)

    # User account that is accessed
    def account(self, username):
        print("Welcome back " + username)

        # Display user options
        user_account_display(username)
        user_response = int(input("Enter Number: "))

        if user_response == 1:
            self.setting_personal_Information(username)
        elif user_response == 2:
            self.banking_options(username)
        elif user_response == 3:
            self.display_information(username)
        else:
            print("Logging Out...")
            time.sleep(0.5)
            Main()  # Take user back to the main menu here!

    # Adding personal information
    def setting_personal_Information(self, username):
        self.email = open_email_file_path
        self.contactInformation = open_contact_information
        self.date_of_birth = open_birthDate
        self.acct_number = open_acctNumber_FilePath

        highlighted_WORD = "exit"
        highlighted_word = colored(highlighted_WORD, color="red")

        print("\nInformation Setup Options: Email, Phone Number, ID, Date of Birth")
        print("Type " + highlighted_word + " to leave this options menu.")

        user_response = str(input("What information do you want to add?: "))

        if user_response in self.email:
            self.the_boolean = True
            self.setup_email(username, self.the_boolean)
        elif user_response in self.contactInformation:
            self.add_contact_information(username)
        elif user_response in self.date_of_birth:
            self.setup_birthDate(username)
        else:
            print("\n")
            self.account(username)
        self.setting_personal_Information(username)

    # Setup first & last name here!
    def add_full_name(self, username):
        read_fullName = open_name

        if os.path.isfile(file_path(username)):
            self.user_first = str(input("Enter your first name: "))
            self.user_last = str(input("Enter your last name: "))

            if self.user_first and self.user_last in read_fullName:
                print("Full name already exists/created.")
            else:
                with open(file_path(username), 'ab') as binaryFile_Open:
                    binaryFile_Open.write("\n".encode())
                    binaryFile_Open.write(str("First Name: " + self.user_first).encode())
                    binaryFile_Open.write(str("Last Name: " + self.user_last).encode())
                    binaryFile_Open.close()
            self.add_age(username)
        else:
            print("User does not exist!")

    # Setup users age
    def add_age(self, username):
        try:
            self.age = int(input("Enter your age: "))

            if os.path.isfile(file_path(username)):
                if int(self.age) < 18:
                    print("You are too young to be creating a bank account!")
                elif int(self.age) >= 18:
                    if str(self.age) in read_file_path(username):
                        print("Age has already been added to personal information.")
                    else:
                        with open(file_path(username), 'ab') as binaryFile_Open:
                            binaryFile_Open.write("\n".encode())
                            binaryFile_Open.write(str("Age: " + str(self.age)).encode())
                            print("Age has been created and added into personal information.")
                            binaryFile_Open.close()
        except ValueError:
            print("Type age number,  no strings.")
            self.add_age(username)  # If value error occurs, then it will execute the function again here!

    # Create email here
    def setup_email(self, username, start_execution):
        while start_execution:
            self.email = str(input("Enter new email: "))

            if self.email in read_file_path(username):
                print("Email already exists!")
                break
            else:
                with open(file_path(username), 'ab') as binaryFile_Open:
                    binaryFile_Open.write("\n".encode())
                    binaryFile_Open.write(str("Email: " + self.email).encode())
                    print("New email has been created.")
                    binaryFile_Open.close()
                    break

    # Load, if email exists
    def load_email(self, username):
        self.email = str(input("Enter your email: "))

        # Read the specific information in the files of the username!
        # Read file from the read_file_path() function.
        if self.email in read_file_path(username):
            print("Email has been found in users informational status.")
            print(read_file_path(username)[2])  # Display the list from the file being read in this function!
        else:
            print("Email not found!")
            self.setting_personal_Information(username)
        self.setting_personal_Information(username)

    # Create contact information
    def add_contact_information(self, username):
        self.contactInformation = str(input("Enter new contact information: "))

        # Check if the user already exists.
        if os.path.isfile(file_path(username)):
            # Read the specific information in the files of the username!
            if self.contactInformation in read_file_path(username):
                print("Contact information already exists in your personal info settings.")
            else:
                with open(file_path(username), 'rb+') as binaryFile_Open:
                    binaryFile_Open.write("\n".encode())
                    binaryFile_Open.write(str("Contact Information: " + str(self.contactInformation)).encode())
                    print("Contact information has been added into your personal information!")
                    binaryFile_Open.close()
            self.setting_personal_Information(username)

    # Load, if contact information exists
    def load_contact_information(self, username):

        if os.path.isfile(file_path(username)):
            with open(file_path(username), 'rb') as binaryFile_Open:
                self.contactInformation = int(input("Enter contact information: "))
                read_contactInfo = binaryFile_Open.read().decode()

                try:
                    if str(self.contactInformation) in read_contactInfo:
                        print("Contact information already exists.")

                except IndexError:
                    user_response = str(input("Phone number does not exist, would you like to create one? "))

                    if user_response in open_yes_responsive:
                        self.add_contact_information(username)
                    self.setting_personal_Information(username)

    # add date of birth
    def setup_birthDate(self, username):

        self.month = str(input("Enter month you were born: "))
        self.day = str(input("Enter day you were born: "))
        self.year = str(input("Enter the year you were born: "))

        if os.path.isfile(file_path(username)):
            if self.month and self.day and self.year in open_birthDate:
                print("Date of Birth has already been added!")
            else:
                with open(file_path(username), 'rb') as binaryFile_Open:
                    binaryFile_Open.write(str("\n").encode())
                    binaryFile_Open.write(str("Date of Birth Information - > " + self.month).encode())
                    binaryFile_Open.write(str(" Day: " + self.day).encode())
                    binaryFile_Open.write(str(" Year: " + self.year).encode())
                    binaryFile_Open.close()
        else:
            print("User does not exist.")

    # Load, if date of birth exists.
    def load_birthDate(self, username):

        if os.path.isfile(file_path(username)):
            self.month = str(input("Enter the month you were born: "))
            self.day = str(input("Enter the day you were born: "))
            self.year = str(input("Enter the year you were born: "))

            if self.month and self.day and self.year in open_birthDate:
                print("Your date of birth information has already been setup!")

            user_response = str(
                input("Date of birth does not exist, did you want to set this up this information(y/n): "))
            if user_response in open_yes_responsive:
                self.setup_birthDate(username)
            self.account(username)
        else:
            print("User does not exist!")

    # Options to enter checkings/savings acct
    def banking_options(self, username):

        print("Press enter to leave options")
        print("Type 'EXIT', to end transactions.")
        user_response = str(input("Do you want to enter checkings or savings account: "))

        if user_response in open_checkings:
            self.checkings_account(username)
        elif user_response in open_savings:
            self.savings_account(username)
        elif user_response == "exit":
            self.account(username)
        else:
            self.account(username)
        self.account(username)

    # Users checkings account
    def checkings_account(self, username):

        if os.path.isfile(file_path(username)):
            self.balance = int(input("Enter amount into checkings: "))

            with open(file_path(username), 'ab') as binaryFile_Open:
                binaryFile_Open.write(str("\nCheckings Account Balance: " + str(self.balance)).encode())
                print("Checkings Account has been updated.")
                binaryFile_Open.close()
        else:
            print("User does not exist for entering amount into checkings.")
        self.account(username)

    # Users savings account
    def savings_account(self, username):

        if os.path.isfile(file_path(username)):
            self.balance = int(input("Enter amount into savings: "))

            with open(file_path(username), 'ab') as binaryFile_Open:
                binaryFile_Open.write(str("\nSavings Account Balance: " + str(self.balance)).encode())
                print("Savings account balance has been updated.")
                binaryFile_Open.close()

    # Display all of users account.
    def display_information(self, username):

        if os.path.isfile(file_path(username)):
            with open(file_path(username), 'rb') as binaryFile_Open:
                print(binaryFile_Open.read().decode())
                binaryFile_Open.close()
        self.account(username)


class Account_Manager(General_Account):

    def __init__(self):
        super(General_Account).__init__()
        self.admin_first = ""
        self.admin_last = ""
        self.admin_fullName = ""
        self.admin_username = ""
        self.admin_password = ""
        self.email_response = open_email_file_path
        self.contact_information_response = open_contact_information
        self.accountNumber_response = open_acctNumber_FilePath  # This is for the account number response!
        self.accountManager_SearchEmail = ""

    # Create account manager
    def create_AccountManager_Acct(self):
        self.admin_first = str(input("Enter your first name: "))
        self.admin_last = str(input("Enter your last name: "))
        self.admin_fullName = self.admin_first + " " + self.admin_last

        if os.path.isfile(admin_file_path(self.admin_fullName)):
            return print("User already exists!")
        else:
            self.admin_username = str(input("Enter new admin username: "))
            self.admin_password = str(input("Enter new admin password: "))
            with open(admin_file_path(self.admin_fullName), 'wb') as binary_fileOpen:
                binary_fileOpen.write(str("Name: " + self.admin_fullName).encode())
                binary_fileOpen.write(str("\nAdmin Username: " + self.admin_username).encode())
                binary_fileOpen.write("\n".encode())
                binary_fileOpen.write(str("\nPassword: " + self.admin_password).encode())
                print("New Admin Account created.")
                binary_fileOpen.close()
        Main()

    # login process
    def acct_manager_login(self):
        self.admin_first = str(input("Enter first name: "))
        self.admin_last = str(input("Enter last name: "))
        self.admin_fullName = self.admin_first + " " + self.admin_last

        if os.path.isfile(admin_file_path(self.admin_fullName)):
            if self.admin_fullName in read_file_path(self.admin_fullName):
                self.admin_username = str(input("Enter Account managers username: "))
                if self.admin_username in read_file_path(self.admin_fullName):
                    self.check_AccountManagers_Password(self.admin_fullName)
                else:
                    print("Username is incorrect!")
                    self.acct_manager_login()
            else:
                return print("Name does not exist!")
        else:
            return print("User does not exist!")

    # Check if password exists!
    def check_AccountManagers_Password(self, account_Manager_Name):
        if os.path.isfile(admin_file_path(account_Manager_Name)):

            with open(admin_file_path(account_Manager_Name), 'rb') as binaryFile_Open:
                self.admin_password = str(input("Enter account managers password: "))
                read_password = binaryFile_Open.read().decode()

                if self.admin_password in read_password:
                    print("""
                    \n
                    Access Granted!
                    Loading Managers Account!
                    \n
                    """)
                    self.accountManager_Account(account_Manager_Name)
                else:
                    print("Password incorrect!")
                    self.check_AccountManagers_Password(account_Manager_Name)

    # Managers account
    def accountManager_Account(self, accountManager_Name):
        print("Welcome back " + accountManager_Name)

        # Display managers options
        accountManagers_Menu(accountManager_Name)

        try:
            response = int(input("Enter number: "))

            if response == 1:
                self.search_Account_Sorted(accountManager_Name)
            if response == 2:
                self.searchUser_Files(accountManager_Name)
            if response == 3:
                self.display_all_accounts(accountManager_Name)
            if response == 4:
                self.manager_display_sortingOptions(accountManager_Name)
            else:
                print("Admin Logging Out...")
                time.sleep(1)
                Main()
        except ValueError:
            print("Only type in integers or digits, here.")
            self.accountManager_Account(accountManager_Name)

    def search_Account_Sorted(self, accountManager_Name):

        exit_word = "exit"

        highlighted_word = colored(exit_word, color="red")

        print("Search User Options: Email, Phone Number, Acct Number")
        print("Press " + highlighted_word + " to go in login page")

        accountManager_Search = str(input("Enter Options: "))

        if accountManager_Search in self.email_response:
            self.searchFile_Email(accountManager_Name)
        elif accountManager_Search in self.contact_information_response:
            self.searchUsing_ContactInformation(accountManager_Name)
        elif accountManager_Search in self.accountNumber_response:
            self.search_AcctNumber(accountManager_Name)
        elif accountManager_Search == exit_word:
            print("Leaving to the login page.")
            time.sleep(1)
            self.accountManager_Account(accountManager_Name)
        else:
            print("You only have the available options listed above!")
            time.sleep(1)
            self.search_Account_Sorted(accountManager_Name)

    # Search dir for user email
    def searchUsing_Email(self, accountManager_Name):
        search_directory = os.path.dirname(os.path.realpath(adminSearch_Directory()))

        if os.path.isfile(admin_file_path(accountManager_Name)):
            # Search for specific file in directory
            for root, Directory, files in os.walk(search_directory):
                for file in files:
                    if file.endswith(''):  # To search for a file that ends with the '' extension!
                        self.searchFile_Email(accountManager_Name)
                        print("\n")
                        break

    # Search user file for email, then display their information
    def searchFile_Email(self, accountManager_Name):
        self.accountManager_SearchEmail = str(input("Enter user email: "))

        if os.path.isfile(admin_file_path(accountManager_Name)):
            for userFiles in glob.glob(adminSearch_Directory()):
                with open(userFiles, 'rb') as binaryFile_Open:
                    content = binaryFile_Open.read().decode()
                    find_email_pattern = re.findall(r'[\w\.+]+@[\w\.]+', content)
                    if self.accountManager_SearchEmail in content:
                        for email in find_email_pattern:
                            print("Email found in " + email)
                            print("\n")
                            print("===========USER ACCOUNT==========")
                            print(content)
                            print("\n")
                        break
            else:
                print("Email not found!")
                print("\n")
        self.search_Account_Sorted(accountManager_Name)

    # Search dir for user, and their contact information if it matches
    def searchUsing_ContactInformation(self, accountManager_Name):

        search_ContactInformation = int(input("Enter user contact information: "))

        if os.path.isfile(admin_file_path(accountManager_Name)):
            for user_Files in glob.glob(adminSearch_Directory()):
                with open(user_Files, 'rb') as binaryFile_Open:
                    file_content = binaryFile_Open.read().decode()
                    if str(search_ContactInformation) in file_content:
                        print("Contact Information has been found in " + file_content)
                        print("\n")
                        break
            else:
                return print("\nContact Information not found!")
        else:
            return print("\nUser not found!")
        self.search_Account_Sorted(accountManager_Name)

    # Find the acct number in file in the current directory
    # client_1 account number is,
    def search_AcctNumber(self, accountManager_Name):
        print("NOTICE: searching account number here!")
        if os.path.isfile(admin_file_path(accountManager_Name)):
            for root, Directory, userFiles in os.walk(adminSearch_Directory()):
                for file in userFiles:
                    if file.endswith(''):
                        self.find_AcctNumber(accountManager_Name)
                        break
                    else:
                        return print("Account number not found in users information")
                self.search_Account_Sorted(accountManager_Name)
        else:
            print("User does not exist.")

    # Find the account number in the users file information
    def find_AcctNumber(self, accountManager_Name):

        search_AccountNumber = int(input("Enter account number: "))

        if os.path.isfile(admin_file_path(accountManager_Name)):
            for userFiles in glob.glob(adminSearch_Directory()):
                with open(userFiles, 'rb') as binaryFile_Open:
                    content = binaryFile_Open.read().decode()
                    if str(search_AccountNumber) in content:
                        print("\n")
                        print("Account Number has been found in " + content)
                        print("\n")
                        break
                    else:
                        print("Account number not found!")
                        self.search_Account_Sorted(accountManager_Name)
                        break

    def searchUser_Files(self, accountManager_Name):

        if os.path.isfile(admin_file_path(accountManager_Name)):
            for root, Directory, files in os.walk(os.path.dirname(adminSearch_Directory())):
                for file in files:
                    if file.endswith(''):
                        self.find_UserFiles_Information(accountManager_Name)
                        print("User found!")
                        print("\n")
                        break

    def find_UserFiles_Information(self, accountManager_Name):

        enter_userFirst = str(input("Enter user first name: "))
        enter_userLast = str(input("Enter user last name: "))

        if os.path.isfile(admin_file_path(accountManager_Name)):
            for files in glob.glob(adminSearch_Directory()):
                with open(files, 'rb') as binaryFile_Open:
                    content = binaryFile_Open.read().decode()
                    if enter_userFirst and enter_userLast in content:
                        print("\n")
                        print("Users Information has been found in " + content)
                        print("\n")
        self.accountManager_Account(accountManager_Name)

    # Account managers sorting options
    def manager_display_sortingOptions(self, accountManager_Name):
        print("""
        1. Display five lowest
        2. Display five recent
        0. Leave to login page
        """)

        try:
            accountManager_response = int(input("What option would you like to display?: "))

            if os.path.isfile(admin_file_path(accountManager_Name)):
                if accountManager_response == 1:
                    self.display_five_oldest(accountManager_Name)
                elif accountManager_response == 2:
                    self.display_five_recent(accountManager_Name)
                else:
                    self.accountManager_Account(accountManager_Name)
            # else:
            #    print("User does not exist.")
            #    self.accountManager_Account(accountManager_Name)
        except ValueError:
            print("Type only integers.")
            self.manager_display_sortingOptions(accountManager_Name)
        self.manager_display_sortingOptions(accountManager_Name)

    # Display the five oldest accounts created
    def display_five_oldest(self, accountManager_Name):

        if os.path.isfile(admin_file_path(accountManager_Name)):
            userAccounts = [users for users in os.listdir(directory())
                            if os.path.isfile(os.path.join(directory(), users))]
            userAccounts.sort(key=lambda users: os.path.getmtime(os.path.join(directory(), users)), reverse=False)

            # Iterates from 1 to 5 here
            for iteration in range(0, 6):
                for users in userAccounts:
                    print(users)
                    if users == userAccounts[4]:
                        break
                break
        self.manager_display_sortingOptions(accountManager_Name)

    # Display the five recent accounts created
    def display_five_recent(self, accountManager_Name):

        if os.path.isfile(admin_file_path(accountManager_Name)):
            userAccounts = [users for users in os.listdir(directory())
                            if os.path.isfile(os.path.join(directory(), users))]
            userAccounts.sort(key=lambda users: os.path.getmtime(os.path.join(directory(), users)), reverse=True)

            # Iterates from 1 to 5 here
            for iteration in range(0, 6):
                for users in userAccounts:
                    print(users)
                    if users == userAccounts[4]:
                        break
                break
        self.manager_display_sortingOptions(accountManager_Name)

    # Display all the accounts, from most updated to oldest
    def display_all_accounts(self, accountManager_Name):

        user_Accounts = [S for S in os.listdir(directory())
                         if os.path.isfile(os.path.join(directory(), S))]
        user_Accounts.sort(key=lambda S: os.path.getmtime(os.path.join(directory(), S)), reverse=True)

        for accounts in user_Accounts:
            print("-------------------")
            print(accounts)
        self.accountManager_Account(accountManager_Name)


def Main():
    start_program = Account_Manager()
    # print("Create new admin account here!")
    # start_program.create_AccountManager_Acct()
    menu_display()

    user_response = int(input("Enter Number: "))

    if user_response == 1:
        start_program.create_Account()
    elif user_response == 2:
        start_program.login()
    elif user_response == 3:
        start_program.acct_manager_login()
    else:
        print("Leaving Program...")
        time.sleep(1)
        exit()


if __name__ == "__main__":
    Main()