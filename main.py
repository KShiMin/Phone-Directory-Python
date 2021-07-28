# counter for number of contact there is in the system/ application
count = 0
# create empty dictionary
contact = {}


# Search Function
def search():
    while True:
        print("Search Contact:")
        print("Search By:")
        print("1. Name")
        print("2. Contact Number")
        print("3. Hobbies")
        print("0. Return to main menu")
        choice = int(input("Your choice:"))
        if choice == 1:
            name = input("Enter the name:").capitalize()
            if name in contact:
                print("Not available yet")
            else:
                print("Contact not found!\n")
        elif choice == 2:
            mobile = int(input("Enter the mobile number:"))
            print(contact.items())
            if mobile in contact.items():
                print("Not available yet")
            else:
                print("No contact with this number found!\n")
        #     if name in contact:
        #         name_add = contact[name][0]
        #         name_mobile = contact[name][1]
        #         name_hobby = contact[name][2]
        #         print("Name: %s" % name
        #         print("Address: %s" % name_add)
        #         print("Mobile Number: %d" % name_mobile)
        #         print("Hobbies : %s \n" % name_hobby)
        #         break
        #     else:
        #         print("Contact not found!\n")
        # if choice == 2:
        #     mobile = int(input("Enter the mobile number:"))
        #     for key in contact:
        #         dict_add = contact[key][0]
        #         dict_mobile = contact[key][1]
        #         dict_hobby = contact[key][2]
        #         if mobile == dict_mobile:
        #             print("Name: %s" % key)
        #             print("Address: %s" % dict_add)
        #             print("Mobile Number: %d" % dict_mobile)
        #             print("Hobbies : %s \n" % dict_hobby)
        #             break
        #         # If mobile number not in contact list
        #         elif mobile != dict_mobile and key == len(contact):
        #             print("No contact with this number found!\n")
        elif choice == 3:
            hobby = input("Enter the hobby:")
            if hobby in contact:
                print("Not available yet")
            else:
                print("No contact with this hobby found!\n")
        elif choice == 0:
            break
        else:
            print("Please select a valid option")


# Adding new contact function
def newcontact():
    global count
    # create empty list for hobbies
    hobbies = []
    print("Add Contact: \n")
    name = input("Please enter the contact name:")
    address = input("Please enter the contact's address:")
    mobile_num = int(input("Please enter the contact's mobile number:"))
    while True:
        hobby = input("Please enter a hobby(Enter 'end' to stop adding):")
        if hobby.lower() == 'end':
            contact[name.capitalize()] = address, mobile_num, hobbies
            print("Contact added!")
            print(contact)
            count += 1
            break
        else:
            hobbies.append(hobby)


# Function to check which option user selected
def checker(option):
    if option == 1:
        newcontact()
    elif option == 2:
        search()
    elif option == 3:
        print("Option 3 function currently not available.")
    elif option == 4:
        print("Option 4 function currently not available.")
    elif option == 5:
        print("Option 5 function currently not available.")
    else:
        print("Please enter a valid function options \n")


# Main Menu function
def menu():
    check = [2, 4, 5]
    while True:
        print("Welcome to My Phone Directory:")
        print("Number of contact in your directory : %d" % count)
        print("These are the functions available:")
        print("1. Add new contact")
        print("2. Search for contact")
        print("3. Display all contact details in directory")
        print("4. Update existing contact details")
        print("5. Remove existing contact")
        print("0. Exit program")
        select = int(input("Your selection please:"))
        # check if user input is search, update or remove
        if select == 0:
            print("Thank you and see you again~")
            break
        elif count == 0 and select in check:
            print("The selection is not valid as your contact list is emtpy.\n")
        else:
            checker(select)
        # if count == 0 and select == 2 or select == 4 or select == 5:
        #     print("The selection is not valid as your contact list is emtpy.\n")
        # if select == 0:
        #     print("Thank you and see you again~")
        #     break
        # else:
        #     checker(select)


menu()
