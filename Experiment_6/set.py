n = int(input("Enter number of elements: "))

my_set = set()

# 1. add()
def add_fun(n):
    print("\n-- add() --")

    for i in range(n):
        value = int(input("Enter value: "))
        my_set.add(value)

    print("Set:", my_set)


# 2. remove()
def remove_fun():
    print("\n-- remove() --")

    value = int(input("Enter value to remove: "))

    if value in my_set:
        my_set.remove(value)
        print("After removing:", my_set)
    else:
        print("Value not found")


# 3. discard()
def discard_fun():
    print("\n-- discard() --")

    value = int(input("Enter value to discard: "))

    my_set.discard(value)

    print("After discard:", my_set)


# 4. pop()
def pop_fun():
    print("\n-- pop() --")

    if len(my_set) > 0:
        value = my_set.pop()
        print("Removed value:", value)
        print("After pop:", my_set)
    else:
        print("Set is empty")


# 5. length
def length_fun():
    print("\n-- len() --")

    print("Length of set:", len(my_set))


# 6. membership
def search_fun():
    print("\n-- search --")

    value = int(input("Enter value to search: "))

    if value in my_set:
        print("Value found")
    else:
        print("Value not found")


add_fun(n)
length_fun()
search_fun()
remove_fun()
discard_fun()
pop_fun()