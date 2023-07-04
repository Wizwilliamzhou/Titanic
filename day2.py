

def getAge(age):
    cat = "baby"
    if (age <= 5):
        cat = "baby"
    elif (age > 5 and age <= 13):
        cat = "kids"
    else:
        cat = "big people"
    return cat
    
"""
myage= input("enter you rage as an integer: ")

mycat = (getAge(int(myage)))
"""


friends = ["anny", "aaron", "kc"]
friends.append("william")
friends.remove("kc")
friends.sort()
print(friends)

for f in friends:
    if (f == "aaron"):
        print(f + " is cool!")
    elif (f == "william"):
        print(f + " is the best!")
    else:
        print(f + " is ok")

for i in range(3):
    print(friends[i])

keepgoing = True

while (keepgoing == True):
    key = input("press q to quit: ")
    if (key == "q"):
        keepgoing = False
        print("bye")

# Homework HOW to dUpload your program to github:

"""
First go to profile:
press repositories
press new
give it a name "titanic"
make sure it is public
click "Add a README file"
click create
click "add file" and upload files
and drag day 1 and 2 into the box
click commit changes
DONE!

"""









