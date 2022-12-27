def LoadDetails():
    with open("room_details.txt", 'r', encoding='utf-8') as room_details:
        rooms_data = []
        for line in room_details:
            line = line.strip("\n")
            line = line.split(',')
            rooms_data.append(line)

        return rooms_data


# 0 -> categoryname
# 1 -> number of rooms
# 2 -> capacity
# 3 -> price per night
# 4 -> price per 7 nights
# 5 -> price per 30 nights
# 6 ->number of rooms occupied
# update function of textfile
def UpdateTextFile(roomData):
    with open("room_details.txt", 'w') as details:
        for room in range(len(roomData)):
            details.write(roomData[room][0] + "," + roomData[room][1] + "," + roomData[room][2] + "," +
                          roomData[room][3] + "," + roomData[room][4] + "," + roomData[room][5] + "," + roomData[room][
                              6] + "\n")


# function for creating a summary of the rooms availability
def CreateSummary(roomData):
    for room in range(len(roomData)):
        print("categoryName", roomData[room][0])
        print("occupied_rooms", roomData[room][6])


# calculate reservation price -->function
def CalculatePrice(roomData, durationOfStay, roomIndex):
    if durationOfStay == 1:
        return int(roomData[roomIndex][3])
    elif durationOfStay == 7:
        return int(roomData[roomIndex][4])
    elif durationOfStay == 30:
        return int(roomData[roomIndex][5])


# check availability of the rooms
def check_availability(roomData, category, numberOfGuests):
    for value in range(len(roomData)):
        print(roomData[value][0]==category)
        print(len(roomData[value][0]))
        print(len(category))
        comparison=roomData[value][0].removesuffix("'").removeprefix("'")
        print(comparison)
        print(numberOfGuests)
        print(roomData[value][2])
        if comparison == str(category):
            if int(roomData[value][2]) >= numberOfGuests:
                return True, value
    return False, -1


# make a reservation
def MakeReservation(roomData):
    category = int(input("enter the room category you want to book: \n \t\t Enter 1 for Wonderful \n\t\t Enter 2 for "
                         "Marvelous \n\t\t Enter 3 for Spectacular \n\t\t Enter 4 for Fantastic \n\t\t Enter 5 for "
                         "fabulous  \n\t\t  "))
    categoryprovided = ""
    if category == 1:
        categoryprovided = "Wonderful"
    elif category == 2:
        categoryprovided = "Marvelous"
    elif category == 3:
        categoryprovided = "Spectacular"
    elif category == 4:
        categoryprovided = "Fantastic"
    elif category == 5:
        categoryprovided = "Faboulous"
    number_of_guest = int(input(" enter the number of guests for the room category: "))
    duration = int(input(" enter the duration in which the guests will stay: "))
    availability, roomindex = check_availability(roomData, categoryprovided, number_of_guest)
    if availability:
        totalprice = CalculatePrice(roomData, duration, roomindex)
        print("The Total price is ", totalprice)

        roomData[roomindex][6] = str(int(roomData[roomindex][6]) + 1)
        UpdateTextFile(roomData)
    else:
        print("we are sorry, there are no rooms available")


def CheckOut(roomData):
    category = input("please enter the room category you would like to check out for: ")
    guest_numbers = int(input("please enter the number of guests staying: "))
    availability, roomindex = check_availability(roomData, category, guest_numbers)

    if availability:
        roomData[roomindex][6] = str(int(roomData[roomindex][6]) - 1)
        UpdateTextFile(roomData)
    else:
        print("We are sorry there are no rooms available")


def Menu():
    print("#################################")
    print("....Welcome to Fancy Hotel........")
    print("##################################")
    print("/n/n/n")
    print("1. Make a new reservation")
    print("2. Check out of a room")
    print("3. Create a summary")
    print("4. Exit")


def GetChoice():
    choice = int(input("Please enter your choice:   "))
    return choice


def HandleChoice(choice, roomData):
    if choice == 1:
        MakeReservation(roomData)
    elif choice == 2:
        CheckOut(roomData)
    elif choice == 3:
        CreateSummary(roomData)
    elif choice == 4:
        print("Thank you for using the system")
        exit()
    else:
        print("invalid input, try again")


def RunProgram():
    roomData = LoadDetails()
    choice = 0
    while choice != 4:
        Menu()
        choice = GetChoice()
        HandleChoice(choice, roomData)


RunProgram()
