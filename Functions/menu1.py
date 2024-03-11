from Classes import Mixed
import string

def menu1(numbers):
    """This function enables the user to create a date and provides implementation to ensure a valid date is inputted by the user.  The function takes in one mutable argument which is a list called dates containing elements of only type Date"""

    #declaration and initialization of local variables
    mixedNum = whole = numerator = denominator = ""
    numWhiteSpaces = numBackSlashes = 0
    flag = flag2 = False
    mixedObject = Mixed()

    print("You are now creating a new mixed number!\nEnter the mixed number in one of the following formats:")

    #for loop which iterates over the variables between zero, inclusive, and five, exclusive
    for i in range(0, 5):
        #conditional statement which evaluates to True if i is equal to either zero or four
        if i == 0 or i == 4:
            print("------------")

        #conditional statement which evaluates to True if i is equal to one    
        elif i == 1:
            print("|  3 4/5   |")

        #conditional statement which evaluates to True if i is equal to two    
        elif i == 2:  
            print("| -4 1/20  |")   

        #conditional statement which evaluates to True if i is equal to three     
        else:
            print("| 0 34/456 |")

    print("* Note, there must be a space separating the integer and the function. There must be a backslash separating the fraction's numerator and denominator. *")

    #while loop which runs until flag is no longer equal to False
    while flag == False:
        #getting mixed number entry from user and stripping whitespaces from both ends of the user's input
        mixedNum = input("Mixed Number Entry > ")
        mixedNum.strip()

        #for loop which iterates over the integers between zero, exclusive, and the length of mixedNum, exclusive
        for i in range(0, len(mixedNum)):
            #conditional statement which evaluates to True if the character at index i in mixedNum is not contained in the predefined list string.digits and is not equal to "/"
            if mixedNum[i] not in string.digits and mixedNum[i] != "/" and mixedNum[i] != " " and mixedNum[i] != "-":
                flag2 = True

        #conditional statement which evaluates to True if flag2 is equal to False
        if flag2 == False:
            #for loop which iterates over the integers between zero, exclusive, and the length of mixedNum, exclusive
            for i in range(0, len(mixedNum)):
                #conditional statement which evaluates to True if numBackSlashes is equal to zero and the character at index i of mixedNum is not equal to "/"
                if numWhiteSpaces == 0 and mixedNum[i] != " ":
                    whole += mixedNum[i]

                #conditional statement which evaluates to True if numBackSlashes is equal to one and the character at index i of date is not equal to "/"    
                elif numWhiteSpaces == 1 and numBackSlashes == 0 and mixedNum[i] != "/":
                    numerator += mixedNum[i]
                
                #conditional statement which evaluates to True if numBackSlashes is equal to two and the character at index i of date is not equal to "/"
                elif numWhiteSpaces == 1 and numBackSlashes == 1:
                    denominator += mixedNum[i]
                
                #conditional statement which evaluates to True if the character at index i of date is equal to "/"
                elif mixedNum[i] == " ": 
                    numWhiteSpaces += 1  

                #conditional statement which evaluates to True if the character at index i of date is equal to "/"
                elif mixedNum[i] == "/": 
                    numBackSlashes += 1        
            
            #conditional statement which evaluates to True if the following conditions are met
            if numBackSlashes == 1 and numWhiteSpaces == 1 and len(whole) > 0 and len(numerator) > 0 and len(denominator) > 0:
                #conditional statement which evaluates to True if the function validDate returns True
                if mixedObject.validMixed(int(whole), int(numerator), int(denominator)) == True:
                    #setting month, day, and year to instance of date and appending this instance to list called dates
                    mixedObject.setter(int(whole), int(numerator), int(denominator))
                    numbers.append(mixedObject)

                    flag = True

                #conditional statement which evaluates to True if the conditional statement above evaluates to False    
                else:
                    print("Invalid mixed number. Try again.")

            #conditional statement which evaluates to True if the conditional statement above evaluates to False
            else:
                print("Invalid mixed number. Try again.") 

        #conditional statement which evaluates to True if the conditional statement above evaluates to False
        else:
            print("Invalid mixed number. Try again.")      

        #resetting some local variables for next time the while loop runs
        flag2 = False
        whole = numerator = denominator = ""
        numBackSlashes = numWhiteSpaces = 0