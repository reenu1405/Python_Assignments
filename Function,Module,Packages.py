from statistics import mean
# 1- given numbers, write a program to find the mean of the numbers
#
def gettuple(*args):# for many inputs and type of args is tuple
    global l
    l = len(args)
    num = 0
    for a in args:
        num = num + a
    return num
s = gettuple(1, 2, 3, 4, 5)
print(s)
print("mean of numbers is :", s/l)
# or
# import this : from statistics import mean
def gettuple(*args):  # for many inputs and type of args is tuple
    print(args)
    m = mean(args) # use the mean function after importing statistics

    return m
s = gettuple(1, 2, 3, 4, 5)
print("Mean of the numbers is:", s)

# 2- write a Python function which takes a positive number as input and
# return the factorial of the number.
def getfact(n):
    if n < 0:
        return " Error: Number must be +ve"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num = int(input("Enter a positive number : "))
fact = getfact(num)
print("The factorial of {} is: {}".format(num, fact))
print(f"The factorial1 of {num} is: {fact}")

# 3- Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
#
# using empty lists
ss = []
ll = []
def counts(strs):
    # print(len(strs))
    for i in strs:
        if i.isupper():
            ss.append(i)

        elif i.islower():
            ll.append(i)
    print("Lowercase letters are: ", len(ll))
    print("Uppercase letters are: ", len(ss))
s1 = input("Enter the String: ")
count_str = counts(s1)

# print(count_str) : using strings
# or
def counts(strs):
    # print(len(strs))
    ss = 0
    ll = 0
    for i in strs:
        if i.isupper():
            ss += 1

        elif i.islower():
            ll += 1
    print("Lowercase letters are: ", ll)
    print("Uppercase letters are: ", ss)
s1 = input("Enter the String: ")
count_str = counts(s1)

# 4- Write a Python function that takes a list and returns a new list with
# distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
lst1 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7]
result_lst = list(lst1)

# 5- Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.
#
def palindrome(pal):
    pal = pal.lower() # Convert the string to lowercase for case insensitivity
    rev_pal = pal[::-1]  # Reverse the string
    print("reverse: ",rev_pal)
    if pal == rev_pal:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
ent = input("passed a string and check its palindrome or not: ")
result = palindrome(ent)

# 6- Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
enter_seq = input("Enter hyphen-separated sequence of words")
res1 = enter_seq.split('-') # Split the sequence into individual words
res2 = sorted(res1) # Sort the words alphabetically
print(res2)
res3 = '-'.join(res2) # Join the sorted words with hyphens
print(res3)

# Alternative method without using join()
result = ''
for word in sorted_words:
    result += word + '-'
result = result.rstrip('-')  # Remove the trailing hyphen
print("Sorted hyphen-separated sequence: ", result)

# 7- write a python function that accepts a string and prints the count of occurrence of each characters
# sample string: aabccda
# expected result:
# a -> 3
# b-> 1
# c-> 2
# d -> 1
def CountCharac(string):
    chardict = {}
    for char in string:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    for char, count in chardict.items():
        print(char, "=", count)


char_input = input("Enter the string:")
char_res = CountCharac(char_input)

# 8- write a function called is_prime that takes an integer as an argument and returns True
# if it is a prime number, and False otherwise.
#
def is_prime(number):
    if number <= 1:
        return False
    elif number%2 != 0:
        return 'True'
    else:
        return 'False'

prime_input = int(input("Enter an integer to chk its prime"))
function_result = is_prime(prime_input)
print("Is the number given prime? : " , function_result)

# 9- write a function called generate_fibonacci that takes an integer n as input and
# returns a list of the first n Fibonacci numbers.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def generate_fibonacci(n):
    fib_list = []
    if n >= 1:
        fib_list.append(0)
    if n >= 2:
        fib_list.append(1)
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])

    return fib_list

fib_n = int(input("Enter an integer: "))
fib_res = generate_fibonacci(fib_n)
print(f"Fibonacci number series for n= {fib_n} : ", fib_res)

# 10- Write a function called capitalize_odd_letters that takes a
# string as input and returns the same string with the odd-indexed letters capitalized.
#
def capitalize_odd_letters(odds):
    s = ''
    for i in odds:
        if odds.index(i)%2 != 0: # Check if the index is odd
            i = i.capitalize()
            s += i
        elif odds.index(i)%2 == 0:
            s += i
    return s
indexed = input("enter string")
index_odd = capitalize_odd_letters(indexed)
print("Modified string:", index_odd)
# or

def capitalize_odd_letters(string):
    capitalized_string = ""

    for i in range(len(string)):
        if i % 2 == 1:  # Check if the index is odd
            capitalized_string += string[i].upper()
        else:
            capitalized_string += string[i]

    return capitalized_string

# Example usage
input_string = input("Enter a string: ")
result = capitalize_odd_letters(input_string)
print("Modified string:", result)

# 11- write a function called find_common_elements that takes two lists as input and
# returns a new list containing the common elements between the two lists.
def find_common_elements(L1,L2):
    L3 = []
    for i in L1:
        for j in L2:
            if i == j:
                L3.append(i)
    return L3
list11 = input("Enter the elements separated by comma")
list1 = list11.split(',')
list21 = input("Enter the elements separated by comma")
list2 = list21.split(',')
List_result = find_common_elements(list1,list2)
print(List_result)

# or
def find_elements(L1,L2):
     common_elements = []
     for i in L1:
         if i in L2:
             common_elements.append(i)
     return common_elements
inputL1 = [1,2,35,6,7,8,9]
inputL2 = [9,76,55,88,35,2,1,77]
common = find_elements(inputL1,inputL2)
print("Common elements are: ", common)








