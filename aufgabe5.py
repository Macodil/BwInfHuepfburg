from array import *
myArray = []
myStepsS = [[1]]  # Saves all the steps Sasha is able to do
myStepsM = [[2]]  # Saves all the steps Mika is able to do


def getField():  # returns the field the players meet
    global myStepsM, myStepsS
    while (True):
        myStepsS.insert(0, sorted(set([x for next in myStepsS[0] for x in myArray[next - 1]])))  # merges all possible steps with a
        myStepsM.insert(0, sorted(set([x for next in myStepsM[0] for x in myArray[next - 1]])))  # connection to the last steps
        for e in myStepsS[0]:  # if one of the possible fields are equal,
            for g in myStepsM[0]:  # return the field
                if e == g:
                    return e
        for e in range(1, len(myStepsS)):  # if the step combination of both players happens
            if myStepsS[e] == myStepsS[0]:  # to be one, that was present before, there is no solution
                if myStepsM[e] == myStepsM[0]:
                    myStepsM = []
                    return None


def getSolution(fName):  # finds the solution to a given file
    global myArray
    with open(fName, 'r', encoding='utf-8') as file:  # reads the given textfile and creates array where fields are accessable with
        myArray = [[] for x in range(int(file.readline().split()[0]))]  # their number -1 (example field1 = myArray[1-1])
        for line in file:
            myArray[int(line.split()[0]) - 1].append(int(line.split()[1]))

    myStepsMFinal = [getField()]  # sets the meeting point as last field of the way
    myStepsSFinal = [myStepsMFinal[0]]

    for i in range(1, len(myStepsM) - 1):  # looks up in myArray which field was the one before in order to get to the present one
        myStepsMFinal.insert(0, [m for m in myStepsM[i] if myStepsMFinal[0] in myArray[m - 1]][0])
        myStepsSFinal.insert(0, [m for m in myStepsS[i] if myStepsSFinal[0] in myArray[m - 1]][0])

    myStepsMFinal.insert(0, 2)  # inserts the start fields
    myStepsSFinal.insert(0, 1)

    return myStepsSFinal, myStepsMFinal  # returns the finals lists (none if not possible)


if __name__ == '__main__':
    for i in range(5):
        print(i)
        print(getSolution('huepfburg' + str(i) + '.txt'))  # prints out the solution
        myArray = []
        myStepsS = [[1]]
        myStepsM = [[2]]