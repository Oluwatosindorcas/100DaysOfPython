# # # # # # print("Hello world")
# # # # # # name = input('What is your name?')
# # # # # # print(name + ' ' + ' good to see you')
# # # # # # entry = input('Enter something: ')
# # # # # # print(entry)
# # # # # #
# # # # #
# # # # #
# # # # # # _num1 = 20
# # # # # # print(_num1)
# # # # #
# # # # # # # #Addition
# # # # # x = 10
# # # # # y = 3
# # # # # #Addition
# # # # # z = x + y
# # # # # # #
# # # # # print(z)
# # # # # # #
# # # # # # # #subtraction
# # # # # z = x - y
# # # # # print(z, type(z))
# # # # # #
# # # # # # #multiplication
# # # # # z = x * y
# # # # # print(z, type(z))
# # # # #
# # # # # #division, result is always in float
# # # # # x = 10
# # # # # y=3
# # # # #
# # # # # z = x /y
# # # # # print(z, type(z))
# # # # #
# # # # # #floor division // returns the whole numbers and ignore the remainder
# # # # #
# # # # # z = x // y
# # # # # print(z, type(z))
# # # # #
# # # # # #modulus % ignores the actual value and return the remainder
# # # # #
# # # # # z = x % y
# # # # # print(z, type(z))
# # # # #
# # # # # #power **
# # # # # z = x ** y
# # # # # print(z, type(z))
# # # # import math
# # # #
# # # # # Math function
# # # #
# # # # print(math.pi)
# # # # print(math.sqrt(16))
# # # # print(math.cbrt(8))
# # # # print(math.pow(2, 3))
# # # # print(math.pow(5, 5))
# # #
# # # # Assignment 1 - Type all the math methods, constants, what they do and how they are used and example of each
# # #
# # # #always import the library
# # # # import random
# # # # #
# # # # print(random.random()) #give random numbers between 0 - 9. and not 10
# # # # print(random.random() * 10 )
# # # # #
# # # # print(random.randint(1,6)) # generate random numbers between two diff integer
# # # # #
# # # # import math
# # # # # # now we dont decimal points in our number, so we import the math library to use the floor function.
# # # #
# # # # rand = math.floor(random.random())
# # # #
# # # #
# # # # rands = math.floor(random.random() * 10) + 1
# # # # #to generate random excluding the zero so we added the plus 1
# # # # #also the .floor function is to ensure that we dont have decimals
# # # # print(rand)
# # # # print(rands)
# # #
# # # #PEMDAS
# # # #print(2+3 * 5)
# # # #calculate the simple interest where principal is 100000
# # # # principal = 100000
# # # # rate = 7.5
# # # # time = 6
# # # # simpleInterest = (principal * rate * time) / 100
# # # # print(simpleInterest)
# # # #
# # # # #volume of a cylinder
# # # # import math
# # # #
# # # # pie = math.pi
# # # # #print(pie)
# # # # rad = 3
# # # # radius = rad * rad
# # # # height = 5
# # # # #calculate the volume of a cylinder where radius is 3cm and height is 5cm
# # # # volumeOfACylinder = pie * radius * height
# # # # print(volumeOfACylinder)
# # # #
# # # # # introduce the pow
# # # # volumeOfACylinder2 = pie * math.pow(rad,2) * height
# # # # print(volumeOfACylinder2)
# # # #
# # # # #convert kilometer to miles
# # # # #calculate the surface area of a sphere
# # # # convert temp from fahrenheit to celcius
# # #
# # # #sphere
# # # # import math
# # # # radius = 14
# # # # areaOfASphere = 4 * math.pi * math.pow(radius,2)
# # # # print(areaOfASphere)
# # # #
# # # # #kilometer to meter
# # # # kilometer = 1000
# # # # miles = kilometer * 0.621372
# # # # print(miles)
# # # #
# # # # #fahrenheit to celcius
# # # # fahrenheitValue = -40
# # # # celcius = (fahrenheitValue -32) * 5/9
# # # # print(celcius)
# # #
# # # #string
# # # # concatenation (+)
# # # # escape string (\)
# # #
# # # #  #\n for new line
# # # #
# # # # # print("This is Koya.\n" +  "Koya is a girl")
# # # # #
# # # # name = "John Doe"
# # # # # print(name, len(name))
# # # # #
# # # # # print(name[5:8])
# # # # print(name[7::-1])
# # # #
# # # words = "It's Tobiloba Folly birthday so he is getting us twenty pizzas"
# # # # print(len(words))
# # # # print(words[56:61])
# # # # print(words[-6:-1])
# # # # print(words[62::-1])
# # # # print(words[12:4:-1])
# # # # print(words[-50:-58:-1])
# # # #
# # #
# # # # #string methods
# # # # state = 'Lagos'
# # # # print(state.count('a'))
# # # # print(words.count('i'))
# # # # print(words.lower())
# # # # print(words.upper())
# # # #
# # # # p = 200000
# # # # r = 7.5
# # # # t = 3
# # # # i = (p * r * t) / 100
# # # # print("The interest of" + str(p) +  "at the rate of" + r + "within" + t + "months will be" +  i)
# # #
# # #
# # # #Type casting/conversion
# # # # int()
# # # # float()
# # # # str()
# # # # list()
# # # # bool()
# # # # tuple()
# # # # set()
# # # # frozenset()
# # # # dict()
# # # # p = float(input("Enter principal value: "))
# # # # r = float(input("Enter the rate value: "))
# # # # t = float(input("Enter the number of months: "))
# # # #
# # # # i = (p * r * t)/100
# # # #
# # # # #print("The interest of " + str(p) + "at the rate of" + str(r) + "within" + str(t) + "months will be" +  str(i))
# # # # #.format eradicate you from type casting
# # # # print("The interest of {0} at the rate of {1} within {2} month will be {3}" .format(p,r,t,i))
# # # #
# # # # print(f"The interest of {p} at the rate of {r} within {t} month will be {i}")
# # #
# # # #logical operator
# # # #AND - all entries has to be true
# # # #OR - at least one of the
# # #
# # # #comparison operator
# # # x = 10
# # # y = 3
# # # #greater than
# # # print(x > y)
# # #
# # # #data structure - list
# # # student1 = "Koya"
# # # student2 = "Nelson"
# # # student3 = "Olayinka"
# # # student4 = "Damilare"
# # # student5 = "Lolu"
# # #
# # students = ["Koya", "Nelson",["Kelvin", "Bayo"], "Olayinka", "Damilare", "Lolu",]
# # #
# # # print(students)
# # # print(students.append("oluwatosin"))
# # # print(students)
# # # students.pop(1)
# # # # print(students)
# # # students.reverse()
# # # print(students)
# # print(students[2][1])
#
# #tuple is immutable cant be changed like lists
# # #subjects = ("Maths", "English","Physics","Chemistry", "Biology")
# #
# # #set ;
# # subjects = {"Maths", "English", "Physics", "Chemistry", "Biology", "Biology"}
# #print(subjects)
#
# #dict
# person = [
#     {
#     "name": "Adeola",
#     "age": "23",
#     "sex": "female",
#     "marital_status": "married",
#     "hobbies": ["reading", "coding","singing","dancing"]
# },
# {
#     "name": "Adeolu",
#     "age": "33",
#     "sex": "male",
#     "marital_status": "complicated",
#     "hobbies": ["sports", "games", "singing","dancing"]
# },
# {
#     "name": "Yomi",
#     "age": "43",
#     "sex": "male",
#     "marital_status": "single",
#     "hobbies": ["drawing", "skating","cycling","painting"]
# },
# {
#     "name": "Lola",
#     "age": "73",
#     "sex": "male",
#     "marital_status": "divorced",
#     "hobbies": ["smoking", "walking","swimming","yoga"]
# },
# {
#     "name": "Rachael",
#     "age": "63",
#     "sex": "female",
#     "marital_status": "married",
#     "hobbies": ["Reading", "washing","praying","dancing"]
# }
#
# ]
# print(person)

#control flow
#conditional statements
#boilerplate
# if(condition):
#     code block
#     print
#


# name = input("What is your name? ")
# if name.capitalize() == "David":
#     print("oh " + name + " is a beautiful name!")

# name = input("What is your name? ")
# if name.capitalize() == "David" or name[::-1] == "David":
#     print("Hello " + name)

# name = input("What is your name? ")
# if name.capitalize() == "David":
#     print("Hello " + name)
# else:
#     print(name + " is a different name than I expected")


#elif statement
# create a program that asks a user to enter amount they have in their wallets to determine which friend they can visit in three location.
#Doyin, mile2 and Okoko
#given that the tofro cost is #400, #1000 and #2000 respectively

# wallet = float(input("How much money do you have? "))
# if wallet >= 2000:
#     print("You can visit Okoko")
# elif wallet >= 1000:
#     print("You can visit mile 2")
# elif wallet >= 400:
#     print("You can visit Doyin")
# else:
#     print("Stay at home")


ussd = input("Enter your USSD code: ")
if ussd == "*123#":
    transaction = input(
        "Select preferred transaction\n"
        "1. Data\n" +
        "2. Airtime\n" +
        "3. Transfer\n"
    )
    if transaction == "1":
        pass
    elif transaction == "2":
        pass
    elif transaction == "3":
        pass

    else:
        print("Invalid selection")

else:
    print("Wrong USSD, Try again.")
