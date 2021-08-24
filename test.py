contact = [['J', 'K', 987, ['m', 't']], ['G', 'H', 876, ['n', 'b']]]

while True:
    query = str(input('Please enter the name of the contact you wish to search: '))
    for i in range(len(contact)):
        print(i)
        if query == contact[i][0]:
            print("Contact details:")
            print("name :", contact[i][0])
            print("address :", contact[i][1])
            print("mobile :", contact[i][2])
            print("hobbies :", contact[i][3])
            break
        else:
            print("contact not found")
