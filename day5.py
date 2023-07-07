

def getKidz(data):
    numkidz = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""):
            if (float(temp[6]) < 16.0):
                numkidz = numkidz + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkidz) * 100

def getGrp(data,sex):
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        #if (temp[6] != ""):
        if (temp[5] == sex):
            numgrp = numgrp + 1
            if (temp[1] == "1"):
                numsurv = numsurv + 1
    return (numsurv / numgrp) * 100
            
            

# open our titanic database
file = open("titanic.csv","r")
cols =file.readline()
data = file.readlines()
file.close()

keepgoing = True
while(keepgoing  == True):
    key = input("w for female, k for kids, m for men, q for quit: ")
    if (key == "q"):
        keepgoing = False
        print("BYE!")
    elif (key == "w"):
        k = getGrp(data, "female")
        print(round(k,1))
    elif (key == "k"):
        k = getKidz(data)
        print(round(k,1))
    elif (key == "m"):
        k = getGrp(data, "male")
        print(round(k,1))
    else:
        print("Please enter one of the values please.")
