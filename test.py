from variable import name

# Greetings
name= input("What is your name? ")
print("Hello " + name)

# Input
birth_year = input("Enter your birth year: ")
age = 2022 - int(birth_year)
print( "you are", age ,"years old" )

# Float
first= float(input("Enter Number: "))
second= int(input("Enter number 2: "))
print("Sum: ", first + second)

# String
course= 'Python for Beginners'
print(course.upper())
print(course.find("B"))
print(course.replace('for','4'))
print("Python" in course)

# Operators

x = 10
x += 3
print(x)

# Operator precedence

b = 10 + 3 * 2
B = (10 + 3) * 2 + 4
print(B)
print(b)

# Comparison Operator
c = 3 > 2
print(c)

# Logical Operator, And , Or, Not
price = 25
print(price > 10 and price < 30)

# if statement
temperature = 35
if temperature > 30:
    print("it's hot day")
    print("Drink enough water")
elif temperature > 20:
    print( "it's a nice day")
elif temperature > 10:
    print("it's bit cold")
elif temperature:
    print("its cold")
    
# Calculate weight
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() =="K":
    coverted= weight / 0.45
    print("Weight in Lbs: ", + coverted)
else:
    coverted=weight * 0.45
    print("Weight in Kgs: ", + coverted)
    
# While loop
i= 1
while i <= 5:
    print(i)
    i= i + 1
    
i= 1
while i <= 10:
    print(i * '*')
    i= i + 1

# List
names=["John","Mary", "Micheal", "Grace", "Bolu"]
names[0]="Charles"
names.append("Tife")
print(names)
print(names[3])
print(names[-2])
print(names[0:3])

# For loop

numbers= [1,2,3,4,5,6]
for item in numbers:
    print(item)

# Range

numbers = range(2,10)
for number in numbers:
    print(number)

numbers = range(5,10,2)
for number in range(5):
    print(number)
