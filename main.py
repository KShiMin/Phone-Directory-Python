def addnewcontact():
    global count
    print("Add Contact: \n")
    name = input("Please enter the contact name:")
    address = input("Please enter the contact's address:")
    mobile_num = input("Please enter the contact's mobile number:")

    while True:
        hobbies = input("Please enter a hobby(Enter 'end' to stop adding):")
        if hobbies == 'end' or hobbies == "End":
            print("Contact added!")
            count += 1
            break
        else:
            contact.

    menu(select)


count = 0
contact = {}
select = 0


# Main Menu
def menu(option):
    global select
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
    return option


# Check which option user selected
def checker():
    # check if user selected is valid
    if select in range(0, 6):
        print(select)
        # check if user input is search, update or remove
        if select == 2 or select == 4 or select == 5:
            # check if there are contact in the system
            if count == 0:
                print("That selection is not valid as your contact list is emtpy.")
            elif select == 2:
                print("Option 2 function currently not available.")
            elif select == 4:
                print("Option 4 function currently not available.")
            else:
                print("Option 5 function currently not available.")
        elif select == 1:
            addnewcontact()
        elif select == 3:
            print("Option 3 function is currently not available.")
        else:
            print("Option 0 function is currently not available.")
    else:
        print("Please enter a valid function options")

menu(select)