# SDM: This program will conduct a series of statistics on an inputted string of grades.
#      The statistics will be saves to a text file.  The stats will include: quantity,
#      sum total, max, min, mean avg, evens, and odds.
#      for example, the file contents should look like (for a list of [12 20]):
#      --------------
#      quantity: 2
#      sum: 32
#      max: 20
#      min: 12
#      avg: 16.0
#      even: 12, 20
#      odd: 
#      --------------

# Steps to Solve:
# 1. Get the numbers from the user.
# 2. Calculate the statistics.
# 2a) quantity - Count up how many numbers there are.
# 2b) sum - Add up all the numbers. 
# 2c) max - Find the largest number.
# 2d) min - Find the smallest number.
# 2e) avg - Sum up the numbers and divide by the quantity of numbers.
# 2f) even - Look at the list of numbers, check each number to see if its even, and if so, add it to a new list of even numbers.
# 2g) odd - Basically the same as evens.
# 3. Save the statistics to a text file.
# 3a) If a stats.txt does not exist already, we will create it.
# 3b) Either way, we will save the string into the file.

# get the numbers from the user (function)
def get_grades():
    """No inputs.  Function assigns user-generated input into variable, splits it into a list, and checks whether it is a valid list for the remainder of program.  If it is, returns that list but if not, quits program entirely."""
    print("Please input the grades from an exam down below.\n")
    grades = input("Enter here (SEPARATE NUMBERS BY SPACES): ") # get a string of numbers
    grades = grades.split() # convert the string into a list of number strings
    try:
        grades = [int(g) for g in grades] # convert the list of number strings into a list of integers
        return grades
    except ValueError or TypeError:
        print("You did not follow the directions unfortunately which led to the program bugging out.")
        print("Now quitting the program...") 
        exit()

def quantity_grades(list):
    """User-generated list is the input.  Function assigns number of items in list into variable.  It returns the integer as a variable."""
    quantity = len(list)
    return quantity

def sum_grades(list):
    """User-generated list is the input.  Function assigns total sum for items in list into variable.  It returns the integer as a variable."""
    total = sum(list)
    return total

def max_grades(list):
    """User-generated list in the input.  Function assigns maximum value of items in list into variable.  It returns the integer as a variable."""
    highest = max(list)
    return highest

def min_grades(list):
    """User-generated list is the input.  Function assigns minimum value of items in list into variable.  It returns the integer as a variable."""
    lowest = min(list)
    return lowest

def average_grades(total, count):
    """Calculated grade total and grade amount are the inputs.  Function assigns the average grade in the list into variable.  It returns the float as a variable."""
    mean = float((total) / (count))
    return mean

def even_grades(list):
    """User-generated list is the input.  Function assigns the even grades in the list into list from looping to check each grade if even.  It returns the integers as a list."""
    evens = []
    for g in list:
        if g % 2 == 0:
            evens.append(g)
    return evens

def odd_grades(list):
    """User-generated list is the input.  Function assigns the odd grades in the list into list from looping to check each grade if odd.  It returns the integers as a list."""
    odds = []
    for g in list:
        if g % 2 != 0:
            odds.append(g)
    return odds

# Creating variables from the function outputs
grade_list = get_grades()
grade_count = quantity_grades(grade_list)
grade_total = sum_grades(grade_list)
highest_grade = max_grades(grade_list)
lowest_grade = min_grades(grade_list)
mean_grade = average_grades(grade_total, grade_count)
even_nums = even_grades(grade_list)
odd_nums = odd_grades(grade_list)

# I create the strings that contain the labels and their associated statistics
count_string = "Quantity: " + str(grade_count)
total_string = "Sum: " + str(grade_total)
highest_string = "Max: " + str(highest_grade)
lowest_string = "Min: " + str(lowest_grade)
mean_string = "Avg: " + str(mean_grade)
even_string = "Even: " + str(even_nums)
odd_string = "Odd: " + str(odd_nums)

# Next I combine the string into a list
stats = [count_string, total_string, highest_string, lowest_string, mean_string, even_string, odd_string]

try:
    with open("Statistics.txt", "w") as file:
        for item in stats:
            file.write(item + "\n")
except IOError: # input/output error
    print("There was a problem saving your list.")