# String 

# 1. string length 
string = input("Enter string : ")
count=0
for i in string:
    count = count+1
print(count)

# 2.count the character 
string = input("Enter string : ")
count_vowels = 0 
digit = 0 
count_space = 0
count_consonent = 0
count_special = 0 
for i in string:
    vowels = "AEIOUaeiou"
    if i.isdigit():
        digit += 1 
    elif i in vowels:
        count_vowels += 1 
    elif i == " ":
            count_space += 1 
    elif i.isalpha():
        count_consonent += 1 
    else:
        count_special += 1 
        
print( "digits : " + str(digit))
print( "vowels : " + str(count_vowels))
print( "consonent : " + str(count_consonent))
print( "spaces : " + str(count_space))
print( "special characters : " + str(count_special))


# 3. reverse string 
string = input("Enter string: ")
result = ""
for i in string:
    result = i + result 
print(result)


 # 4. check palindrom 
string = input("Enter string : ")
result = ""
string1 = string.lower()
for i in string1:
    result = i + result 
if string1 == result:
    print(string1," given string is a Palindrom")
else:
        print(string1," given string is not a Palindrom")
        

# 5. uppercase & lowercase 
string = input("Enter string : ")
count_upper = 0 
count_lower = 0

for i in string:
    if i.isupper():
       count_upper += 1 
    else:
        count_lower += 1 
print("Uppercase letters count : ",count_upper)
print("Lowercase letter count : ",count_lower)


# 6. replace character 
string = input("Enter String : ")
old_char = input("character to replace : ")
new_char = input("New character : ")
result = ""
for i in string:
    if i==old_char:
        result = string.replace(old_char, new_char)
print("New string : ",result)


 # 7. remove spaces 
string = input("Enter string : ")
result = ""
for i in string:
    if i == " ":
        result +=""
    else:
        result+=i 
print(result)


# 8.frequency of character 
string = input("Enter string : ")
result = ""

for i in string:
    if i not in result:
        count = 0
        for j in string:
            if i==j:
                count +=1 
        print(i,":",count)
        result+=i
        
       
# 9. first & last char 
string = input("Enter string : ")
length = len(string)
for i in range(length):
    if i==0:
        print("First char : ",string[i])
    if i==length-1:
        print("Last char : ",string[i])
        
# 10.ASCII - ord() , chr()
string = input("Enter string : ")
result = ""
for i in string:
    ASCII = ord(i)
    result = result + (i + ":" + str(ASCII) +" ")
print(result)

# 11. count words in sentence 
string = input("Enter sentence : ")
count = 0 
for i in string:
    if i==" ":
        count += 1 
print("Total words in sentence is : ",count+1)

# 12.longest word in sentence 
string = input("Enter string : ")
word = string.split() 
longest = ""
for i in word:
    if len(i) > len(longest):
        longest = i 
print(longest)


        
# 13. short word in sentense
string = input("Enter string : ")
word = string.split() 
shortest = word[0]
for i in word:
    if len(i) < len(shortest):
        shortest = i 
print(shortest) 

# 14. first lettle uppercase 
string = input("Enter sentence : ")
word = string.split()
result = "" 
for i in word :
    result += i.capitalize() + " "
print(result)
        
# 15. print duplicates characters
string = input("Enter string : ")
result =""
duplicates = ""
for i in string:
    if i not in result:
        result += i 
    else:
        if i not in duplicates:
            duplicates += i + " "
print(duplicates)

# 16. character frequence 
string = input("Enter string : ")
result = ""
count=1
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        result+=string[i-1]+str(count)
        count=1 
if len(string)>0:
    result+=string[-1]+str(count)
print(result)
        
# 17. check anagram
string1 = input("Enter 1st string : ")
string2 = input("Enter 2nd string : ")
if sorted(string1)==sorted(string2):
    print(string1,"and" ,string2,"are anagram string ")
else:
    print(string1,"and" ,string2,"are not anagram string ")


# 18. remove duplicates 
word = input("Enter string : ")
result = ""
for i in word:
    if i not in result:
        result+=i 
print(result)


# 19. check substring exits in main string 
main_str = input("Enter main string : ")
sub_str = input("Enter sub string : ")

if sub_str in main_str:
    print("Substring exists in the main string.")
else:
    print("Substring does not exist in the main string.")
    
# 20. occurence of word 
sentence = input("Enter sentence : ")
word = input("Enter word to count : ")

count = sentence.split().count(word)
print({word},"appears",{count},"times in sentence.")


# 21.valid password 
password = input("Enter password: ")

is_digit = False
is_upperchar = False
is_lowerchar = False
is_special = False

for i in password:
    if i.isdigit():
        is_digit = True
    elif i.isupper():
        is_upperchar = True
    elif i.islower():
        is_lowerchar = True
    elif not i.isalnum():
        is_special = True

length = len(password)

if length >= 8 and is_digit and is_upperchar and is_lowerchar and is_special:
    print("Your password is Valid")
else:
    print("Password not Valid, change it")

# 22. String Compression

string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

print("Compressed string:", compressed)
