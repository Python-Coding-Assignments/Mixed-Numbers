from Functions import menu, menu1, menu3, menu4, menu5, validIndex

def implementation(userInput, numbers):
    """This function determines how the program should flow depending on the user's menu selection.  This function takes in two arguments: the user's menu selection of type string and a list of dates created by the user, containing elements of type Date"""

    #declaring and initializing variable by calling validIndex function
    index = validIndex.validIndex(numbers, userInput)

    #conditional statement which evaluates to True if the user's menu selection is "1"
    if userInput == "1":
        #calling menu1 function
        menu1.menu1(numbers)

    #conditional statement which evaluates to True if the user's menu selection is "2"
    elif userInput == "2":
        print("-------------------------------\nMixed Number " + str(index) + ":")
        numbers[index].show(1)

    #conditional statement which evaluates to True if the user's menu selection is "3"
    elif userInput == "3":
        menu3.menu3(numbers[index])   

    #conditional statement which evaluates to True if the user's menu selection is "4"
    elif userInput == "4":
        menu4.menu4(numbers)    

    #conditional statement which evaluates to True if the user's menu selection is "5"
    elif userInput == "5":
        menu5.menu5(numbers)    

    #conditional statement which evaluates to True if the user's menu selection is "6"
    elif userInput == "6":
        menu()    

    #conditional statement which evaluates to True if the user's menu selection is invalid
    else:
        print("Invalid entry.  Try again.")          