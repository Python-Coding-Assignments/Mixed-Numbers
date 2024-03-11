from Functions import secondIndex

def validIndex(numbers, userInput = "null"):
    """This function gets the user to input a valid date index from the user's defined list containing at least one object of type Date.  The function takes in two parameters: one called dates which is a mutable list containing elements of type Date and the other is a default value which will contain the value "null" if another value is not provided within the function's call"""

    #declaration and initialization of variables
    validIndex = 0

    #conditional statement which evaluates to True if the length of dates is greater than one and the user input is either "2", "3", "4", "6", or "7"
    if len(numbers) > 1 and (userInput == "2" or userInput == "3" or userInput == "null"):
        print("Here is a list of dates that you created.")

        #for loop which iterates over the integers between zero, inclusive, and the length of the dates list, exclusive
        for i in range(0, len(numbers)):
            #conditional statement which evaluates to True if i is equal to zero
            if i == 0:
                print("-------------------------------")

            print("Mixed Number " + str(i) + ": ", end="")
            numbers[i].show()
            print()

            #conditional statement which evaluates to True if i is equal to one less than the length of dates
            if i == (len(numbers) - 1):
                print("-------------------------------\n") 

        #calling implementMenu7 function to get valid date index
        validIndex = secondIndex.secondIndex(numbers)  
    
    #returning validIndex
    return validIndex    