class Mixed:
    def __init__(self, *arguments):
        if len(arguments) == 0:
            self.__wholeNum = 0
            self.__numerator = "null"
            self.__denominator = "null"
        elif len(arguments) == 1:
            self.__wholeNum = arguments[0]
            self.__numerator = "null"
            self.__denominator = "null"
        elif len(arguments) == 3:
            if self.validMixed(arguments[0], arguments[1], arguments[2]) == True:
                self.__wholeNum = arguments[0]
                self.__numerator = arguments[1]
                self.__denominator = arguments[2] 
            else:
                self.__wholeNum = 0
                self.__numerator = "null"
                self.__denominator = "null"

    def setter(self, whole, numerator, denominator):
        if self.validMixed(whole, numerator, denominator) == True:
            self.__wholeNum = whole
            self.__numerator = numerator
            self.__denominator = denominator
        else:
            self.__wholeNum = 0
            self.__numerator = "null"
            self.__denominator = "null"

    def getWholeNum(self):
        return self.__wholeNum

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator           

    def simplify(self):
        numFactorList = []
        denFactorList = []
        maxCommonFactor = 0 

        for i in range(1, (self.__numerator + 1)):
            if self.__numerator % i == 0:
                numFactorList.append(i)

        for i in range(1, (self.__denominator + 1)):
            if self.__denominator % i == 0:
                denFactorList.append(i)  

        for i in range(0, len(numFactorList)):
            for j in range(0, len(denFactorList)):
                if numFactorList[i] == denFactorList[j]:
                    maxCommonFactor = numFactorList[i]

        self.__numerator //= maxCommonFactor
        self.__denominator //= maxCommonFactor

        while self.__numerator / self.__denominator >= 1:
            self.__numerator -= self.__denominator
            self.__wholeNum += 1     

    def show(self, default = 0):

        if default != 0:
            print("Original Mixed Number: ", end="")

        if self.__numerator != 0 and self.__wholeNum != 0:
            print(str(self.__wholeNum) + " " + str(self.__numerator) + "/" + str(self.__denominator), end=" ") 
        elif self.__wholeNum == 0 and self.__numerator != 0:
            print(str(self.__numerator) + "/" + str(self.__denominator), end=" ") 
        elif self.__wholeNum != 0 and self.__numerator == 0:          
            print(str(self.__wholeNum), end=" ")
        
        if default != 0:
            print("\n" + self.toFraction(self.__wholeNum, self.__numerator, self.__denominator))
            print(self.evaluate(self.__wholeNum, self.__numerator, self.__denominator))
            print("-------------------------------")

    @staticmethod
    def evaluate(whole, numerator, denominator):
        return ("Decimal Form: " + "{:.2f}".format(whole + (numerator / denominator)))

    @staticmethod
    def toFraction(whole, numerator, denominator):
        return ("Improper Fraction Form: " + str(numerator + (denominator * whole)) + "/" + str(denominator))
    
    @staticmethod
    def validMixed(whole, numerator, denominator):
        if denominator <= 0 or (whole < 0 and numerator < 0):
            return False
        else:
            return True  

    def compare(self, other):
        difference = Mixed()

        if self.__eq__(other) == True:
            print("Both mixed numbers are equal in value.")

        elif self.__lt__(other) == True:
            difference = self.__sub__(other)
            print("-------------------------------------")
            other.show()
            print("is greater than ", end="")
            self.show()
            print("by ", end="")
            difference.show() 
            print()
            other.show()
            print("- ", end="")
            self.show()
            print("= ", end="")
            difference.show()
            print("\n-------------------------------------")

        elif self.__gt__(other) == True:
            difference = self.__sub__(other) 
            print("-------------------------------------")
            self.show()
            print("is greater than ", end="")
            other.show()
            print("by ", end="")
            difference.show() 
            print()
            self.show()
            print("- ", end="")
            other.show()
            print("= ", end="")
            difference.show() 
            print("\n-------------------------------------")  

    def __eq__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum == otherMixed.__wholeNum and selfMixed.__numerator == otherMixed.__numerator and selfMixed.__denominator == otherMixed.__denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum != otherMixed.__wholeNum or selfMixed.__numerator != otherMixed.__numerator or selfMixed.__denominator != otherMixed.__denominator:
            return True
        else:
            return False     

    def __lt__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum <= otherMixed.__wholeNum:
            if selfMixed.__numerator / selfMixed.__denominator < otherMixed.__numerator / otherMixed.__denominator:
                return True
            else:
                return False
        else:
            return False 

    def __gt__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum >= otherMixed.__wholeNum:
            if selfMixed.__numerator / selfMixed.__denominator > otherMixed.__numerator / otherMixed.__denominator:
                return True
            else:
                return False
        else:
            return False    

    def __le__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum <= otherMixed.__wholeNum:
            if selfMixed.__numerator / selfMixed.__denominator <= otherMixed.__numerator / otherMixed.__denominator:
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        selfMixed = Mixed(self.__wholeNum, self.__numerator, self.__denominator)
        otherMixed = Mixed(other.__wholeNum, other.__numerator, other.__denominator)

        selfMixed.simplify()
        otherMixed.simplify()

        if selfMixed.__wholeNum >= otherMixed.__wholeNum:
            if selfMixed.__numerator / selfMixed.__denominator >= otherMixed.__numerator / otherMixed.__denominator:
                return True
            else:
                return False
        else:
            return False              

    def __add__(self, other):
        whole = self.__wholeNum + other.__wholeNum
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        mixed = Mixed(whole, numerator, denominator)

        mixed.simplify()    

        return mixed     

    def __sub__(self, other):
        whole = self.__wholeNum - other.__wholeNum
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator

        if numerator < 0:
            numerator *= -1
            whole *= -1

        mixed = Mixed(whole, numerator, denominator)
        mixed.simplify()  

        return mixed
    
    def __mul__(self, other):
        numerator1 = self.__numerator + (self.__denominator * self.__wholeNum)
        numerator2 = other.__denominator + (other.__denominator * other.__wholeNum)
        finalNumerator = numerator1 * numerator2
        finalDenominator = self.__denominator * other.__denominator
        mixed = Mixed(0, finalNumerator, finalDenominator)

        mixed.simplify()

        return mixed

    def __div__(self, other):
        numerator1 = self.__numerator + (self.__denominator * self.__wholeNum)
        denominator2 = other.__denominator + (other.__denominator * other.__wholeNum)
        finalNumerator = numerator1 * other.__denominator
        finalDenominator = self.__denominator * denominator2   
        mixed = Mixed(0, finalNumerator, finalDenominator)

        mixed.simplify()

        return mixed