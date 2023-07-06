
#1. loop through all data
#2. if person is less than 16, count them
#3. did they die? if they survived count them
#4. return the total kids that survived / total kids *100 >> # that survived
# pid surv class name sex age

def kidz(data):
    numkidz = 0
    kidzlive = 0
    for r in data:
        temp = r.split(",")
        if (temp[6] != ""):
            if (float(temp[6])  < 16.0):
                numkidz = numkidz + 1
                if (temp[1] == "1"):
                    kidzlive = kidzlive + 1
    return round((kidzlive / numkidz) * 100, 1)
                

file = open("titanic.csv","r") # r = read w = write
cols = file.readline()# get first line , and reposition pointer
data = file.readlines()# grab all remaining data >> list
file.close()

print(cols)
print(data[0])
print(str(kidz(data)) + "% survived")






