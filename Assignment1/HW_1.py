#Luis Moreno, Richard Stelly
#CS512: Dataming
#Assignment 1
#Purpose:
#   Write a program that uses matrices and does operations on those matrices
#file: HW_1.py

from matrix import Matrix


#checkForValidInteger
# Check input from the user and validates that it is an integer grater than 3
#
def checkForValidInteger(arg):
    try:
        arg = int(arg)

        if(arg <= 3):
            print "Error: Please enter a value greater than 3. Program ends here"
            exit()
        if(arg > 6):
            print "Error: Please enter a less than 7. Program ends here"
            exit()

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

    #Prompts user for Integer and handle if input is not an Integer
    matrixSize = checkForValidInteger(getInput("Please Enter Integer >= 3: "))

    myMatrix = Matrix(matrixSize)

    M1 = myMatrix.getMatrix("file1.txt", matrixSize)
    M2 = myMatrix.getMatrix("file2.txt", matrixSize)
    M1_Multiply_M2 = myMatrix.multiply(M1, M2)
    M1_DotProduct_M2 = myMatrix.dotProduct(M1, M2)
    M1_Trans = myMatrix.transpose(M1)
    M2_Trans = myMatrix.transpose(M2)
    M1_Divide_M2 = myMatrix.divide(M1, M2)
    M1Trans_Divide_M2Trans = myMatrix.divide(M1_Trans, M2_Trans)
    M1Trans_Multiply_M2Trans = myMatrix.multiply(M1_Trans, M2_Trans)
    M1Trans_DotProduct_M2Trans = myMatrix.dotProduct(M1_Trans, M2_Trans)
    print "________________________________________________________"
    print "________________________________________________________"

    print "The content of the first matrix is:"
    myMatrix.printMatrix(M1); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The content of the second matrix is:"
    myMatrix.printMatrix(M2); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The product of the two matrices is:"
    myMatrix.printMatrix(M1_Multiply_M2); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The dot-product of the two matrices is:"
    myMatrix.printMatrix(M1_DotProduct_M2); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The result of matrix1 divided by matrix2 is:"
    myMatrix.printMatrix(M1_Divide_M2); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The transpose of the first matrix is:"
    myMatrix.printMatrix(M1_Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The transpose of the second matrix is:"
    myMatrix.printMatrix(M2_Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The dot product of the transpose of the two matrices is:"
    myMatrix.printMatrix(M1Trans_Multiply_M2Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The result of matrix1 divided by matrix2 is:"
    myMatrix.printMatrix(M1Trans_DotProduct_M2Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The result of matrix1 divided by matrix2 is:"
    myMatrix.printMatrix(M1Trans_Divide_M2Trans); print
    print "-----------------------End Program----------------------"
if __name__ == "__main__":
  main()
