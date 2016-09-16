#Luis Moreno, Richard Stelly
#CS512: Datamining
#Assignment 1
#Purpose:
#   Write a program that uses matrices and does operations on those matices
#file: matrix.py

class Matrix():
    #constructors
    #
    def __init__(self, matrixSize):
            #create empty matrix
            myMatrix= self.createEmptyMatrix(matrixSize)

    #createEmptyMatrix
    # creates and empty matrix
    def createEmptyMatrix(self, matrixSize):
            #create an empty matrix
            w, h = matrixSize, matrixSize
            emptyMatrix = [['-' for x in range(w)] for y in range(h)]
            return emptyMatrix

    #getMatrix
    #   retreives a matrix based from file on the given size n
    #
    def getMatrix(self, fileName, N):
        matrixSize = N * N
        numbersList = []
        count = 0
        lineCounter = 0

        #open file and fill list of numbers
        try:
            numbersFile = open(str(fileName), "r")
            for line in numbersFile:
                
                for i in line.split():
                    count += 1
                    numbersList.append(i)

                    #exit file after got the need amount of numbers for matrix
                    if count == N:
                        continue
                    if count == matrixSize:
                        break

                if count == N:
                    continue
                if count == matrixSize:
                    #close file
                    numbersFile.close()
                    break
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

        #verify theres enough elements in the file
        if(len(numbersList) < matrixSize):
            print "ERROR: Not Enough Numbers In File: %s" % (fileName)
            exit()

        #create empty matrix
        matrix= self.createEmptyMatrix(N)

        #counter to increment through numbers in file
        count = 0
        #fill matrix with numbers from file
        for i in range(N):
            for j in range(N):
                matrix[i][j] = numbersList[count]
                count += 1

        return matrix

    #dotProduct
    # calcuates the dot product of two matrices
    #
    def dotProduct(self, M1, M2):
        m1Length = len(M1)
        m2Length = len(M2)

        M1_Multiply_M2 = self.createEmptyMatrix(m1Length)

        for row in range(m1Length):
            for col in range(m2Length):
                temp = float(M1[row][col]) * float(M2[row][col])
                M1_Multiply_M2[row][col] = str(temp)

        return M1_Multiply_M2

    def divide(self, M1, M2):
        m1Length = len(M1)
        m2Length = len(M2)

        M1_Divide_M2 = self.createEmptyMatrix(m1Length)

        for row in range(m1Length):
            for col in range(m2Length):
                try:
                    temp = float(M1[row][col]) / float(M2[row][col])
                    M1_Divide_M2[row][col] = temp
                except:
                    M1_Divide_M2[row][col] = 'undefined'


        return M1_Divide_M2

    #transpose
    #   transposes a given matrix
    #
    def transpose(self, M):
        mLength = len(M)

        M_Trans = self.createEmptyMatrix(mLength)

        for row in range(mLength):
            for col in range(mLength):
                M_Trans[row][col] = M[col][row]

        return M_Trans
    #multiply
    #   calcuates the multiplication of two matices
    #
    def multiply(self, M1, M2):
        mLength = len(M1)

        M1_DotProduct_M2 = self.createEmptyMatrix(mLength)

        for row in range(mLength):
            for col in range(mLength):
                temp = 0
                for k in range(mLength):
                    temp += float(M1[row][k]) * float(M2[k][col])

                M1_DotProduct_M2[row][col] = temp

        return M1_DotProduct_M2

    #Print Matrix
    #
    def printMatrix(self, M):
        mLength = len(M)

        for row in range(mLength):
            for col in range(mLength):
                print ("%9s" % M[row][col]) , "" ,

            print

#checkForValidInteger
# Check input from the user and validates that it is an integer grater than 3
#
    def checkForValidInteger(self, arg):
        try:
            arg = int(arg)

            if(arg <= 3):
                print "Error: Please enter a value greater than 3. Program ends here"
                exit()

        except ValueError:
            print "Not a Valid Interger. Please Enter An Integer (:"
            exit()

        return arg


    #getInput
    #Prompts the User for Input
    #
    #
    def getInput(self, arg):
        userInput = raw_input(str(arg))
        return userInput
#End Matrix Class
