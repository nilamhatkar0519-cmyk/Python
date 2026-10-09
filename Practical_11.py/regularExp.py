import re 

## search specific word 
text = "I am learning python programming libraries."
result = re.search("python",text)

if result:
    print(" found in given text")
else:
    print(" not found in given text")
    
## match word at beginning of text 
result = re.match("am",text)
if result:
    print("\n Match found at beginning")
else:
    print("\n Match not found at beginning")
    
    
## findall 
text1 = "cat dog rat cat cat "
result = re.findall("cat",text1)
print("\n",result)


## replace word 
result = re.sub("python","Java",text)
print("\n",result) 


## split 
fruits = "apple,banana;mango,guava,"
result = re.split(r"[,;]+",fruits)
print("\n",result)


## compile 
pattern = re.compile("python")
result = pattern.search(text)
if result:
    print("\nword found, compile successful")
else:
    print("\nword not found, not compile ")
    
## escape 
text = "Price is $100"
pattern = re.escape("$100")
result = re.search(pattern, text)
if result:
    print("\nPattern found:", result.group())
else:
    print("\nPattern not found")
