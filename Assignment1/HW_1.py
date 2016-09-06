#finished part A and B move on to C

from matrix import Matrix
#part A

#User Input

def checkForValidInteger(arg):
    try:
        arg = int(arg)

    except ValueError:
        print "Not a Valid Interger. Please Enter An Integer (:"
        exit()

    return arg


#getInput
#Prompts the User for Input
#
#
def getInput(arg):
    userInput = raw_input(str(arg))
    return userInput


def main():

    #Prompts user for Interger and handle if input is not an Integer
    matrixSize = checkForValidInteger(getInput("Please Enter Integer >= 3: "))

    myMatrix = Matrix(matrixSize)

    M1 = myMatrix.getMatrix("Numbers1.txt", matrixSize)
    M2 = myMatrix.getMatrix("Numbers2.txt", matrixSize)
    M1_Multiply_M2 = myMatrix.multiply(M1, M2)
    M1_Trans = myMatrix.transpose(M1)
    M1_DotProduct_M2 = myMatrix.dotProduct(M1, M1)
    m0 = myMatrix.createEmptyMatrix(4)
    M1_Divide_M2 = myMatrix.divide(M1, M2)
    print "_______________________________________________________________"
    print "_______________________________________________________________"

    print "M1:"
    myMatrix.printMatrix(M1); print
    print "M2:"
    myMatrix.printMatrix(M2); print
    print "Multiply M1 by M2:"
    myMatrix.printMatrix(M1_Multiply_M2); print
    print "Transpose M1:"
    myMatrix.printMatrix(M1_Trans); print
    print "DotProduct M1 to M2:"
    myMatrix.printMatrix(M1_DotProduct_M2); print
    print "Divide M1 by M2"
    myMatrix.printMatrix(M1_Divide_M2); print
    print "Zero Matrix"
    myMatrix.printMatrix(m0); print
    print "_______________________________________________________________"
    print "_______________________________________________________________"


if __name__ == "__main__":
  main()
