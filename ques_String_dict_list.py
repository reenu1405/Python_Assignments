# 1- given a list of numbers, write a program to find the mean of the numbers in list
num = [1, 4, 5, 7, 8, 9, 3, 5]
s = sum(num)
l = len(num)
print("Mean of the numbers is: ", s/l)

###################
# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list
num = [1, 4, 5, 7, 8, 9, 3, 2, 6]
num.sort()
length = len(num)
if length % 2 == 0:
    median = (num[length//2 - 1] + num[length//2])/2
else:
    median = num[length // 2]

    print("median of the numbers is: ", median)
###################
# 3- from a list of numbers create 2 list , one containing only the even numbers
# and other only the odd numbers
num = [1, 4, 5, 7, 8, 9, 3, 2, 6]
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers list: ", even)
print("Odd numbers list: ", odd)
############
# 4- create a dictionary to store following attributes of CSK
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players),
# opponent name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss
csk = {
    'team_name': 'Chennai Super Kings', 'Captain': 'MSD',
    'players': [
        ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'],#match1
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'], #match 2
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'] #match3
    ],
    'Opponents': ['RCB', 'MI', 'KKR'],
    'result': ['won', 'loss', 'won']
}

dicts1 = dict(CSK='Chennai Super Kings', Captain='MSD',
             players=['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9',
                      'player10', 'player11'], Opponents=['RCB', 'MI', 'KKR'], result=['won', 'loss', 'won'])

#
# 5- in the previous dictionary add one more item for RCB. you can choose any 3 opponents.
ipl: {
 "csk": {
    'team_name': 'Chennai Super Kings', 'Captain': 'MSD',
    'players': [
        ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'],#match1
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'], #match 2
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'] #match3
    ],
    'Opponents': ['RCB', 'MI', 'KKR'],
    'result': ['won', 'loss', 'won']
 },
 "RCB": {
    'team_name': 'Royal Challengers Bangalore', 'Captain': "Virat Kohli",
    'players': [
        ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'],#match1
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'], #match 2
['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11'] #match3
    ],
    'Opponents': ['CSK', 'MI', 'KKR'],
    'result': ['loss', 'loss', 'loss']
 }
}


# 6- write a program to take a positive number as input from user. if the user enters negative number then keep promoting him to enter positive number until he enters the positive number and then print the same
user_num2 = int(input("Enter positive number"))
while user_num2 <= 0:
    print("Input is invalid please Enter positive number")
    user_num2 = int(input("Enter positive number"))

print("Your positive num is : ", user_num2)

# 7- consider the below list of list contains following information :
#
# 1. The name of a university
# 2. The total number of enrolled students
# 3. The annual tuition fees
#
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
#
# write a program to print following information :
# 1- a list of all the universities  : ['California Institute of Technology','Harvard',..so on]

university_names = []
for university in universities:
    university_names.append(university[0])
print("List of all university names : ", university_names)


# 2- total number of student enrolled in all the universities together
students = 0
for student in universities:
    students += student[1]
print("total students : ", students)

# or
stu = []
for student in universities:
    stu.append(student[1])
print("total students2 : ", sum(stu))

# 3- mean of tuition fees
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

tuition_fee = []
for tuition in universities:
    tuition_fee.append(tuition[2])
    mean = sum(tuition_fee)/len(tuition_fee)
print("mean 1 : ", mean)


# or
tuition_fees = 0
tuition_fee = []
for tuition in universities:
    tuition_fee.append(tuition[2])
    length = len(tuition_fee)
    tuition_fees += tuition[2]
    tuition_mean = tuition_fees/length
print("tuition fee mean : ", tuition_mean)


# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

uni_dict = {}
for uni in universities:
    name = uni[0]
    attributes = {
        'total_students': uni[1],
        'tuition_fee': uni[2]
    }
    uni_dict[name] = attributes
print(uni_dict)

# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"
user = input("Enter your string")
reverse_string = ""
for i in user:
    reverse_string = i + reverse_string
print(reverse_string)
#
user = input("Enter your string")
reverse_string = ""
for i in user:
    reverse_string = user[::-1]
print(reverse_string)

# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
num = [1, 4, 5, 7, 8, 9, 33, 2, 6]
maxi = 0
print(type(maxi))
for i in num:
    if i > maxi:
        maxi = i
print("largest number is: ", maxi)























