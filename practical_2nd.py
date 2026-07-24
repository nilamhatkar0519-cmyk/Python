###---- for loop ----###

# 1. print natural numbers upto n
n = int(input("Enter a number : ")) 
for i in range(1, n+1):
    print(i)

# 2. print even numbers upto n 
n = int(input("Enter a number : ")) 
for i in range(1, n+1):
    if i%2==0:
        print(i)
        
# 3. print odd numbers upto n 
n = int(input("Enter a number : ")) 
for i in range(1, n+1):
    if i%2==1:
        print(i)

# 4. print 1 2 4 8 16 32...
n = int(input("Enter a number : "))
square = 1
result = str(square) + " "
for i in range(1, n+1):
    if i==1:
        square = i*square
        
    else:
        square = square*2
        result = result + str(square) + " "
print(result) 
    
    
# 5. 1 + 1/1! + 1/2! + 1/n! 
n = int(input("Enter a number : "))
fact = 1 
sum = 0
for i in range(1, n+2):
    if i==1:
        sum += 1
    else:
        num = i-1
        fact *= num
        sum = sum + (1/fact)
print(sum)

# 6. cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! ...
n = int(input("Enter a number : "))
result = 0
fact = 1
for i in range(1, n+1):
    if i==1:
        result = result + 1 
    else:
        if i%2==0:
            square = n**i 
            fact = fact * i 
            result = result - (square/fact)
        else:
            square = 

# 7. check square root is prime or not 
n = int(input("Enter a number : "))
square_root = n ** 0.5 
for i in range(2, square_root):
    if square_root % i == 0:
        print(square_root,"is not a prime number")
    else:
        print(square_root,"is a prime number")
        
# 8. A B C
#    A B C 
#    A B C 

n = int(input("Enter a number : "))
for i in range(1, n+1):
    x = " "
    for j in range(0, n):
        x = x + chr(65 + j) + " "
    print(x)

# 9.   A
#      A B 
#      A B C
n = int(input("Enter a number : "))

for i in range(1, n+1):
    row = " "
    for j in range(i):
        row = row + chr(65 + j) + " "
    print(row)

# 10.  A B C
#      A B 
#      A
n = int(input("Enter a number : "))
for i in range(n , 0):
    for j in range(i):
        print(chr(65 + j) , end=" ")
    print()
            
# 11. 1
#     1 2 

n = int(input("Enter a number : "))
for i in range(1, n+1):
    for j in range(i):
        print(j , end=" ")
    print()
    
# 12. 1
#     2 2
n = int(input("Enter a number : "))
for i in range(1, n+1):
    print((str(i) + " ")*i)
    
