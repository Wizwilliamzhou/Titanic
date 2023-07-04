



"""

print("Hello World!")

age = 12 #this is an integer
pi = 3.14 #this is a float
name = "William" # this is a string
isawesome = True #boolean

print(age + pi)
print(age - pi)
print(age / pi)
print(age * pi)
niceoutput = round(age * pi,2)
print(niceoutput)

print(name + str(age))

print("Your name is " + name + " and your age is " + str(age) + ".")
"""

#Homework

print(" ")
print("***********************|Welcome to THE AGE GAME!|************************")
print(" ")
print("*fireworks popping* *people cheering*")
print(" ")
print("Now, let's begin! First question; ")

myask = int(input("How old are you?: "))

if (int(myask) >= 50):
    yesno = input("Well greqt! You're definitely old and probably already retired! Am I right?: ")
    if yesno == "yes":
        print(" ")
        print("Awesome! I'm so smart! ")
        print(" ")
        print("*people laughing*")
    elif yesno == "no":
        print(" ")
        print("Well at least I tried!")
        print(" ")
        print("*people laughing*")
elif (int(myask) < 50):
    if (int(myask) <= 18 and int(myask) >= 13):
        print(" ")
        print("So you're probably a teen or kid right? And you probably use social media.")
    else:
        print(" ")
        young = input("Amazing! You're pretty young am I right?: ")
        if young == "yes":
            print(" ")
            print("Awesome! I'm so smart! ")
            print(" ")
            print("*people laughing*")
        elif young == "no":
            print(" ")
            print("Well at least I tried!")
            print(" ")
            print("*people laughing*")
print(" ")
print("***********************|Thanbks for joining us!|************************")
print(" ")
print("Well thanks for joining us for the AGE GAME thanks!")



