    ## data types in python 

#1. string(str)
print(type("Hello World!!"))

#2. integer(int)
number = 70
print(number)
print(type(number))

#3. float
number = 53.7
print(number)
print(type(number))


#4. boolean(bool) -> True or False
value = True 
print(value)
print(type(value))


#5. list[] -> mutable
fruits = ["apple", "banana", "mango", "grapes"]
print(fruits)
print(type(fruits))


#6. tuple() -> immutable 
numbers = (1, 2, 3, 4, 5, "nilam")
print(numbers)
print(type(number))

#7. dic{} -> key:value 
marks ={"maths":98, "physics":96, "chemistry":99}
print(marks)
print(type(marks))

#8. set{} -> 
letters = {"a", "a", "b", "c", "c"}
print(letters)
print(type(letters))



    ##conditional statements
#if 
age = 19
if age>=18:
    print("You're eligible for VOTE.")
    
# if-else
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

#if-elif-else
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
else:
    print("Adult.") 
    


    ##Looping statements

#for loop
number = 10 
for i in range(1, number+1):
    i = 2*i 
    print(i) 

#while loop 
number = 5 
while number > 0 :
    number -= 1
    print("Hello")
    
#for-else 
number = 6 
for i in range(1,number+1):
    print(i)
else:
    print("Break")
    
#while-else 
number = 5 
sum = 0 

while number > 0:
    sum += number 
    number -= 1 
else:
    print("loop end.. sum = ", sum)
