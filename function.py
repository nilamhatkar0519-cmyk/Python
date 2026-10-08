
## Q.1 Factorial of any number
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

n = int(input("Enter no: "))
result = fact(n)

print("Factorial of", n, "is", result)

##Q.2 Check even or odd number
def check_even_odd(n):
    if n % 2 == 0:
        return "EVEN"
    return "ODD"

n = int(input("Enter no: "))
result = check_even_odd(n)

print("No is:", result)

## Q.3 Return greater number
def greater_no(a, b):
    if a > b:
        return a
    return b

n = int(input("Enter 1st no: "))
m = int(input("Enter 2nd no: "))
result = greater_no(n, m)
print("Greater no is:", result)

## Q.4 Calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = int(input("Enter amount: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

result = simple_interest(p, r, t)
print("Simple interest is:", result)
print("Total amount is:", p + result)

## Q.5 Check number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter no: "))
result = is_prime(n)
print("Given no is prime:", result)

## Q.6 Calculate area of circle
def area_of_circle(radius):
    if radius == 0:
        return 0
    area = 3.14 * (radius ** 2)
    return area

radius = int(input("Enter radius of circle: "))
result = area_of_circle(radius)
print("Area of circle is:", result)

##Q.7 Calculate sum of n numbers
def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)

n = int(input("Enter num: "))
result = sum_of_n(n)
print("Sum of n numbers:", result)

## Q.8 Calculate base raised to exponent
def power_n(base, exp):
    if exp == 0:
        return 1
    return base * power_n(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exp: "))
result = power_n(base, exp)
print("Power of base", base, "raised to exponent", exp, "is:", result)

## Q.9 Find largest number from list without max()
def largest_no(list_a):
    if not list_a:
        return 0
    first = int(list_a[0])
    for i in list_a:
        i = int(i)
        if i > first:
            first = i
    return first

list_a = input("Enter no separated by commas: ").split(",")
result = largest_no(list_a)
print("Largest no is:", result)

## Q.10 Calculate number of vowels from string
def no_of_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    return count

string = input("Enter string: ")
result = no_of_vowels(string)
print("Number of vowels:", result)

## Q.11 Reverse of string
def reverse_string(string):
    if not string:
        return ""
    return string[::-1]

string = input("Enter string: ")
result = reverse_string(string)
print("Reverse string:", result)


## Q.12 Check palindrome or not
def check_palindrom(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return "Palindrome"
    return "Not Palindrome"

string = input("Enter string: ")
result = check_palindrom(string)
print(result)

## Q.13 Average of numbers
def avg_of_num(list_a):
    if not list_a:
        return 0
    length = len(list_a)
    total = 0
    for i in list_a:
        i = int(i)
        total += i
    return total / length

list_a = input("Enter numbers separated by commas: ").split(",")
result = avg_of_num(list_a)
print("Avg of numbers:", result)


## Q.14 Count occurrence of given element
def count_element(list_a, element):
    count = 0
    for ch in list_a:
        if ch == element:
            count += 1
    return count

list_a = input("Enter string: ")
element = input("Enter character: ")
result = count_element(list_a, element)
print("Count of character:", result)

## Q.15 Return unique elements
def unique_element(element):
    unique_list = []
    for i in element:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

element = input("Enter elements separated by commas: ").split(",")
result = unique_element(element)
print("Unique elements:", result)

## Q.16 Find second largest number in list
def sec_large(list_a):
    sort_list_a = sorted(set(list_a))
    return sort_list_a[-2]

list_a = list(map(int, input("Enter list separated by space: ").split()))
result = sec_large(list_a)
print("Second largest no:", result)

## Q.17 Fibonacci series of n numbers
def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_series(n - 1) + fibonacci_series(n - 2)

n = int(input("Enter no: "))
print("Fibonacci series:", end=" ")
for i in range(n):
    print(fibonacci_series(i), end=" ")
    

## Q.18 Return percentage and grade of 5 subjects
def per_grade(marks):
    total_marks = 0
    for i in marks:
        total_marks += int(i)
    per = total_marks / 5
    if per >= 90:
        grade = "O Grade"
    elif per >= 75:
        grade = "B Grade"
    elif per >= 45:
        grade = "A Grade"
    else:
        grade = "Fail"
    return per, grade

marks = input("Enter 5 subjects marks separated by space: ").split()
per, grade = per_grade(marks)
print("Percentage:", per)
print("Grade:", grade)


##Q.19 Calculate electricity bill using units
def bill(unit):
    total = unit * 90
    return total
unit = float(input("Enter units: "))
result = bill(unit)
print("Electricity bill is:", result)

## Q.20


## Q.21 Total bill of items after discount
def item_bill(price):
    total = 0
    for i in price:
        total += int(i)
    if total <= 500:
        discount = total * 5 / 100
    elif total <= 1000:
        discount = total * 10 / 100
    else:
        discount = total * 20 / 100
    final_bill = total - discount
    return final_bill

price = input("Enter price of items: ").split()
length = len(price)
result = item_bill(price)
print("Total number of items:", length)
print("Total bill after discount:", result)


## Q.22 Return min, max, sum and average of list
def function_method(list_a):
    list_b = []
    for i in list_a:
        list_b.append(int(i))

    min_list = min(list_b)
    max_list = max(list_b)
    sum_list = sum(list_b)
    avg_list = sum_list / len(list_b)
    return min_list, max_list, sum_list, avg_list

list_a = input("Enter numbers: ").split()
minimum, maximum, total, average = function_method(list_a)
print("Minimum of list:", minimum)
print("Maximum of list:", maximum)
print("Sum of list:", total)
print("Average of list:", round(average, 2))


## Q.23 Calculate total, percentage, grade, average,
#     highest and lowest score
def cal_total(marks):
    total = 0
    for i in marks:
        total += int(i)
    return total

def cal_grade(marks):
    total = cal_total(marks)
    percentage = total / 5
    if percentage >= 90:
        return "O Grade"
    elif percentage >= 75:
        return "B Grade"
    elif percentage >= 45:
        return "A Grade"
    else:
        return "Fail"

def cal_high_lower_score(marks):
    list_a = []
    for i in marks:
        list_a.append(int(i))
    maximum = max(list_a)
    minimum = min(list_a)
    return maximum, minimum

name = input("Enter name: ")
roll_no = int(input("Enter roll no: "))
marks = input("Enter 5 subject marks: ").split()
total = cal_total(marks)

print("\nName:", name)
print("Roll no:", roll_no)
print("Total marks:", total)

percentage = total / 5

print("Percentage:", percentage)
print("Average:", round(total / 5, 2))

grade = cal_grade(marks)
print("Grade:", grade)
maximum, minimum = cal_high_lower_score(marks)

print("Highest score:", maximum)
print("Lowest score:", minimum)

## Q.24 Bank functions
def deposit(amount):
    value = int(input("Enter amount to deposit: "))
    amount = amount + value
    print("Amount deposited successfully!")
    return amount

def withdrawal(amount):
    if amount == 0:
        print("You have insufficient balance.")
    else:
        value = int(input("Enter amount to withdraw: "))
        if value > amount:
            print("Insufficient balance.")
        else:
            amount = amount - value
            print("Amount withdrawn successfully!")
    return amount

name = input("Enter your name: ")
amount = int(input("Enter initial bank balance: "))

amount = deposit(amount)
amount = withdrawal(amount)

print("Account holder:", name)
print("Total amount in bank:", amount)
