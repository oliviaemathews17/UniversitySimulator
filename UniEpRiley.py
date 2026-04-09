#Pseduocode 
# #################################
# STEP 1: thinking before programming (problem analysis)
#
# what is the program required to do?
# - simulate a student's weekly schedule (monday through friday)
# - allow the user to make choices for classes and activities
# - update gpa, happiness, and social stats based on choices
# - display final stats at the end of the week
#
# key goals:
# - correct input handling (only accept valid choices)
# - correct stat updates after each decision
# - correct order of days and events
# - clear output messages for user interaction
#
# key problems to be aware of:
# - repeated structure for each day (classes and choices)
# - need to validate user input multiple times
# - avoid missing stat updates
#
# plan to solve the problem:
# - create variables for gpa, happiness, and social
# - create a helper function enter() to pause the program
# - handle each day separately (monday through friday)
# - for each class/activity:
#     ask for input
#     validate input
#     update stats
# - display final results at the end

###################################
# STEP 2: procedural decomposition (break the program into pieces)
#
# main()
# - controls the entire simulation
# - calls each day function in order
#
# monday(), tuesday(), wednesday(), thursday(), friday()
# - handle all events and choices for each day
#
# enter()
# - pauses the program until user presses enter
#
# why this design avoids redundancy:
# - each day is grouped into its own function
# - repeated pause logic is handled by enter()
# - input validation structure reused logically

###################################
# a. problem decomposition:
#
# the program consists of 5 days
#
# each day includes:
# - multiple classes or activities
# - user choices (a/b or a/b/c)
# - stat updates based on choices
#
# pattern:
# input → validate → update stats → continue

###################################
# b. program pseudocode:


#def main():
    #initialize stats
    #get user name
    #monday()
    #tuesday()
    #wednesday()
    #thursday()
    #friday()
    #display final stats

#def enter():
    #wait for user input

#def monday():
    #handle comp 170
    #handle break
    #handle theology
    #handle math

#def tuesday():
    #handle comp 163
    #handle cjc
    #handle chinese culture

#def wednesday():
    #handle comp 170
    #handle theology
    #handle math

#def thursday():
    #handle comp 163
    #handle cjc
    #handle chinese culture

#def friday():
    #handle comp 170
    #handle theology
    #handle math


###################################
# program pseudocode & structure for a class block
#
# pseudocode:
#   display class name
#   input choice
#   while input invalid:
#       input again
#   if choice == "a":
#       increase stats
#   else:
#       decrease stats
#   call enter()

###################################
# program pseudocode & structure for break block
#
# pseudocode:
#   display options (a/b/c)
#   input choice
#   while invalid:
#       input again
#   if a:
#       increase gpa and happiness
#   elif b:
#       increase happiness
#   else:
#       increase social, decrease happiness
#   call enter()

###################################
# final output pseudocode
#
# display "end of week stats"
# display name
# display gpa
# display happiness
# display social

###################################
# main()


#MainCode 

print("Welcome to your GPA Simulator!")

name = input("What is your name? ")
print("Hello", name, "! Let's go through your week.\n")

def enter():
    input("Press Enter to continue...")

# Stats
gpa = 0
happiness = 0
social = 0

# ---------- MONDAY ----------
day = "monday"
print("----- Monday -----")
enter()

# COMP 170
print("COMP 170 at 9:20 AM - 10:15 AM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Please enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("Good thing you went today, you would have missed a lot")
    enter()
    print('''You walked into class today to see that your teacher is your family friend. 
          Her name is Mrs. Kelly. 
          But she was always kind of rude to you growing up. 

          You guys went over the syllabus today. 
          You will have a syllabus quiz when the class meets again this Wednesday.''')
    enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    social -= 1
    print("Hopefully that wasn't a bad idea...")
    enter()


print("You have an hour and 15 minutes till your next class. What do you want to do?")
print("a) Study for your next class")
print("b) Take a short nap")
print("c) Scroll social media")
answer = input("Enter your choice (a/b/c): ").lower()
while answer != "a" and answer != "b" and answer != "c":
    answer = input("Invalid input. Please enter a, b, or c: ").lower()

if answer == "a":
    gpa += 1
    happiness += 1
    print("You decided to study for your next class. I'm proud of you!")
    enter()
elif answer == "b":
    happiness += 2
    print("I hope the nap was worth it... Are you prepared for your next class?")
    enter()
elif answer == "c":
    social += 1
    happiness -= 1
    print("Scrolling can reduce focus and cognitive functions.")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Please enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You met Mr. Han today. He assigned a weekly assignment due Friday.")
    enter()
    ans = input("Do you (a) take notes or (b) zone out? ").lower()
    while ans != "a" and ans != "b":
        ans = input("Invalid input. Enter a or b: ").lower()
    if ans == "a":
        gpa += 2
        print("You took good notes and understood the assignment. Good job!")
        enter()
    elif ans == "b":
        gpa -= 2
        print("You zoned out and didn't understand the assignment.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped Theology class.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
ans = input("Do you (a) do practice problems or (b) give up? ").lower()
while ans != "a" and ans != "b":
    ans = input("Invalid input. Enter a or b: ").lower()
if ans == "a":
    gpa += 3
    print("Great! Your practice paid off.")
    enter()
elif ans == "b":
    gpa -= 3
    print("Skipping practice hurt your understanding of the material.")
    enter()

# ---------- TUESDAY ----------
day = "tuesday"
print("----- Tuesday -----")
enter()

# COMP 163
print("COMP 163 at 10:00 AM - 11:30 AM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You attended COMP 163 and got the lecture notes.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped COMP 163 and missed important lecture notes.")
    enter()

# CJC
print("CJC at 1:00 PM - 2:15 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You attended CJC class and participated in discussions.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped CJC class and missed out on participation.")
    enter()

# Chinese Culture
print("Chinese Culture at 2:30 PM - 3:45 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You learned about Chinese Culture today! Great job attending class.")
    enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    print("You skipped Chinese Culture. You missed out on learning about a new culture.")
    enter()

# ---------- WEDNESDAY ----------
day = "wednesday"
print("----- Wednesday -----")
enter()

# COMP 170
print("COMP 170 at 9:20 AM - 10:15 AM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You went to COMP 170 and reviewed the material. " \
    "This will help you prepare for the syllabus quiz on Friday.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped COMP 170. You missed out on important review for the syllabus quiz.")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You attended Theology class and worked on the assignment.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped Theology class. " \
    "You missed out on working on the assignment and understanding the material.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
ans = input("Do you (a) do practice problems or (b) give up? ").lower()
while ans != "a" and ans != "b":
    ans = input("Invalid input. Enter a or b: ").lower()
if ans == "a":
    gpa += 3
    print("Math practice helped your skills today. Keep it up!")
    enter()
elif ans == "b":
    gpa -= 3
    print("Skipping math practice hurt your understanding. Keep practicing!")
    enter()

# ---------- THURSDAY ----------
day = "thursday"
print("----- Thursday -----")
enter()

# COMP 163
print("COMP 163 at 10:00 AM - 11:30 AM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You attended COMP 163. " \
    "You reviewed the material and got the lecture notes. " \
    "This will help you prepare for the test on Friday.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped COMP 163. You missed out on reviewing " \
    "the material and getting the lecture notes.")
    enter()

# CJC
print("CJC at 1:00 PM - 2:15 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You attended CJC class. You took a pop quiz today and did well!")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped CJC class. You missed out on a pop quiz and lost points.")
    enter()

# Chinese Culture
print("Chinese Culture at 2:30 PM - 3:45 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You learned about Chinese Culture today! You also got points for attending class.")
    enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    print("You skipped Chinese Culture. You lost points for skipping class")
    enter()

# ---------- FRIDAY ----------
day = "friday"
print("----- Friday -----")
enter()

# Repeat Monday's classes (COMP 170, Theology, Math)
# COMP 170
print("COMP 170 at 9:20 AM - 10:15 AM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    print("You went to COMP 170. This will help you prepare for the syllabus quiz today.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped COMP 170. You missed out on important review for the syllabus quiz.")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
go = input("Do you (a) Want to go to class? or (b) Skip class?  ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()
if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You attended Theology class. " \
    "You reviewed the material and got the lecture notes. " \
    "This will help you prepare for the test on Monday.")
    enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skipped Theology class. You missed out on reviewing the material "
    "and getting the lecture notes.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
ans = input("Do you (a) take the pop quiz or (b) give up? ").lower()
while ans != "a" and ans != "b":
    ans = input("Invalid input. Enter a or b: ").lower()
if ans == "a":
    gpa += 3
    print("Great job on the pop quiz! Your practice paid off.")
    enter()
elif ans == "b":
    gpa -= 3
    print("You gave up on the pop quiz and lost points. Better luck next time.")
    enter()

# ---------- End of Week ----------
print("\nEnd of Week Stats for", name)
print("GPA:", gpa)
print("Happiness:", happiness)
print("Social:", social)
