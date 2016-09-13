class Matrix():
    #constructor
    def __init__(self, matrixSize):
            #create empty matrix
            myMatrix= self.createEmptyMatrix(matrixSize)

    #createEmptyMatrix
    def createEmptyMatrix(self, matrixSize):
            #create an empty matrix
            w, h = matrixSize, matrixSize
            emptyMatrix = [['-' for x in range(w)] for y in range(h)]
            return emptyMatrix

    #getMatrix
    def getMatrix(self, fileName, N):
        matrixSize = N * N
        numbersList = []
        count = 0

        #open file and fill list of numbers
        try:
            numbersFile = open(str(fileName), "r")
            for line in numbersFile:
                for i in line.split():
                    count += 1

                    numbersList.append(i)
                    #number = i

                    #exit file after got the need amount of numbers for matrix
                    if count == matrixSize:
                        break

                if count == matrixSize:
                    #close file
                    numbersFile.close()
                    break
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

        #verify theres enough elements in the file
        if(len(numbersList) < matrixSize):
            print "Not Enough Numbers In File: %s" % (fileName)
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

    #multiply
    def multiply(self, M1, M2):
        m1Length = len(M1)
        m2Length = len(M2)

        M1_Multiply_M2 = self.createEmptyMatrix(m1Length)

        for i in range(m1Length):
            for j in range(m2Length):
                temp = int(M1[i][j]) * int(M2[i][j])
                M1_Multiply_M2[i][j] = str(temp)

        return M1_Multiply_M2

    def divide(self, M1, M2):
        m1Length = len(M1)
        m2Length = len(M2)

        M1_Divide_M2 = self.createEmptyMatrix(m1Length)

        for i in range(m1Length):
            for j in range(m2Length):
                try:
                    temp = int(M1[i][j]) / int(M2[i][j])
                    M1_Divide_M2[i][j] = temp
                except:
                    M1_Divide_M2[i][j] = 'undefined'


        return M1_Divide_M2


    def transpose(self, M):
        mLength = len(M)

        M_Trans = self.createEmptyMatrix(mLength)

        for i in range(mLength):
            for j in range(mLength):
                M_Trans[i][j] = M[j][i]

        return M_Trans

    def dotProduct(self, M1, M2):
        mLength = len(M1)
        m2_Trans = self.transpose(M2)

        M1_DotProduct_M2 = self.createEmptyMatrix(mLength)

        for i in range(mLength):
            for j in range(mLength):
                temp = 0
                for k in range(mLength):
                    temp += int(M1[i][k]) * int(m2_Trans[i][k])

                M1_DotProduct_M2[i][j] = temp

        return M1_DotProduct_M2


    def printMatrix(self, M):
        mLength = len(M)

        for row in range(mLength):
            for col in range(mLength):
                print ("%9s" % M[row][col]) , " " ,

            print

#End Matrix Class
