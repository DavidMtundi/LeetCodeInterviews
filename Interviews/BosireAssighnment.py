import matplotlib as plt


# Write a python function that:


# Takes a number param, converts it to a string and then iterates through it to dertermine if the number is a palindrome
class Solution(object):
    parameter = str(object)
    firstindex=0
    lastindex = len(parameter)-1
    def functionCheckPalindrom(self, parameter, firstindex, lastindex):
        if firstindex is None:
            firstindex = 0
        if lastindex is None:
            lastindex = len(parameter) - 1

        mid = int((firstindex + lastindex) / 2)
        if (mid - 1 <= firstindex) & (parameter[firstindex] == parameter[lastindex]):
            return "Palindrome"

        while firstindex < lastindex:
            if parameter[firstindex] == parameter[lastindex]:
                firstindex += 1
                lastindex -= 1
                return self.functionCheckPalindrom(parameter, firstindex, lastindex)
            else:
                return "Not Palindrome"


# Takes a file name as a paremeter and counts and returns the number of white spaces in the file name
def whiteSpacesinFile():
    filename = input("please enter the file name or path")
    file = open(filename, "r")

    count = 0
    while True:

        # this will read each character
        # and store in char
        char = file.read(1)

        if char.isspace():
            count += 1
        if not char:
            break

    return count


# Displays all numbers divisible by 5 between 1 and a number entered by the user
def displayNumbersDivisibleBy5():
    number = int(input("Enter a number"))
    arrayvalue = []
    for x in range(0, number):
        if x % 5 == 0:
            arrayvalue.append(x)
    return arrayvalue


# Takes a random number of numerical values and displays a graph based on the parameters entered.
def displayGraph():
    numberofvalues = int(input("please enter the number of rows you want to add"))
    x = []
    y = []
    print("enter the row values")
    for i in range(0, numberofvalues):
        x[i] = int(input("Number"))
    print("enter the column values")
    for j in range(0, numberofvalues):
        y[j] = int(input("Number"))

    # plotting the points
    plt.plot(x, y)

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()
