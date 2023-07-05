
def exData(blist,num):
    for r in range(1,num):
        line = blist[r]
        temp = line.split(",")
        print("Did " + temp[3] + " survive?: (" + temp[1] + "), M/F: " + temp[5] + ", Age: " + temp[6] + ", Passenger ID: " + temp[0] + ", Cabin: " + temp[11])

fi = open("titanic.csv","r")
biglist = fi.readlines()
fi.close()




print(len(biglist))
print(biglist[0])
exData(biglist,10)



# Homework, make it cooler.
