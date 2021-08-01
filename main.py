# counter for number of contact there is in the system/ application
count = 0
# create empty dictionary
contact = {}


# Remove Function
def remove():
    global count
    print("Remove Contact: \n")
    remove_contact = input("Please enter the contact name you want to remove: ").capitalize()
    for key in contact:
        if remove_contact == key:
            print("Contact Details:")
            print("Name: ", key)
            print("Address: ", contact[key]["add"])
            print("Mobile Number: ", contact[key]["mobile"])
            print("Hobbies: ", contact[key]["hobby"])
            while True:
                confirmation = input("Is this the contact you want to remove? (Yes/No) ").capitalize()
                if confirmation == "Yes":
                    print("Removal not available yet")
                    count -= 1
                    break
                elif confirmation == "No":
                    print("Contact was not removed!")
                    break
                else:
                    print("Please select a valid confirmation option")
        elif key == len(contact) - 1:
            print("No such contact found.")


# Update Function
def update():
    print("Update Contact:")
    print("")
    update_contact = input("Please enter the name of the contact you would like to update: ").capitalize()
    for key, value in contact.items():
        if update_contact == key:
            print("Name: ", key)
            print("Address: ", contact[key]["add"])
            print("Mobile Number: ", contact[key]["mobile"])
            print("Hobbies: ", contact[key]["hobby"])
            print("")
            print("Contact Exist")
            print("1. Address")
            print("2. Mobile Number")
            print("3. Hobbies")
            print("0. Exit")
            update_option = int(input("What would you like to update?: "))
            if update_option == 1:
                new_add = input("Enter the new address: ")
                contact[key]["add"] = new_add
                print("Address updated!")
            elif update_option == 2:
                new_mobile = int(input("Enter the new mobile number: "))
                contact[key]["mobile"] = new_mobile
                print("Mobile number updated!")
            elif update_option == 3:
                print("!!Note that everything will be rewritten!!")
                hobbies = []
                while True:
                    new_hobby = input("Please enter new hobbies:(Enter 'end' to stop adding):")
                    if new_hobby.lower() == 'end':
                        contact[key]["hobby"] = hobbies
                        print("Hobbies updated!")
                        break
                    else:
                        hobbies.append(new_hobby)
            elif update_option == 0:
                break
            else:
                print("Please enter a valid option")
            break
        else:
            print("No such contact found.")


# Display Function
def display():
    if count == 0:
        print("No contacts")
        print("")
    else:
        print("Display all contacts:")
        # Loop through the dictionary to get both the key and the value
        for key, value in contact.items():
            print("Contact Details:")
            print("Name: ", key)
            print("Address: ", contact[key]["add"])
            print("Mobile Number: ", contact[key]["mobile"])
            print("Hobbies: ", contact[key]["hobby"])
            print("")


# Search Function
def search():
    # menu for search function
    while True:
        print("\nSearch Contact:")
        print("Search By:")
        print("1. Name")
        print("2. Contact Number")
        print("3. Hobbies")
        print("0. Return to main menu")
        choice = int(input("Your choice:"))
        print("")
        # counter to check if it's at the last loop
        counter = 0
        if choice == 1:
            name = input("Enter the name: ").capitalize()
            for key in contact:
                if name == key:
                    print("\nContact Details:")
                    print("Name: ", key)
                    print("Address: ", contact[key]["add"])
                    print("Mobile Number: ", contact[key]["mobile"])
                    print("Hobbies: ", contact[key]["hobby"])
                    break
                # check if the loop is at the final loop
                elif name not in contact:
                    print("No contact with this name found\n")
                    break
                else:
                    continue
        elif choice == 2:
            mobile = int(input("Enter the mobile number: "))
            for key in contact:
                print(contact[key].values())
                if mobile == contact[key]["mobile"]:
                    print("\nContact Details:")
                    print("Name: ", key)
                    print("Address: ", contact[key]["add"])
                    print("Mobile Number: ", contact[key]["mobile"])
                    print("Hobbies: ", contact[key]["hobby"])
                    break
                # check if the loop is at the final loop
                elif mobile != contact[key]["mobile"]:
                    print("No contact with this number found\n")
                    break
                else:
                    continue
        elif choice == 3:
            hob = input("Enter the hobby: ")
            for key in contact:
                # loop through 2nd dictionary key "hobby" list
                for x in contact[key]["hobby"]:
                    if hob == x:
                        print("\nContact Details:")
                        print("Name: ", key)
                        print("Address: ", contact[key]["add"])
                        print("Mobile Number: ", contact[key]["mobile"])
                        print("Hobbies: ", contact[key]["hobby"])
                        break
                    # check if the loop is at the final loop
                    elif counter == (len(contact) - 1):
                        print("No contact with this hobby found\n")
                    else:
                        continue
        elif choice == 0:
            break  # return to main menu
        else:
            print("Please select a valid option")
        # if choice == 1:
        #     name = input("Enter the name: ").capitalize()
        #     print("")
        #     print(len(contact_list) - 1)
        #     # loop through contact_list
        #     for x in range(len(contact_list)):
        #         if name in contact_list[x]:
        #             print("Contact details:")
        #             print("Name: %s" % contact_list[x][0])
        #             print("Address: %s" % contact_list[x][1])
        #             print("Mobile Number: %d" % contact_list[x][2])
        #             print("Hobbies : %s \n" % contact_list[x][3])
        #             break
        #         # check if the loop is at the final loop
        #         # --> loop through all indexes already and it is at it's final loop
        #         elif (x == (len(contact_list) - 1)):
        #             print("No contact with this name found\n")
        #             break
        #         else:
        #             continue
        #
        # elif choice == 2:
        #     mobile = int(input("Enter the mobile number: "))
        #     print("")
        #     for x in range(len(contact_list)):
        #         if mobile in contact_list[x]:
        #             print("Contact details:")
        #             print("Name: %s" % contact_list[x][0])
        #             print("Address: %s" % contact_list[x][1])
        #             print("Mobile Number: %d" % contact_list[x][2])
        #             print("Hobbies : %s \n" % contact_list[x][3])
        #             break
        #         elif (x == (len(contact_list) - 1)):
        #             print("No contact with this mobile number found\n")
        #             break
        #         else:
        #             continue
        #
        # elif choice == 3:
        #     hobby = input("Enter the hobby: ")
        #     print("")
        #     for x in range(len(contact_list)):
        #         if hobby in contact_list[x][3]:
        #             print("Contact details:")
        #             print("Name: %s" % contact_list[x][0])
        #             print("Address: %s" % contact_list[x][1])
        #             print("Mobile Number: %d" % contact_list[x][2])
        #             print("Hobbies : %s \n" % contact_list[x][3])
        #             continue
        #         elif (x == (len(contact_list) - 1)):
        #             print("No contact with this hobby found\n")
        #             break
        #         else:
        #             continue
        #
        # elif choice == 0:
        #     break  # return to main menu
        # else:
        #     print("Please select a valid option")

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
        # elif choice == 3:
        #     hobby = input("Enter the hobby:")
        #     if hobby in contact:
        #         print("Not available yet")
        #     else:
        #         print("No contact with this hobby found!\n")


# Adding new contact function
def newcontact():
    global count
    # create empty list for hobbies
    hobbies = []
    print("Add Contact: \n")
    name = input("Please enter the contact name:")
    address = input("Please enter the contact's address:")
    mobile_num = int(input("Please enter the contact's mobile number:"))
    # while True:
    #     mobile_num = input("Please enter the contact's mobile number:")
    #     if mobile_num == mobile_num.isdigit():
    #         print("okay")
    #         break
    #     else:
    #         print("Please enter a valid mobile number")

    while True:
        hobby = input("Please enter a hobby(Enter 'end' to stop adding):")
        if hobby.lower() == 'end':
            contact[name.capitalize()] = {"add": address, "mobile": mobile_num, "hobby": hobbies}
            print("Contact added!")
            print(contact)
            print("")
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
        display()
    elif option == 4:
        update()
    elif option == 5:
        remove()
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
        print("")
        if select == 0:
            print("Thank you and see you again~")
            break
        # check if user input is search, update or remove
        elif count == 0 and select in check:
            print("The selection is not valid as your contact list is emtpy.\n")
        else:
            checker(select)


menu()
