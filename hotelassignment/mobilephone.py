validmobilenumber = 971551234567
validpin = 1234
validcustomername = "Maitha Ahmad"


def Menu():
    print("#################################")
    print("....Welcome to the Mobile Phone Management System........")
    print("##################################")
    print("\n")
    print("1. Check Account Details")
    print("2. Calculate Bill")
    print("3. Change Pin")
    print("4. Quit")


def GetChoice():
    choice = int(input("Please enter your choice:   "))
    return choice


def GetCustomerDetails():
    print("......Login Stage........")
    mobilephone = int(input("Please Enter your phone Number: "))
    pin = int(input("Enter your pin please : "))
    if (mobilephone != validmobilenumber) or (pin != validpin):
        print("Incorrect Credentials, try again")
        return False
    return True


def CheckAccountDetails():
    print("......Here are your account details........")
    print("Customer Name: ", validcustomername)
    print("Mobile Number: ", validmobilenumber)
    print("PIN: ", validpin)


def CalculateBill():
    print("....Calculate your bill....")
    code = input("Service Type(code) R for Regular or P for Premium: ")
    numberofminutesR = 0
    numberofminutesP = 0
    if code == 'R':
        numberofminutesR = int(input("Regular (Number of Minutes SPENT): "))
    if code == 'P':
        numberofminutesP = int(input("Premium (Number of Minutes SPENT): "))

    Regularcharge = 20 + ((numberofminutesR - 50) * 0.2)
    Premiumcharge = 50 + ((numberofminutesP - 75) * 0.5)

    salestax = (Regularcharge / Premiumcharge) * 0.10
    Totalcharges = Regularcharge / Premiumcharge + salestax

    if numberofminutesP == 0:
        print("Your Bill is ", str(Regularcharge)+'AED')
    else:
        print("Your Bill is ", str(Premiumcharge)+'AED')


def ChangePin():

    print(".........Change your pin.............")
    newpin = int(input("Enter your new pin: "))
    validpin = newpin
    print("pin changed successfully")


def HandleChoice(choice):
    if choice == 1:
        CheckAccountDetails()
    elif choice == 2:
        CalculateBill()
    elif choice == 3:
        ChangePin()
    elif choice == 4:
        print("Thank you for using the system")
        exit()
    else:
        print("invalid input, try again")


def RunProgram():
    isloggedin = False
    count = 0
    while not isloggedin:
        isloggedin = GetCustomerDetails()
        count += 1
        if count >= 3:
            print("Incorrect credentials three times, you have been blocked\n System Exiting")
            exit()

    choice = 0
    while choice != 4:
        Menu()
        choice = GetChoice()
        HandleChoice(choice)


RunProgram()
