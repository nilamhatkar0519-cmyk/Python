# function

# 1. add two numbers 
def add(a,b):
    return a+b 

a = int(input("Enter first number : "))
b = int(input("Enter seccond number : "))
result = add(a,b)
print("sum of two numbers : ", result)


# lambda function 
# 1. display the square of number 
square = lambda x: x*x 
n = int(input("Enter a number : "))
print("Square of number",n,"is : ", square(n)) 



### Array ###

# 1.append()
n = int(input("Enter array size : "))
arr = []

def append_fun(n):
    for i in range(n):
        array = int(input("Enter array : "))
        arr.append(array)
    print("\nArray : ",arr)

    length = len(arr)
    print("length of array : ", length)

# 2.insert()
def insert_fun():
    print("\n-- insert--")
    index = int(input("Enter index  : "))
    value = int(input("Enter value to insert into the array : "))
    arr.insert(index,value)
    print("after inserting, updated array: ",arr)
    
# 3. pop()
def pop_fun():
    print("\n--pop--")
    index = int(input("Enter index to remove : "))
    arr.pop(index)
    print("after pop, updated array : ", arr)
    
# 4. sort()
def sort_fun():
    print("\n-- sort --")

    arr.sort()

    print("After sorting, updated array:", arr)
    
append_fun(n)
insert_fun()
pop_fun()
sort_fun()