#finished part A and B move on to C


#part A

#User Input

def checkForValidInteger(arg):
    try:
        arg = int(arg)

    except ValueError:
        print "Not a Valid Interger. Please Enter An Integer (:"

    return arg

def fillMatrixFromFile(file, userInput):
    matrixSize = userInput * userInput
    numbersList = []
    count = 0
    try:
        numbersFile = open(str(file), "r")
        for line in numbersFile:
            for i in line.split():

                count += 1

                numbersList.append(int(i))

                number = int(i)

                if count == matrixSize:
                    break

            if count == matrixSize:
                break

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

    #verify theres enough elements in the file
    if(len(numbersList) < matrixSize):
        print "Not Enough Numbers In File: %s" % (file)
        exit()

    #create an empty matrix
    w, h = userInput, userInput
    matrix = [[0 for x in range(w)] for y in range(h)]

    #counter to increment throuh
    count = 0
    #fill matrix with numbers from file
    for i in range(userInput):
        for j in range(userInput):
            matrix[i][j] = numbersList[count]
            count += 1

    return matrix

#getInput
#Prompts the User for Input
#
#
def getInput(arg):
    userInput = raw_input(str(arg))
    return userInput


def main():

    #Promts user for Interger and handle if input is not an Integer
    userInput = checkForValidInteger(getInput("Please Enter Integer >= 3: "))

    matrixA = fillMatrixFromFile("Numbers1.txt", userInput)
    matrixB = fillMatrixFromFile("Numbers2.txt", userInput)

    print "___________________________"
    print matrixA
    print len(matrixA)
    #print numbersList
    #print len(numbersList)

if __name__ == "__main__":
  main()
