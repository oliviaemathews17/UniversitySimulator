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

# Break
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