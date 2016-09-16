#Luis Moreno, Richard Stelly
#CS512: Dataming
#Assignment 1
#Purpose:
#   Write a program that uses matrices and does operations on those matrices
#file: HW_1.py

from matrix import Matrix
#Main
def main():

    dummyMatrix = Matrix(0)
    #Prompts user for Integer and handle if input is not an Integer
    userInput = dummyMatrix.getInput("Please Enter Integer >= 3: ")
    matrixSize = dummyMatrix.checkForValidInteger(userInput)

    myMatrix =Matrix(matrixSize)

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
    print "The product of the transpose of the two matrices is:"
    myMatrix.printMatrix(M1Trans_Multiply_M2Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The dot product of the transpose of the two matrices is:"
    myMatrix.printMatrix(M1Trans_DotProduct_M2Trans); print
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "The result of matrix1 divided by matrix2 is:"
    myMatrix.printMatrix(M1Trans_Divide_M2Trans); print
    print "-----------------------End Program----------------------"
if __name__ == "__main__":
    main()
