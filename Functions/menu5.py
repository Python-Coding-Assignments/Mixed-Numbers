from Functions import validIndex
from Functions import secondIndex

def menu5(numbers):
    """This function compares two instances of Date, which are selected by the user, and then prints some information regarding the difference.  If both dates are identical, then a statement saying so will be printed to the screen.  The function takes in one mutable argument of type list, containing elements of type Date."""
    
    #declaration and initialization of variables
    index1 = index2 = 0

    #conditional statement which evaluates to True if the length of the list called dates is greater than two
    if len(numbers) > 2:
        print("You will be prompted to enter two indices that are associated with the dates you wish to compare.")
        
        #calling validIndex function to get two valid indices from the user
        index1 = validIndex.validIndex(numbers)
        index2 = secondIndex.implementMenu7(numbers)

        #comparing two instances of Date at index1 and index2
        numbers[index1].compare(numbers[index2])

    #conditional statement which evaluates to True if the length of the list called dates is equal to two
    elif len(numbers) == 2:
        #comparing two instances of Date at index1 and index2
        numbers[0].compare(numbers[1])

    #conditional statement which evaluates to True if the length of the list called dates is one
    else:
        print("Only one date has been created; therefore, it cannot be compared to anything else.")    