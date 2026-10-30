# print("hello world")

# x = 32
# y = -3.142
# print(x, "is an integer and the data type is: ", type(x))
# print(y, "is a float and the data type is: ", type(y))

# print("Testing for True in Boolean",10 > 9)
# print("Testing for False in Boolean",3 < 1)
# c = True
# d = False
# print("Start Engine ", d)

# print("The memory location of x in my processor is: ", id(x))
# print("The memory location of d in my processor is: ", id(d))

# e = "a"
# vowels = ("a", "e", "o", "u", "i", "x")
# print(vowels[-1])
# print(vowels, "what is the data type", type(vowels))

# mylist = ["book", "pen", True, False, 28, -34.56]
# print("This is my list", mylist, type(mylist))

# myset = {1,1,2,2,3,3,5}
# print(myset, "the data type is ", type(myset))

# car = {
#     "make" : "BMW",
#     "model": 320,
#     "year": 2026,
#     "Trans": "Auto",
#     "4wd": True
# }

# print("my dictionary is", car, type(car))
# print(car.keys())
# print(car.values())

# a = 1; b=2; c=3
# print("hello python")
# print(b)

# #literal method
# a_list =[2, 3 ,7, None]
# print("first item at index 0 is: ", a_list[0])

# co_list = list(vowels)
# print("The constructor list", co_list)

# legends = ["Groucho", "Chico", "Harpo", "Carlin", "Pryo"] 
# print(legends[2:3])

# legends.append("Mr Ben")
# print("Our new refreshed list", legends)

# legends.remove("Chico")
# print("Our list after deletion:", legends)
# #carl, harp, chic

# games = ["Atari", "Nintendo", "Gameboy","Sega"]
# print("The created gams list: ",games)
# games.insert(1, "Playstation")
# print("The new game list ", games)

# eng2esp = {"one": "uno", "two" :"duo", "three": "tres"}
# countries = {}
# countries["UK"] = "Europe"
# countries["China"] = "Asia"
# countries["Namibia"] = "Africa"
# print(eng2esp.keys(),eng2esp.values(),"\n", countries)

# apps = dict(twitter="USA", tiktok="China", faceapp= "Russia")
# print(apps)

# list_items =[ ["sky", "blue"], ["cloud", "rain"], ["sun","hot"]]
# print("Dictionary created from list", dict(list_items))

# avengers = {
#     "JoshBroslin" : "Thanos",
#     "RobertDJ": "Iron Man",
#     "ChrisEvans": "Capt America"
# }
# print("at the time of creation", avengers)
# others = {"loki": "Tom Hidelston", "Spiderman": "Tom Holland"}
# print("JoshBroslin" in avengers)
# print("loki" in avengers)

# avengers.update(others)
# print("The new updated avengers dictionary: ", avengers)

# print(avengers["loki"])
# print(avengers.get("Spiderman"))

# del avengers["JoshBroslin"]
# print("After deleting thanos", avengers)

# Marvel = avengers.copy()
# print("A marvel production: ", Marvel)

# newtuple = tuple(legends)
# print("My new tuple", newtuple)

# set2 = {"red", "green", "blue"}
# set3 = set("letters")

# print(myset, set2, set3)

# k = {1,2,3,4,5}
# l ={3,4,5,6,7,8}

# m = k.union(l)
# print("The union of k and l sets:", m)
# print("Items in common", k&l)
# print("all items in sets", k | l)
# print(k ==l)

#======SECOND WEEK Session1===================##
# print("==SECOND WEEK CODE==")
# a,b,c = 5,3.2, "hello"
# print(a,b,c)

# current_salary = 1000
# PI = 3.143
# SPEED_OF_LIGHT= 36000000
# FirstName = "Ali"
# lastName = "Aliyu"
# print(current_salary, PI, SPEED_OF_LIGHT,
#       FirstName, lastName)

# print("show me they type of my data:","salary:",
#       type(current_salary), "PI", type(PI), "FirstName",
#         type(FirstName))

# def myFunction():
#     print("My First Function")
#     print("Ronaldo", 7)
#     print("Messi", 14)
# myFunction()   

# def add_numbers(a, b):
#     c = a + b
#     print("Result of adding two numbers", c)

# add_numbers(12,16)

# def my_email(student_id):
#     print(student_id + "@leedstrinity.ac.uk")

# my_email("2608765")

# def greet(name, msg= "Good Morning"):
#     print("Hello", name, msg)

# greet( name= "Ali", msg="Good afternoon")

# u = str(24)
# print("The data type of u us", type(u))

# def Bird(name, specie):
#     print(name, "is a ", specie)

# Bird(specie="Lahore", name= "Pigeon")

# def names(*inputs):
#     print("The youngest in the list is: ", inputs[1])

# names("John", "Henry", "Jummiy", "Ron")


# def sortList(mylist):
#     sortedlist = sorted(mylist)
#     print("The sorted list", sortedlist)

# sortList([34,56,2,7,1,98])
# sortList(["f", "c", "r", "k", "q", "a"])

# squaredFunction =lambda x: x**2
# print("My first lambda function: ",
#        squaredFunction(5))

# def sqaured(x):
#     c =  x ** 2
#     print("My output", c)

# #===========Second week Session 2=====
# print("===========Afternoon Session====")

# x = 120

# if (x > 0):
#     print("X is a positive integer")
# else:
#     print("X is 0 or less than 0, a negative no")

# passing_score = 40
# my_score= 170

# if (my_score >= passing_score):
#     print("I have passed the module with grade", 
#           my_score)

# if "Python" in ["Java", "C", "Kotlin", "Python"]:
#         print("Python in the list")

# print("Even",2%2,"Odd with remainder", 3%2)

# def checkEvenOdd(x):
#     if (x % 2 == 0):
#         print(x, "is even")
#     else:
#         print(x, "is odd")

# checkEvenOdd(15)

# for letter in "programming":
#      print(letter)

# for number in range(0, 10):
#      print(number)

# genre = ["pop", "rock", "jazz"]

# for music in range(len(genre)):
#      print("I like ", genre[music])

# numbers = [6,5,3,8]
# sum = 0
# for val in numbers:
#     sum = sum + val

# print("The sum total is",sum)

# for number in range(20):
#      if (number %2 == 0):
#           print(number, "is even")

# count = 10

# while count > 0:
#      if count == 1:
#           print("Happy New YEar 2027")
#      print(count)
#      count = count - 1

# for val in "string":
#      if val == "n":
#           break
#      print(val)
#=================Session3 Morning======================#
#print("This is week 3")

# class Car:
#     #attributes
#     make = "Mercedez"
#     model = "C-class"
#     year = 2019
#     manual= False
#     colour = "Blue"

# mycar = Car() #instance of class car
# print(mycar.make, mycar.model, mycar.year, 
#       mycar.manual, mycar.colour)

# print("Is the car manual:", mycar.manual)

# mycar.colour =  "green"
# mycar.model = "S-class"

# print("My car option is", mycar.colour, mycar.model)

# mycar2 = Car()
# print(mycar2.make, mycar2.model, mycar2.year, 
#       mycar2.manual, mycar2.colour)

# class vehicle(object):

#     def __init__(self, make, model, year, manual,
#                   colour, speed):
#         self.make = make
#         self.model = model
#         self.year = year 
#         self.manual = manual
#         self.colour = colour
#         self.speed = speed

#     def accelerate(self):
#         print("The car is accelerating at" ,self.speed
#               , "mph")
#         self.speed = self.speed + 30
#         print("The car is moving at" ,self.speed
#                       , "mph")

#     def stop(self):
#         print("Applying breaks")
#         self.speed = self.speed - 15
#         print("The car is moving at" ,self.speed
#                               , "mph")

#     def turnRight(self):
#         print("The car is turning right")

#     def getSpeed(self):
#         print("The current speed :", self.speed, "mph")

#     def getColour(self):
#         print("The colour of the car: ", self.colour)

#     def setTrans(self, trs):
#         self.manual= trs
#         print("Transmission of the car", self.manual)

#     def setYear(self, yr):
#         self.year = yr
#         print("Year :", self.year)

#     def carSound(self):
#         print("Sound of my car {} at full speed".format("vroom vroom"))

#     def carModel(self, model="A6"):
#         self.model = model
#         print(" {} is the new model".format(self.model))

# firstCar = vehicle("Audi","A3", 2020, True, "red", 0)
# secondCar = vehicle("BMW", 320, 2021, True, "black", 0)

# print("Make:", firstCar.make, "model:", firstCar.model,
#       "year:", firstCar.year, "manual:", firstCar.manual,
#       "Colour:", firstCar.colour)

# firstCar.accelerate()
# firstCar.stop()
# firstCar.turnRight()
# firstCar.getSpeed()
# firstCar.getColour()
# firstCar.setTrans("Automatic")
# firstCar.setYear(2026)
# firstCar.carSound()
# firstCar.carModel()

# print("My name is {} , I am {} years old, work with {}".format("John", 21, "ebay"))

##============SESSION 3 AFTERNOON==========
# print("Session 3 afternoon")

# class Employee(object):
#     companyName = "Github"

#     def __init__(self, name, id, salary):

#         self.name  = name
#         self.id = id
#         #self.__salary = salary   no access/modification
#         self.salary = salary

#     def show(self):
#         print("My name is: ", self.name, "with ID:", self.id,
#                "and salary", self.salary)

#     @staticmethod
#     def department(dpt):
#         print("The employee's department is", dpt)

#     @classmethod
#     def placeOfWork(cls, name):
#         print("This is the name of the company", Employee.companyName)
#         Employee.companyName = name
#         print("My new place of work is", Employee.companyName)

#     def setDetails(self, id, salary):
#         print("Current salary", self.salary, "Current_ID", self.id)
#         self.id = id
#         self.salary = salary
#         print("New:","Current salary", self.salary, "Current_ID",self.id)

#     def printEmail(self):
#         print("Employee email:", self.name + "@microsoft.com")


# emp1 = Employee("JohnDoe", "AB555", 1500)
# emp1.show()
# print("Accessing salary from outside",emp1.salary)
# emp1.department("Accounting")
# emp1.placeOfWork("Microsoft")
# emp1.setDetails("ZZ222", 2000)
# emp1.printEmail()

# class Circle(object):

#     def __init__(self, area, size):
#         self.area = area
#         self.size = size

#     def __add__(self, other):
#         return self.area + other.area, self.size + other.size

#     def __sub__(self,other):
#         return self.area - other.area

#     def __truediv__(self,other):
#             return self.area / other.area

#     def __lt__(self,other):
#                 return self.area < other.area
    
# c1 = Circle(14, "small")
# c2 = Circle(10, "large")

# print("Area for C1:", c1.area, "Area for C2:", c2.area)
# print("Addition of two circle areas", c1 + c2)
# print("Subtraction of two circle areas", c1 - c2)
# print("Division of two circle areas", c1 / c2)
# print("Two circles comparison", c1 < c2)

# class Shark(object):

#     def swim(self):
#         print("The shark is swimming")

#     def swimbackwards(self):
#         print("Can't swim backward but can sink backward")

#     def skeleton(self):
#          print("The shark's skeleton is made up cartilage")


# class eelfish(object):

#     def swim(self):
#         print("The eelfish is swimming")

#     def swimbackwards(self):
#         print("Eelfish can swim backward")

#     def skeleton(self):
#          print("The eelfish's skeleton is made up bones")

# s1 = Shark()
# e1 = eelfish()

# for fish in (s1, e1):
#      fish.swim()
#      fish.swimbackwards()
#      fish.skeleton()

# class Nigeria(object):

#     def capital(self):
#         print("The capital of Nigeria is Abuja")
    
#     def language(self):
#         print("English is the official language")

#     def continent(self):
#         print("It is in Africa")

# class France(object):

#     def capital(self):
#         print("The capital of France is Paris")
    
#     def language(self):
#         print("French is the official language")

#     def continent(self):
#         print("It is in Europe")


# c1 = Nigeria()
# c2 = France()

# for country in (c1, c2):
#      country.capital()
#      country.language()
#      country.continent()
# #==========SESSION4_FRIDAY=================
# print("====SESSION 4 FRIDAY MORNING=====")

# class Bird(object):
#     msg2 = "Global variable of Bird's class"

#     def fly(self):
#         message =" The bird is flying" #local variable
#         return message

# sparrow = Bird()
# print(sparrow.msg2)
# #print(sparrow.message)

# class Aircraft(object):

#     def __init__(self, name , model, capacity, speed, engine):
#         self.name = name 
#         self.model =model
#         self.capacity = capacity
#         self.speed = speed
#         self.engine = engine

#     def fly(self):
#         print("The created aircraft can fly")

#     def info(self):
#         print("Make {} and Model {} ".format(self.name, self.model))
#         print("The created aircraft has {} passengers".format(self.capacity))
#         print("Engine Type {} and Speed {}".format(self.engine, self.speed))
        
# class Civilian(Aircraft):

#     def __init__(self, name, model, capacity, speed, engine, wings):
#         super().__init__(name, model, capacity, speed, engine)
#         self.wings = wings
        

#     def passengerSeat(self):
#         print("There are more seats in civilian aircraft")
#         print("Wingspan is {}".format(self.wings))

#     def runwayLength(self, length):
#         print("The runway length for {} {} is {} feet".format(self.name,
#               self.model, length))

   

# Airbus = Civilian("Airbus", "A380", 800, "1000km/h", "Rolls-Royce", "80m")
# Airbus.fly()
# Airbus.passengerSeat()
# Airbus.info()
# Airbus.runwayLength(7250)

# class FighterJet(Aircraft):

#     def runwayLength(self, length):
#             print("The runway length for {} {} is {} feet".format(self.name,
#                   self.model, length))

#     def stealthMode(self):
#         print("The {} {} can operate in stealth mode".format(self.name,
#             self.model))


# f16 = FighterJet("F16", "X34R", 2, "2414 km/h", "Turbo")
# f16.runwayLength(2250)
# f16.info()
# f16.stealthMode()

# class Radio(object):

#     def __init__(self, make, model, channel):
#         self.make = make
#         self.model = model
#         self.channel = channel

#     def tuneChannel(self):
#         print("Tuning my radio to BBC")

# class Camera(object):

#     def __init__(self, name, lens, pixels):
#         self.name = name
#         self.lens = lens
#         self.pixels = pixels

#     def snapMethod(self):
#         print("Parent method for snapping")

# class cellPhone(Radio, Camera):

#     def __init__(self, make, model, channel, name, lens, pixels, year):
#         Radio.__init__(self,make, model, channel)
#         Camera.__init__(self, name, lens, pixels)
#         self.year = year

#     def info(self):
#         print("A childclass of Radio and camera")
#         print("Phone Make {}, Model {}, Channel:{}, Camera Name: {} ".
#               format(self.make, self.model, self.channel, self.name))
#         print("The lens:{}, the pixels: {} and the year{}".format(
#             self.lens, self.pixels, self.year
#         ))


# phone1 = cellPhone("Apple","18 pro", 76.5, "sony", "QLED","4K",2026)
# phone1.snapMethod()
# phone1.tuneChannel()
# phone1.info()

# #===========Afternoon Session 4==
# print("Session 4 Afternoon Friday")

# horses = 33
# print(horses /12, "&&" , type(horses//12))
# print((1+3)**(5-2), (59*60) / 100)  

# a = 1
# b =2
# c = a + b  #ans3
# c = c+ 2    #ans5
# c += 2
# print("testiung +=",c)#7
# c-= 2
# print("testing -=", c)#5
# c/=2
# print("testing div-equal",c)#2.5
# c*=2
# print("testing *=", c)
# c**=2
# print("testing **=", c)

# print("is a greater than b:",a > b)

# e = "hello "
# e+= "world"

# print("This is testing string e", e)

# print("is a lessthan b:",a < b)
# print(" a not equal to b:",a !=b)
# print("is a greater than or equal to b:",a >= b)
# print("is a lessthan or equal b:",a <= b)
# print("is a equal to b in value and type:",a == b)

# a = 2; b=4

# if (a<0) or (b>0):
#     print("Boolean Comparison", a * b)
# else:
#     print("Something is off")

# print(10 and 20)

# print("Testing Not", not a)

# a = 10
# b = 20
# numlist = [1, 2, 3, 4, 5, 20]

# if (a not in numlist):
#     print(a, "is contained in this list")
# else:
#     print("NOT CONTAINED")

# x = 10
# y= 11
# z = 10
# print("X position in CPU memory", id(x))
# print("Y position in CPU Memory", id(y))
# print("Checking for IS", x is y)
# print("Checking or x and z", x is z)

# print("CHecking for IS NOT", x is not y)
# print("Checking for IS NOT", x is not z)
#======Week 5 Session 1 Morning=================
print("hello world")

class BankAccount(object):
    #init class
    def __init__(self, name, acct_no, sort_code, balance):
        self.name = name
        self.acct_no = acct_no
        self.sort_code = sort_code
        self.balance = balance

    #deposit method
    def deposit(self, amt):
        print("The current balance is", self.balance)
        print("I have deposited {} in my account".format(amt))
        self.balance = self.balance + amt
        print("My new account balance is", self.balance)


    def withdraw(self, amt):
        if self.balance - amt <= 0:
            print("Insufficient balance")
            print("Add credits to withdraw")

        else:    
            print("The current balance is ", self.balance)
            print("I am wihtdrawing {} from my acct".format(amt))
            self.balance = self.balance - amt
            print("My new balance", self.balance)

    def getBalance(self):
        print("Checking my Balance ", self.balance)

    def info(self):
        print(" The account holder is", self.name)
        print("Their acct no {} and sort code {}".format
              (self.acct_no, self.sort_code))
        print("The account balance is: ", self.balance)

    def creatATM(self):
        print("Card number: 1234 5678 9101 2131")
        print("EXP MM {} YYYY {}".format(10, 2030))
        print("CVV 345")
        print("Name", self.name)

    def regAddress(self, addr):
        print("Current address is:", addr )

    def PhoneNumber(self, num):
        print("My phone number is", num)

u1 = BankAccount("John Doe", 123456, "01-01-01", 0)
print("========Running Acct Deposit====")
u1.deposit(50)
print("======Running the debit function===")
u1.withdraw(40)
print("====Running the balance====")
u1.getBalance()
print("=====Info method=========")
u1.info()
print("====Creating ATM CARD")
u1.creatATM()
print("===Register Address====")
u1.regAddress("1 Travelyn Square Leeds LS1 1CX")
print("==Your Phone  Number=")
u1.PhoneNumber(11123434)

print("===BUILDING A PROMPT FOR THE BANK ACCOUNT")

name = input("Enter Your Name: ")
acct_no = input("Enter your Account Number: ")
sort_code = input("Enter your sort code: ")
balance = float(input("Enter your balance: £"))
u2 = BankAccount(name, acct_no, sort_code, balance)

while True:
    print("\n ====== BANK MENU====")
    print("1. Depoist")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Info")
    print("5. Create ATM Card")
    print("6. Register Address")
    print("7. Register Phone Number")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        amount = int(input("Enter Deposit Amount: £"))
        u2.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdraw amount: £"))
        u2.withdraw(amount)

    elif choice == "3":
        u2.getBalance()

    elif choice == "4":
        u2.info()

    elif choice == "5":
        u2.creatATM()

    elif choice == "6":
        addr = input("Enter your address")
        u2.regAddress(addr)

    elif choice == "7":
        phone = input("Enter your phone number")
        u2.PhoneNumber(phone)
        
    else:
        print("Thanks for uisng our Bank")
        exit()
























# print("=====BANK ACCT PROMPT=====")
# name = input("Enter Customer Name")
# acct = input("Enter Acct Number")
# sort_code = input("Enter Sort Code")
# balance = float(input("Your balance"))
# u2 = BankAccount(name, acct, sort_code, balance)
