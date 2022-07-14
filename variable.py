
#data type
from hashlib import new


x = 5
y = 4.6
a = 'Pcharles'
b = -5

print(type(x))
print(type(y))
print(type(b))

#lenght of a string
print(a[3])
print(len(a))

#booleans
print(10 > 9)
print(10 ==9)
print(10 < 9)


# if statement
A = 130
B = 87

if B > A:
    print("B is greater than A")
else:
    print("B is not greater than A")
    
#  bool, every value is true except is zero, empty string
print(bool("Boluwatife"))
print(bool(10))
print(bool())
print(bool(0))

#list
list =["apple", "banana", "mango","oranges","banana", "mango"]

print(list)
print(len(list))
print(list[3])

#tuples
this_tuple =("machinery")
print(this_tuple)

tuple = ("man", "woman","boy","girl")
print(tuple)

#set
set={"mouth", "eyes","head","ear","hair"}
print(set)
print(len(set))

#dictionaries
dictionary ={
    "brand": "Apple",
    "model": "Iphone11",
    "year": 2020,
}
print(dictionary)
print(len(dictionary))
print(dictionary["model"])

#conditional statement

e = 170
m = 130
n = 170

if e > m:
    print("E is greater than M, so relax bro")
elif e == n:
    print("the values are thesame, bro")
else:
    print("M is the highest value, nigga")
    
#while loop

i = 0
while i < 7:
     print(i)
     i += 1
else:
         print("i is no longer less than 7")

#for loop

fruit = ("apple", "mangoes", "banana", "pawpaw")
for x in fruit:
    print(x)

for b in "banana":
    print(b)
    
fruit = ("apple", "mangoes", "banana", "pawpaw")
for x in fruit:
    print(x)
else:
    print("I'm done!")
    
#function

def function():
    print('Hello, im a function')
function()

def name(name):
    print(name)
name("GERMENT")

#class

class MyClass():
    x = "Nigga we gat to work on this asap"
new = MyClass()

print(new.x)