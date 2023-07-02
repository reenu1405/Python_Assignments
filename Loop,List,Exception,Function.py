# 1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.
# example :
# file 1:
# this is namaste sql course
# this is python course
# this assignment is part of day4 lecture
#
# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7
# C:\Users\MY DEVICE\Desktop

# Create the first file and write lines into it

# executing with two different files
with open("../../Desktop/open1.txt", 'w') as open1:
    lines = [
        "this is namaste sql course",
        "this is python course",
        "this assignment is part of day4 lecture"
    ]
    for line in lines:
        open1.write(line + '\n')

# Create the second file with word count at the end of each line
with open("../../Desktop/open1.txt", 'r') as open1, open("../../Desktop/open2.txt", 'w') as open2:
    for line in open1:
        line = line.strip()
        word_count = len(line.split())
        open2.write(line + ':' + str(word_count) + '\n')

print("File creation and word count operation completed!")

# Or
# with one single file
with open("../../Desktop/open1.txt", 'w') as f:
    print(f.write("this is namaste sql course\n"))
    print(f.write("this is python course\n"))
    print(f.write("this assignment is part of day4 lecture\n"))

f = open("../../Desktop/open1.txt", 'r')

content = f.readlines()
f.close()

f = open("../../Desktop/open1.txt", 'w')
for line in content:
    f.write(line.strip() + ":" + str(len(line.split()))+"\n")
f.close()
print(f)
# or
f = open("../../Desktop/open1.txt", 'w')
print(f.write("this is namaste sql course\n"))
print(f.write("this is python course\n"))
print(f.write("this assignment is part of day4 lecture\n"))
f.close()

# 2- given below dictionaries of states and their capital:
#
# capitals_dict = {
# 'Alabama': 'Montgomery',
# 'Alaska': 'Juneau',
# 'Arizona': 'Phoenix',
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver',
# 'Connecticut': 'Hartford',
# 'Delaware': 'Dover',
# 'Florida': 'Tallahassee',
# 'Georgia': 'Atlanta',
# }
#
# pick a state from above dictionary and ask user to enter the capital of the state.
# If the user answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However,
# if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".
#
# Note: Make sure the user isn’t punished for case sensitivity. In other words,
# a guess of "Denver" is the same as "denver".
# Do the same for exiting—"EXIT" and "Exit" should work the same as "exit".
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

state = input("Pick a state from the dictionary: ")
state = state.capitalize()  # Convert the input to capitalize for case insensitivity

while True:
    if state in capitals_dict:
        capital = capitals_dict[state]
        guess = input("Enter the capital of {}: ".format(state))
        guess = guess.capitalize()  # Convert the guess to capitalize for case insensitivity

        if guess == capital:
            print("Correct!")
            break
        elif guess.lower() == 'exit':
            print("The correct answer was: {}".format(capital))
            print("Goodbye!")
            break
        else:
            print("Incorrect. Try again or type 'exit' to quit.")
    else:
        print("Invalid state. Please pick a state from the dictionary.")

    state = input("Pick a state from the dictionary: ")
    state = state.capitalize()
# solution :
# Pick a state from the dictionary: >? Georgia
# Enter the capital of Georgia: >? Tallahassee
# Incorrect. Try again or type 'exit' to quit.
# Pick a state from the dictionary: >? Atlan
# Invalid state. Please pick a state from the dictionary.
# Pick a state from the dictionary: >? Florida
# Enter the capital of Florida: >? Tallahassee
# Correct!

# 3- write a program to take state as input from user and
# print the capital of the state using above dictonary.
# If the state is not there in dictonary then print "sorry , information not available"
capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

try:
    state = input("State Name").capitalize()
    print("Capital of ",state,"is: ", capitals_dict[state])

except Exception as e:
    print("sorry , information not available")
    print(e)

# solution :
# State Name>? Florida
# Capital of  Florida is:  Tallahassee

#
# 4- Let say You have one 100 cats.
# One day, you decide to arrange all your cats in a giant circle.
# Initially,none of your cats has a hat on.
# You walk around the circle a 100 times, always starting with the first cat (cat #1).
# Each time you stop at a cat, you check if it has a hat on.
# If it does not, then you put a hat on it. If it does, then you take the hat off.
#
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you stop only at every second cat (#2, #4, #6,
# #8, and so on).
# 3. The third round, you stop only at every third cat (#3, #6, #9, #12,
# and so on).
# 4. You continue this process until you’ve made one hundred rounds
# around the cats. On the last round, you stop only at cat #100.
#
#
# Write a program that simply outputs which cats have hats at the end.


# by default all are set to false since none have been visited
def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
        # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on
cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))

# solution : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]














