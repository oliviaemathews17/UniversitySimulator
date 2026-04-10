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

def show_stats():
    print("--- Current Stats ---")
    print("GPA Points:", gpa)
    print("Happiness:", happiness)
    print("Social:", social)
    print("---------------------")
    enter()

# ---------- MONDAY ----------
print("----- Monday -----")
enter()

# COMP 170
print("COMP 170 at 9:20 AM - 10:15 AM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Please enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("You make it to COMP 170 just in time.")
    enter()
    print('''The professor - Dr. Kelly - turns out to be a family friend.
          She was always a bit cold to you growing up.
          She spots you and says, "Oh. I didn't know YOU were in my class."
          Awkward. But at least you showed up.
          She announces a syllabus quiz next Wednesday. Better take notes!''')
    enter()
    print("Midway through class, a classmate passes you a note asking to study together later.")
    choice = input("Do you (a) write back yes, (b) ignore it, or (c) whisper yes out loud? ").lower()
    while choice != "a" and choice != "b" and choice != "c":
        choice = input("Invalid input. Please enter a, b, or c: ").lower()
    if choice == "a":
        social += 2
        print("You write back yes and swap numbers after class. Great connection!")
        enter()
    elif choice == "b":
        print("You ignore it. The classmate shrugs and turns away.")
        enter()
    elif choice == "c":
        happiness -= 1
        print("Dr. Kelly glares at you. 'Is there something you'd like to share with the class?'")
        print("You sink into your seat. Maybe not the move.")
        enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    social -= 1
    print("You sleep in instead, which feels amazing...")
    enter()
    print("...until a classmate texts you: 'Dude, the prof announced a quiz for Wednesday!'")
    print("You didn't even know there WAS a quiz. This could be bad.")
    enter()

# Break
print("You have an hour and 15 minutes till your next class. What do you want to do?")
print("a) Head to the library and get ahead on readings")
print("b) Grab breakfast at the dining hall")
print("c) Take a quick nap in your dorm")
print("d) Scroll through your phone")
answer = input("Enter your choice (a/b/c/d): ").lower()
while answer != "a" and answer != "b" and answer != "c" and answer != "d":
    answer = input("Invalid input. Please enter a, b, c, or d: ").lower()

if answer == "a":
    gpa += 2
    print("You knock out some reading before Theology even starts. Productive!")
    enter()
elif answer == "b":
    happiness += 2
    print("Eggs and toast do wonders. Full stomach, clear head. Ready for Theology!")
    enter()
elif answer == "c":
    happiness += 1
    print("You set an alarm and wake up just in time. Groggy but alive.")
    enter()
elif answer == "d":
    social += 1
    happiness -= 1
    print("An hour of scrolling later, you feel more anxious than rested. Not your best call.")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Please enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("You walk in and meet Mr. Han. He seems easygoing but clearly loves the subject.")
    enter()
    print("He assigns a weekly reflection paper due every Friday.")
    enter()
    ans = input("During discussion, do you (a) participate, (b) take notes quietly, or (c) zone out? ").lower()
    while ans != "a" and ans != "b" and ans != "c":
        ans = input("Invalid input. Enter a, b, or c: ").lower()
    if ans == "a":
        gpa += 2
        social += 1
        print("You raise your hand and make a solid point. Mr. Han nods approvingly.")
        enter()
    elif ans == "b":
        gpa += 1
        print("You fill three pages of notes. Quiet but productive.")
        enter()
    elif ans == "c":
        gpa -= 2
        print("You drift off. Mr. Han calls on you and you have no idea what he asked.")
        print("'Uh... could you repeat the question?' The class snickers.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip Theology. Mr. Han takes attendance - that's a participation point gone.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
print("Dr. Torres is intense but fair. She dives straight into the material.")
enter()
ans = input("Do you (a) follow along and do practice problems or (b) give up and doodle? ").lower()
while ans != "a" and ans != "b":
    ans = input("Invalid input. Enter a or b: ").lower()
if ans == "a":
    gpa += 3
    print("You grind through the problems. Dr. Torres notices your effort.")
    enter()
    bonus = input("After class, do you (a) ask Dr. Torres a follow-up question or (b) just head out? ").lower()
    while bonus != "a" and bonus != "b":
        bonus = input("Invalid input. Enter a or b: ").lower()
    if bonus == "a":
        gpa += 1
        social += 1
        print("Dr. Torres gives you a tip that will help all semester. Nice work!")
        enter()
    elif bonus == "b":
        print("You head out. Nothing wrong with that.")
        enter()
elif ans == "b":
    gpa -= 3
    print("You produce a great doodle but learn absolutely nothing.")
    print("The homework tonight is going to be painful.")
    enter()

# Monday Evening
print("Classes are done for Monday! How do you spend your evening?")
print("a) Study and review today's notes")
print("b) Check out a club interest meeting you saw on a flyer")
print("c) Order pizza with your floor and watch a movie")
evening = input("Enter a, b, or c: ").lower()
while evening != "a" and evening != "b" and evening != "c":
    evening = input("Invalid input. Please enter a, b, or c: ").lower()

if evening == "a":
    gpa += 2
    happiness += 1
    print("Two productive hours later your notes are organized and you feel ready. Future you says thank you.")
    enter()
elif evening == "b":
    social += 3
    happiness += 2
    print("You join a photography club meeting and meet five cool people. You sign up on the spot!")
    enter()
elif evening == "c":
    happiness += 3
    social += 2
    print("Pizza and a movie with your floor. Best Monday ever. You feel completely at home.")
    enter()

show_stats()

# ---------- TUESDAY ----------
print("----- Tuesday -----")
enter()

# COMP 163
print("COMP 163 at 10:00 AM - 11:30 AM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("You show up and the professor dives into Python basics.")
    enter()
    print("Then she announces a surprise check-in quiz! Let's see how you do...")
    enter()

    quiz_score = 0
    q1 = input("Q1: What symbol starts a comment in Python? ")
    if q1 == "#":
        print("Correct!")
        quiz_score += 1
    else:
        print("Incorrect. The answer is: #")

    q2 = input("Q2: What keyword defines a function in Python? ").lower()
    if q2 == "def":
        print("Correct!")
        quiz_score += 1
    else:
        print("Incorrect. The answer is: def")

    q3 = input("Q3: True or False - print() displays text to the screen? ").lower()
    if q3 == "true":
        print("Correct!")
        quiz_score += 1
    else:
        print("Incorrect. The answer is True.")

    print("You scored " + str(quiz_score) + "/3 on the check-in quiz!")
    if quiz_score == 3:
        gpa += 3
        print("The professor gives you a nod. Impressive for week one!")
    elif quiz_score >= 1:
        gpa += 1
        print("Solid effort! There is room to grow.")
    else:
        gpa -= 1
        print("Time to review the basics tonight...")
    enter()

elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip COMP 163. Your lab partner texts: 'Where are you?? We had a quiz!'")
    print("A quiz. On the first Tuesday. That you missed.")
    enter()

# CJC
print("CJC at 1:00 PM - 2:15 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("CJC - Criminal Justice and Criminology. Surprisingly interesting from day one.")
    enter()
    print("The professor starts a debate: 'Is rehabilitation more important than punishment?'")
    enter()
    debate = input("Do you (a) argue for rehab, (b) argue for punishment, or (c) stay neutral? ").lower()
    while debate != "a" and debate != "b" and debate != "c":
        debate = input("Invalid input. Enter a, b, or c: ").lower()
    if debate == "a":
        gpa += 1
        social += 1
        print("You argue for rehabilitation backed by statistics. The professor says 'Strong argument!'")
        enter()
    elif debate == "b":
        gpa += 1
        social += 1
        print("You make a solid case for deterrence theory. The class is divided. Great discussion!")
        enter()
    elif debate == "c":
        print("You offer a balanced take. Some respect it, others think you are playing it safe.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip CJC. There was apparently a great debate today - everyone is talking about it.")
    enter()

# Chinese Culture
print("Chinese Culture at 2:30 PM - 3:45 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("Chinese Culture immediately becomes a favorite. Today: Chinese New Year traditions.")
    enter()
    print('''You learn about the Lantern Festival, red envelopes called hong bao,
          and traditional foods like dumplings and tang yuan.
          The professor is passionate and really engaging.''')
    enter()
    ans = input("The professor asks if anyone knows what 'hong bao' means. Do you (a) raise your hand or (b) stay quiet? ").lower()
    while ans != "a" and ans != "b":
        ans = input("Invalid input. Enter a or b: ").lower()
    if ans == "a":
        gpa += 2
        social += 1
        print("'Red envelope - money given as a gift during celebrations!'")
        print("The professor beams. 'Exactly right!' The class applauds.")
        enter()
    elif ans == "b":
        print("Someone else answers. You make a mental note to speak up more next class.")
        enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    print("You miss Chinese Culture. You hear later the class made traditional dumplings together.")
    print("You missed free food AND learning. Rough.")
    enter()

# Tuesday Evening
print("How do you spend Tuesday evening? You have a paper coming up in Chinese Culture.")
print("a) Take the train to Chinatown for firsthand research")
print("b) Hit the campus library and find academic sources")
print("c) Ask a classmate who knows about Chinese culture to chat over coffee")
research = input("Enter a, b, or c: ").lower()
while research != "a" and research != "b" and research != "c":
    research = input("Invalid input. Please enter a, b, or c: ").lower()

if research == "a":
    gpa += 3
    happiness += 2
    social += 1
    print("You hop on the train. The sights, smells, and sounds of Chinatown are incredible.")
    enter()
    print("You try soup dumplings at a tiny restaurant. Life-changing.")
    print("Your notes are vivid and your paper practically writes itself.")
    enter()
elif research == "b":
    gpa += 2
    print("You find solid academic sources and build a great bibliography. Thorough!")
    enter()
elif research == "c":
    gpa += 2
    social += 2
    happiness += 1
    print("Your classmate shares personal family stories about traditions and holidays.")
    print("You gain great insight - and make a real friend in the process.")
    enter()

show_stats()

# ---------- WEDNESDAY ----------
print("----- Wednesday -----")
enter()

# COMP 170 Syllabus Quiz
print("COMP 170 at 9:20 AM - 10:15 AM")
print("Today is the COMP 170 Syllabus Quiz Dr. Kelly announced on Monday!")
enter()
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("You show up for the quiz. Let's see how well you were paying attention on Monday!")
    enter()

    sqz = 0
    q1 = input("Q1: What is your COMP 170 professor's last name? ").lower()
    if q1 == "kelly":
        print("Correct!")
        sqz += 1
    else:
        print("Incorrect - the answer is Kelly.")

    q2 = input("Q2: On what day was the syllabus quiz announced? ").lower()
    if q2 == "monday":
        print("Correct!")
        sqz += 1
    else:
        print("Incorrect - it was announced on Monday.")

    q3 = input("Q3: What time does COMP 170 start? ")
    if q3 == "9:20" or q3 == "9:20 am":
        print("Correct!")
        sqz += 1
    else:
        print("Incorrect - class starts at 9:20 AM.")

    print("You scored " + str(sqz) + "/3 on the syllabus quiz!")
    if sqz == 3:
        gpa += 4
        print("Dr. Kelly raises an eyebrow and says 'Impressive.' High praise from her.")
    elif sqz >= 1:
        gpa += 1
        print("You passed - barely. Could have been much worse.")
    else:
        gpa -= 2
        print("Dr. Kelly sighs. You slide down in your seat.")
    enter()

elif go == "b":
    gpa -= 3
    social -= 1
    print("You skip quiz day. That is an automatic zero and Dr. Kelly marks you absent.")
    print("This is not looking good for your grade...")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("Mr. Han runs a group reflection activity today. You are placed in a group of three.")
    enter()
    group = input("Do you (a) take the lead, (b) share your ideas and collaborate, or (c) let others do the work? ").lower()
    while group != "a" and group != "b" and group != "c":
        group = input("Invalid input. Enter a, b, or c: ").lower()
    if group == "a":
        gpa += 2
        social += 1
        print("You keep the group on track. Mr. Han praises your leadership.")
        enter()
    elif group == "b":
        gpa += 1
        print("You share some thoughtful ideas. Good collaborative energy.")
        enter()
    elif group == "c":
        gpa -= 1
        happiness -= 1
        print("Your group notices you are not pulling your weight. Awkward.")
        print("That participation grade is going to sting.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip and miss the group activity. Your group had to cover for you.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
print("Today is a work day - Dr. Torres gives class time for the problem set.")
enter()
ans = input("Do you (a) work seriously, (b) work but keep checking your phone, or (c) give up entirely? ").lower()
while ans != "a" and ans != "b" and ans != "c":
    ans = input("Invalid input. Enter a, b, or c: ").lower()
if ans == "a":
    gpa += 3
    print("You knock out most of the problem set. Dr. Torres checks your work - solid progress!")
    enter()
elif ans == "b":
    gpa += 1
    print("You get through about half. You will need to finish tonight but it is manageable.")
    enter()
elif ans == "c":
    gpa -= 3
    print("You stare at the ceiling for 50 minutes. The entire set is waiting for you tonight.")
    enter()

# Wednesday Afternoon
print("No more classes today! How do you spend your Wednesday afternoon?")
print("a) Hit the campus rec center for a workout")
print("b) Meet your study group at the library")
print("c) Explore a part of campus you have not seen yet")
print("d) Go back to your dorm and take a nap")
afternoon = input("Enter a, b, c, or d: ").lower()
while afternoon != "a" and afternoon != "b" and afternoon != "c" and afternoon != "d":
    afternoon = input("Invalid input. Please enter a, b, c, or d: ").lower()

if afternoon == "a":
    happiness += 3
    print("You run into your floormates at the gym. Someone challenges you to a plank contest.")
    print("You lose badly. But it was fun and you feel great afterward.")
    enter()
elif afternoon == "b":
    gpa += 2
    social += 2
    print("Your study group helps you crack two problems you were stuck on. Teamwork!")
    enter()
elif afternoon == "c":
    happiness += 2
    social += 1
    print("You find a rooftop garden above the library. It is beautiful.")
    print("It becomes your new favorite spot on campus.")
    enter()
elif afternoon == "d":
    happiness += 1
    print("A mid-week nap hits different. You wake up groggy but eventually feel recharged.")
    enter()

show_stats()

# ---------- THURSDAY ----------
print("----- Thursday -----")
enter()

print("You check your phone - heavy rain all day. Lovely.")
enter()
weather = input("Do you (a) power through and walk, (b) take the campus shuttle, or (c) debate it and leave late? ").lower()
while weather != "a" and weather != "b" and weather != "c":
    weather = input("Invalid input. Enter a, b, or c: ").lower()
if weather == "a":
    happiness -= 1
    print("You arrive completely soaked. A stranger in the lobby hands you a paper towel.")
    print("Your pride is as damp as your shoes.")
    enter()
elif weather == "b":
    happiness += 1
    print("Smart call. The shuttle is packed but dry. You arrive on time and not miserable.")
    enter()
elif weather == "c":
    gpa -= 1
    print("Ten minutes of debate later you head out and arrive five minutes late to first class.")
    enter()

# COMP 163
print("COMP 163 at 10:00 AM - 11:30 AM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("The professor announces a group coding project starting next week!")
    enter()
    partner = input("A classmate asks if you want to be partners. Do you (a) say yes enthusiastically, (b) hesitate but say yes, or (c) say you will think about it? ").lower()
    while partner != "a" and partner != "b" and partner != "c":
        partner = input("Invalid input. Enter a, b, or c: ").lower()
    if partner == "a":
        social += 2
        gpa += 1
        print("Your new partner is a great coder. This could really help your grade. Excellent move!")
        enter()
    elif partner == "b":
        social += 1
        print("They seem a little unsure but agree. Could still be a solid partnership.")
        enter()
    elif partner == "c":
        print("They partner with someone else. You end up with whoever is left.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip and miss the project announcement. You will be scrambling to catch up.")
    enter()

# CJC
print("CJC at 1:00 PM - 2:15 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("Surprise pop quiz in CJC! Let's see if you have been keeping up with the readings.")
    enter()

    cjc_score = 0
    q1 = input("Q1: What does CJC stand for? (write it out) ").lower()
    if q1 == "criminal justice and criminology":
        print("Correct!")
        cjc_score += 1
    else:
        print("Incorrect - Criminal Justice and Criminology.")

    q2 = input("Q2: True or False - rehabilitation aims to reform offenders? ").lower()
    if q2 == "true":
        print("Correct!")
        cjc_score += 1
    else:
        print("Incorrect - the answer is True.")

    print("You scored " + str(cjc_score) + "/2 on the pop quiz!")
    if cjc_score == 2:
        gpa += 3
        print("You aced it! The professor gives you a nod.")
    elif cjc_score == 1:
        gpa += 1
        print("One point is better than none. You are hanging in there.")
    else:
        gpa -= 1
        print("You really need to keep up with the readings.")
    enter()

elif go == "b":
    gpa -= 3
    social -= 1
    print("You skip and miss a pop quiz. That zero is permanent. Ouch.")
    enter()

# Chinese Culture
print("Chinese Culture at 2:30 PM - 3:45 PM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    print("Today the class watches a short documentary on the Silk Road. Genuinely fascinating.")
    enter()
    notes = input("Do you (a) take detailed notes, (b) just watch, or (c) sketch the maps from the documentary? ").lower()
    while notes != "a" and notes != "b" and notes != "c":
        notes = input("Invalid input. Enter a, b, or c: ").lower()
    if notes == "a":
        gpa += 2
        print("Your notes are thorough. This material might show up on a future exam!")
        enter()
    elif notes == "b":
        print("You enjoy it but only remember the broad strokes afterward.")
        enter()
    elif notes == "c":
        happiness += 1
        social += 1
        print("Your hand-drawn map is so detailed the professor asks to use it as a class example.")
        print("You will take that win.")
        enter()
elif go == "b":
    gpa -= 2
    happiness -= 1
    print("You miss the Silk Road documentary. A classmate says it was the best class so far. Devastating.")
    enter()

# Thursday Evening
print("Almost Friday! How do you wind down Thursday night?")
print("a) Call home and catch up with family")
print("b) Play video games in the lounge with your floor")
print("c) Get ahead and write your Theology paper due tomorrow")
print("d) Go to a campus open mic night")
thursday_eve = input("Enter a, b, c, or d: ").lower()
while thursday_eve != "a" and thursday_eve != "b" and thursday_eve != "c" and thursday_eve != "d":
    thursday_eve = input("Invalid input. Please enter a, b, c, or d: ").lower()

if thursday_eve == "a":
    happiness += 3
    print("You talk to your mom for an hour. She says she is proud of you. You really needed that.")
    enter()
elif thursday_eve == "b":
    happiness += 2
    social += 2
    print("Mario Kart until midnight with your floor. You lose every race. You do not care at all.")
    enter()
elif thursday_eve == "c":
    gpa += 3
    print("You finish the Theology paper a whole day early. One less thing to stress about tomorrow!")
    enter()
elif thursday_eve == "d":
    happiness += 2
    social += 3
    print("A student performs original music that gives you chills.")
    print("You talk to them for twenty minutes afterward. A real connection made.")
    enter()

show_stats()

# ---------- FRIDAY ----------
print("----- Friday -----")
enter()

print("It's FRIDAY,", name, "! The finish line is right there.")
print("Today: COMP 170 lab day, Theology paper due, and Math pop quiz.")
enter()

# COMP 170
print("COMP 170 at 9:20 AM - 10:15 AM")
go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    print("Friday is lab day - you finally get hands-on with Python code.")
    enter()
    coding = input("Do you (a) write the code yourself, (b) copy from a neighbor, or (c) ask Dr. Kelly for help? ").lower()
    while coding != "a" and coding != "b" and coding != "c":
        coding = input("Invalid input. Enter a, b, or c: ").lower()
    if coding == "a":
        gpa += 3
        happiness += 1
        print("Your code runs on the first try. Dr. Kelly raises both eyebrows.")
        print("That is basically a standing ovation from her.")
        enter()
    elif coding == "b":
        gpa -= 1
        print("You copy your neighbor's code and it does not even run because they also have no idea.")
        print("Copying from the equally confused: a classic mistake.")
        enter()
    elif coding == "c":
        gpa += 1
        print("Dr. Kelly actually explains it really well. Who knew she had it in her?")
        print("You understand it now. Good instinct to ask.")
        enter()
elif go == "b":
    gpa -= 2
    social -= 1
    print("You skip the lab. You will have to figure it all out on your own.")
    print("Dr. Kelly noticed. She always notices.")
    enter()

# Theology
print("Theology 11:30 AM - 12:30 PM")
print("Weekly reflection paper is DUE TODAY.")
enter()

if thursday_eve == "c":
    print("Good news - you already wrote it last night. You walk in confident and relaxed.")
    paper_status = "done"
else:
    paper_status = input("Did you finish the reflection paper? (a) Yes it is done or (b) no I need to rush it? ").lower()
    while paper_status != "a" and paper_status != "b":
        paper_status = input("Invalid input. Enter a or b: ").lower()

go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
while go != "a" and go != "b":
    go = input("Invalid input. Enter a or b: ").lower()

if go == "a":
    gpa += 2
    happiness += 1
    social += 1
    if paper_status == "a" or paper_status == "done":
        gpa += 3
        print("You turn in your paper with confidence. Mr. Han seems genuinely pleased.")
    else:
        gpa -= 1
        print("You finish the last paragraph in the hallway and turn it in barely on time. It shows.")
    enter()
    print("Today's discussion: Does college change who you really are?")
    discuss = input("Do you (a) share your honest thoughts, (b) agree with whatever others say, or (c) just listen? ").lower()
    while discuss != "a" and discuss != "b" and discuss != "c":
        discuss = input("Invalid input. Enter a, b, or c: ").lower()
    if discuss == "a":
        social += 1
        happiness += 1
        gpa += 1
        print("You say something genuine and the room goes quiet in the best possible way.")
        enter()
    elif discuss == "b":
        print("You nod along. Safe but forgettable.")
        enter()
    elif discuss == "c":
        happiness += 1
        print("You absorb everyone's perspectives. Sometimes listening IS the lesson.")
        enter()
elif go == "b":
    gpa -= 3
    social -= 1
    print("You skip and miss turning in your paper. That is a zero AND an absence.")
    print("Mr. Han will definitely bring this up.")
    enter()

# Math
print("Math 1:40 PM - 2:30 PM")
ans = input("Do you (a) take the pop quiz or (b) walk out and skip it? ").lower()
while ans != "a" and ans != "b":
    ans = input("Invalid input. Enter a or b: ").lower()

if ans == "a":
    print("Here we go. Three questions. Let's do this.")
    enter()

    math_score = 0
    q1 = input("Q1: What is 15% of 200? ")
    if q1 == "30":
        print("Correct!")
        math_score += 1
    else:
        print("Incorrect - the answer is 30.")

    q2 = input("Q2: Solve for x:  2x + 6 = 14.  What is x? ")
    if q2 == "4":
        print("Correct!")
        math_score += 1
    else:
        print("Incorrect - x = 4.")

    q3 = input("Q3: What is the slope of the line y = 3x + 7? ")
    if q3 == "3":
        print("Correct!")
        math_score += 1
    else:
        print("Incorrect - the slope is 3.")

    print("You scored " + str(math_score) + "/3 on the pop quiz!")
    if math_score == 3:
        gpa += 5
        happiness += 2
        print("Perfect score! Dr. Torres says 'Solid work, keep it up.' You float out of class.")
    elif math_score >= 1:
        gpa += 2
        print("Decent! You held your ground. There is room to grow but you did not collapse.")
    else:
        gpa -= 3
        print("Rough quiz. Now you know exactly what to study for next time.")
    enter()

elif ans == "b":
    gpa -= 3
    print("You walk out. Dr. Torres watches you go with a disappointed look.")
    print("That is a zero you cannot make up.")
    enter()

# Friday Celebration
print("FRIDAY AFTERNOON - YOU SURVIVED THE WEEK!")
print("Congrats,", name, "! First week of college: done. How do you celebrate?")
print("a) Go out with new friends for dinner downtown")
print("b) Head to a campus comedy show tonight")
print("c) Go back to your dorm, journal, and get some rest")
print("d) Call a high school friend and compare first-week stories")
friday_end = input("Enter a, b, c, or d: ").lower()
while friday_end != "a" and friday_end != "b" and friday_end != "c" and friday_end != "d":
    friday_end = input("Invalid input. Please enter a, b, c, or d: ").lower()

if friday_end == "a":
    happiness += 3
    social += 3
    print("You and some new friends take the train downtown for deep dish pizza.")
    print("Laughing until your face hurts. This is exactly what college is supposed to feel like.")
    enter()
elif friday_end == "b":
    happiness += 3
    social += 2
    print("The comedian has the whole room in tears. Best two hours of your week easily.")
    enter()
elif friday_end == "c":
    happiness += 2
    gpa += 1
    print("You journal about the week, make a to-do list for Monday, and sleep early.")
    print("Future you will look back on this with respect.")
    enter()
elif friday_end == "d":
    happiness += 2
    social += 1
    print("Your high school friend is having an equally chaotic first week.")
    print("You laugh about it for an hour. Feels good to know you are not alone.")
    enter()

# ---------- End of Week ----------
print("\nEnd of Week Stats for", name)
print("GPA:", gpa)
print("Happiness:", happiness)
print("Social:", social)
print()

if gpa >= 40:
    print("Academic result: Outstanding! You are on track for a fantastic semester.")
elif gpa >= 25:
    print("Academic result: Solid week. You are building good habits.")
elif gpa >= 10:
    print("Academic result: You are getting by, but there is room to improve.")
elif gpa >= 0:
    print("Academic result: Rough week. Time to refocus next Monday.")
else:
    print("Academic result: Skipping class has a real cost. Turn it around next week!")

if happiness >= 15:
    print("Happiness result: You are genuinely thriving. College suits you!")
elif happiness >= 8:
    print("Happiness result: Decent week. Some highlights, some lows.")
elif happiness >= 0:
    print("Happiness result: You are surviving. Make time for things that recharge you.")
else:
    print("Happiness result: This week took a toll. Be kind to yourself next week.")

if social >= 12:
    print("Social result: You have built real connections already. Great start!")
elif social >= 5:
    print("Social result: You made some solid connections. Keep putting yourself out there.")
elif social >= 0:
    print("Social result: A bit of a lone wolf this week. Try saying yes to more things.")
else:
    print("Social result: Isolation adds up. Reach out to someone next week.")