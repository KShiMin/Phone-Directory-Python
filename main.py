# counter for number of contact there is in the system/ application
count = 0
# create empty dictionary
contact = {}


# Remove Function
def remove():
    global count
    print("Remove Contact: \n")
    remove_contact = input("Please enter the contact name you want to remove: ").capitalize()
    counter = 0
    for key in contact:
        counter += 1
        if remove_contact == key:
            print("Contact Details:")
            print("Name: ", key)
            print("Address: ", contact[key]["add"])
            print("Mobile Number: ", contact[key]["mobile"])
            print("Hobbies: ", contact[key]["hobby"])
            while True:
                confirmation = input(" Is this the contact you want to remove? (Yes/No): ")
                if confirmation.lower() == "yes":
                    contact.pop(key)
                    count -= 1
                    break
                elif confirmation.lower() == "no":
                    print("Contact was not removed!")
                    break
                else:
                    print("Please select a valid confirmation option")
            break
        elif counter == count:
            print("No such contact found.")
        else:
            continue


# Update Function
def update():
    print("Update Contact: \n")
    update_contact = input("Please enter the name of the contact you would like to update: ").capitalize()
    counter = 0
    # for loop to loop through contact
    for key, value in contact.items():
        counter += 1
        if update_contact == key:
            print("Name: ", key)
            print("Address: ", contact[key]["add"])
            print("Mobile Number: ", contact[key]["mobile"])
            print("Hobbies: ", contact[key]["hobby"])
            print("")
            print("Contact Exist!")
            print("1. Address")
            print("2. Mobile Number")
            print("3. Hobbies")
            print("0. Exit")
            update_option = int(input("What would you like to update?: "))
            print("")
            # while loop to ensure user update_option is valid
            while True:
                if update_option == 1:
                    new_add = input("Enter the new address: ")
                    contact[key]["add"] = new_add
                    print("Address updated!\n")
                    break

                elif update_option == 2:
                    new_mobile = int(input("Enter the new mobile number: "))
                    contact[key]["mobile"] = new_mobile
                    print("Mobile number updated!\n")
                    break

                elif update_option == 3:
                    print("!!Note that everything will be rewritten!!")
                    hobbies = []  # create hobbies list again to store the new hobbies
                    while True:
                        new_hobby = input("Please enter new hobbies:(Enter 'end' to stop adding):")
                        if new_hobby.lower() == 'end':
                            contact[key]["hobby"] = hobbies
                            print("Hobbies updated!\n")
                            break
                        else:
                            hobbies.append(new_hobby)
                    break

                elif update_option == 0:
                    break
                else:
                    print("Please enter a valid option.\n")
        # check if for loop is at the final loop
        elif counter == count:
            print("No such contact found.\n")
        else:
            continue


# Display Function
def display():
    if count == 0:
        print("No contacts \n")
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
    global count
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
            counter = 0
            mobile = int(input("Enter the mobile number: "))
            for key in contact:
                counter += 1
                if mobile == contact[key]["mobile"]:
                    print("\nContact Details:")
                    print("Name: ", key)
                    print("Address: ", contact[key]["add"])
                    print("Mobile Number: ", contact[key]["mobile"])
                    print("Hobbies: ", contact[key]["hobby"])
                    break
                # check if the loop is at the final loop
                elif counter == count:
                    print("No contact with this number found\n")
                    break
                else:
                    continue
        elif choice == 3:
            counter = 0
            hob = input("Enter the hobby: ")
            for key in contact:
                counter += 1
                if hob in contact[key]["hobby"]:
                    print("\nContact Details:")
                    print("Name: ", key)
                    print("Address: ", contact[key]["add"])
                    print("Mobile Number: ", contact[key]["mobile"])
                    print("Hobbies: ", contact[key]["hobby"])
                    continue  # stop at this line and repeat loop
                # check if the loop is at the final loop
                elif counter == count:
                    print("No contact with this hobby found\n")
                    break
                else:
                    continue
        elif choice == 0:
            break  # return to main menu
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
            contact[name.capitalize()] = {
                "add": address, "mobile": mobile_num, "hobby": hobbies}
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
