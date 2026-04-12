

#----Global variables, titles, etc.  
#TITLE SCREEN---------------------------------------------------------------------------------------------------
#This function displays a decorative title screen for the University Simulator.
#It welcomes the player, explains the goals of the game, and sets expectations
#for the week. It introduces the idea that player choices will affect GPA,
#social life, and happiness. This function does not take any input or return values.

def title():
    print('''
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                  ꒰ঌ࿔────⊹˖₊˚⊹⋆────⋆˚˖⟡˖˚⋆────⋆⊹˚₊˖⊹────࿔໒꒱
          //ᐢ⑅ᐢ\\   ♡   ₊˚  
        ꒰ ˶• ༝ •˶꒱       ♡‧₊˚    ♡      WELCOME TO UNIVERSITY SIMULATOR!     ♡‧₊˚    ♡
        ./づ~ :¨·.·¨:     ₊˚               ~ loyola university chicago ~
                                                    ────୨ৎ────
                                        Welcome to your first month, rambler! 
          
                                      This week will be full of new experiences,   
                                      challenges, and opportunities for growth.     𖹭 ₊˚⊹
                    
                                As you navigate through your classes, social life, and 
                               personal well-being, remember that every choice you make 
                                         will shape your university experience. 
          
             Will you prioritize your studies, or will you focus on making friends and enjoying campus life? 
                    
                         The decisions are yours to make, and the consequences will follow. 
          
          

                   𖹭 ₊˚⊹   Good luck, and have fun exploring the world of university life!   𖹭 ₊˚⊹

                                   



                       ๋ㅤ ࣭ ㅤ⭑  ☆ㅤ ๋࣭ㅤ ⭑    by olivia, alona, and riley   ๋ㅤ ࣭ ㅤ⭑  ☆ㅤ ๋࣭ㅤ ⭑
                                    ꒰ঌ࿔────⊹˖₊˚⊹⋆────⋆˚˖⟡˖˚⋆────⋆⊹˚₊˖⊹────࿔໒꒱
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          
       '''   )


#This is the code for the university episode app. OLIVIA MATHEWS

#----preliminary notes:
#Each class is a function
#Each scenario is a function
#Each day is a function which contains the functions for the events of that day
#The main function will be the entire week, which will call the day functions in order

#If the user chooses something that is not an option, the program will print "Invalid choice, please try again" and ask the user to choose again
# Figure out how to make the user choose again without having to restart the program

#I have to make variables that will be affected by the user's choices, such as grades, social life, mental health, etc. 
# These variables will be used to determine the outcome of the week and the final result.
#-----------

'''
-------------------------------------------------------
REPEATING FUNCTIONS:



enterContinue()
This function pauses the narrative until the player presses Enter.
It allows the player to read messages at their own pace and creates
a natural break between scenes or choices. It does not take input
parameters and does not return a value.


dailyScheduleOlivia(day)       
This function prints Olivia's class schedule depending on the day.
If the day is Monday, Wednesday, or Friday, it prints MWF classes:
Computer Science, Philosophy, Math, and Sociology.
If the day is Tuesday or Thursday, it prints TTh classes:
Philosophy and Chinese Literature & Film.
This function is purely informational and does not affect game variables.


cuteTitle()
This function prints a cute decorative title for each day.
It adds aesthetic styling before showing the schedule.
It does not take input parameters and does not return values.


startDayTitleOlivia(day)
This function begins the day for Olivia's week.
It prints the day of the week, calls the cuteTitle function
to display a decorative header, then shows the daily schedule
by calling dailyScheduleOlivia(day). It also pauses with enterContinue
so the player can absorb the information before making decisions.


whatsYourName()
This function prompts the player to enter their name at the start of the game.
It welcomes the player by name and sets the stage for the university experience.


journalEntry(day)
This function simulates a daily journal entry assignment for the philosophy class.
The player is prompted to write about their experiences and feelings for the day.
The entry is saved to a text file called "journal.txt" with the day as a header
and the player's input as the content.
The function does not return any value but allows the player to reflect on their 
day and document their thoughts.


finalStats()
This function displays the final values of GPA, social, and happiness.
It summarizes the cumulative effect of all decisions made throughout the day.

statNums()
This function ensures that the GPA, social, and happiness variables stay within a reasonable range (0-100). 
It checks each variable and adjusts it if it goes above 100 or below 0. 
This prevents unrealistic values and maintains the integrity of the simulation's scoring system.

--------------------------------------------------------------------------------------------------------

MONDAY:
-compSciMonday():
This function represents the first class of the day, Computer Science.
It displays an introduction to the class and then calls introduceYourself to
allow the player to make a social decision. This function does not directly
change any variables but relies on the called function to update stats.

-passingPeriodCompToPhil():
This function represents the transition between Computer Science and Philosophy.
It only displays narrative text and does not affect any variables.

-philMonday():
This function simulates Philosophy class. First, the player is introduced to
the class and given a social interaction opportunity through introduceYourself.
Then, the player faces an academic decision about whether they completed a reading.
Input validation is used to ensure a valid response.
If the player pretends they did the reading, happiness decreases slightly.
If they admit they did not complete the reading, happiness, social, and GPA
all decrease more significantly. This function demonstrates multiple variable
impacts from a single decision.

-philToMath():
This function represents the transition from Philosophy to Math. It only
displays narrative text and does not modify any variables.

-mathMonday():
This function simulates Math class. The player first makes a social decision
through introduceYourself. Then, they choose how to behave in class: pay attention,
scroll on their phone, or take a nap. A loop ensures valid input.
Paying attention increases GPA and happiness. Scrolling slightly increases happiness
but does not affect GPA. Napping significantly decreases GPA, happiness, and social
due to missed material and embarrassment.

-soclMonday():
This function represents Sociology class. The player is introduced to the class
and calls introduceYourself for a social interaction. There are no academic decisions
in this function, so only social and happiness may change through that interaction.

studyMonday():
This function represents studying during free time. The player chooses between
philosophy reading or math homework. Input validation ensures a correct response.
Choosing philosophy increases GPA. Choosing math increases GPA and also increases
happiness after completing the work.


gFitMonday():
This function simulates attending a group fitness class. It does not require input.
The player gains happiness from exercising and gains social points from meeting
and interacting with others.


dinnerMonday():
This function simulates going out to dinner with a friend. It is a narrative function
that increases happiness and represents a positive social experience at the end of the day.


dayOverMonday():
This function marks the end of classes and the beginning of free time.
It summarizes the day and then calls studyMonday, gFitMonday, and dinnerMonday
in sequence to simulate the players evening activities.

finalStats():
This function displays the final values of GPA, social, and happiness.
It summarizes the cumulative effect of all decisions made throughout the day.

mondayOlivia():
This is the main function that controls the full program flow.
It runs each part of the day in order: starting the day, all classes,
transition periods, free-time activities, journal entry, and final stats.
It ensures the program executes in a logical sequence from morning to night.
---------------------------------------------------------------------------------------------
TUESDAY 

syllabusQuiz():
This function simulates a short graded quiz based on the philosophy syllabus.
The player is asked a series of factual questions about the course. Each correct answer
increases the quiz score by 25 points. At the end, the total score is calculated and
a message is displayed based on performance. Higher scores result in positive feedback,
while lower scores encourage reviewing the syllabus more carefully.

philTuesday():
This function simulates the philosophy class. The player is introduced to the class
and its structure, including exams and weekly readings. The player then makes a social
decision using the introduceYourself function. Later, the syllabus quiz is triggered,
which tests the players knowledge of course expectations. This function combines social
interaction and academic evaluation in one class period.

chineseTuesday():
This function simulates a Chinese literature and film class. The player is introduced
to the course content and then given a social interaction opportunity through
introduceYourself. The function is primarily narrative but introduces a major assignment:
a research paper on Chinese culture in Chicago. This assignment becomes the foundation
for later after-school exploration choices.

chineseRestaurant():
This function represents one possible after-school research path. The player visits
multiple Chinese restaurants from different regions and experiences diverse cuisines.
Throughout the experience, the player learns cultural and historical context, including
interaction with a restaurant owner who provides insight into cultural diversity.
At the end of the function, happiness and social both increase due to positive interaction
and meaningful cultural engagement. The researchTopic variable is set to "food".

herbalMedicine():
This function represents another research option where the player visits a traditional
Chinese herbal medicine shop. The player learns about herbal remedies, cultural beliefs
such as yin and yang, and the philosophy behind traditional Chinese medicine. A conversation
with the shop owner deepens cultural understanding. Happiness and social both increase,
and researchTopic is set to "medicine".

musicalPerformance():
This function represents a cultural research option involving a musical performance.
The player learns about traditional Chinese instruments such as the erhu, pipa, and guzheng.
After the performance, the player speaks with performers and gains deeper understanding
of each instruments cultural significance. Happiness and social increase, and researchTopic
is set to "music".

clothingShops():
This function represents a cultural exploration of traditional Chinese clothing.
The player visits shops and learns about garments such as qipao, hanfu, and tangzhuang.
Shop owners explain the cultural and historical significance of each style. This experience
increases both happiness and social, and researchTopic is set to "clothes".

chinaTown():
This function allows the player to choose how to spend their time in Chinatown.
The player selects one of four options: restaurants, herbal medicine, musical performance,
or clothing shops. Input validation ensures a valid choice. Based on the selection,
the corresponding function is called. This function acts as a menu controller for
after-school studying in chinatown.

dormResearch():
This function represents staying in the dorm to complete research online instead of
going out. The player chooses a research focus area related to Chinese culture in Chicago.
Each option provides informational content and sets the researchTopic variable accordingly.
The function is entirely academic and focuses on gathering information for the final paper.

afterSchoolTuesday():
This function represents the decision after classes end. The player chooses whether
to travel to Chinatown or stay in the dorm. Based on the choice, either chinaTown()
or dormResearch() is called. This function determines the structure of the after-school
research experience.

tuesdayOlivia():
This is the main control function for Tuesday. It runs all parts of the day in sequence:
starting the day, philosophy class, Chinese literature class, after-school research,
journal entry, and final stats. It ensures that all functions execute in order and
that the players choices carry through the entire simulation.
-------------------------------------------------------------------------------------

WEDNESDAY 

compWednesday():
This function simulates a computer science class offered both online and in-person.
The player chooses whether to attend class online or in person. Each choice leads to
different narrative events and consequences.
If the player attends online, they experience a disruptive roommate interaction that
results in a negative outcome with decreased happiness, social, and GPA. If the player
attends in person, they experience an accident where a chair breaks during class,
leading to embarrassment and a smaller decrease in happiness. This function demonstrates
how early-day decisions can lead to unexpected consequences.


philWednesday():
This function simulates philosophy class on Wednesday. The player is given the option
to skip class or attend. Input validation ensures correct choices.
If the player skips class, they can choose between studying at the library, going to the gym,
or relaxing at a café. Each option results in different benefits such as increased GPA or
happiness. If the player attends class, they experience a positive social interaction involving
cupcakes provided by the teacher, which increases both social and happiness. This function
demonstrates branching life decisions with different reward paths.

mathGame():
This function simulates a short math quiz game used inside math class. The player is given
a series of math questions and earns points for each correct answer. The function tracks a
local score variable and provides feedback based on performance.
A perfect score results in highly positive feedback, while lower scores result in increasingly
critical messages. This function demonstrates iteration through multiple questions and scoring
based on correctness.

mathWednesday():
This function simulates math class where the player can choose to participate in a review game.
The player decides whether or not to participate in "Math Jeopardy."

If the player participates, the mathGame function is called and they gain social and happiness
due to engagement and peer interaction. If they do not participate, they lose social and happiness
due to missing out on interaction and review. This function emphasizes participation-based outcomes.

soclSyllabusQuiz():
This function simulates a sociology syllabus quiz. The player answers questions about course
details such as the teacher name, number of quizzes, exams, and papers. Each correct answer
increases a quiz score.
At the end, the score is evaluated and used to adjust GPA. Higher scores result in GPA increases,
while low scores result in a GPA decrease. This function demonstrates knowledge-based scoring and
conditional outcomes.

soclWednesday():
This function simulates sociology class on Wednesday. The player is introduced to a syllabus quiz
and then completes soclSyllabusQuiz. After the quiz, the teacher reviews course expectations.
This function is primarily academic and does not involve major branching decisions, but it may
affect GPA through quiz performance.

daylunchWednesday():
This function simulates the player choosing a lunch option after classes. The player selects
between the dining hall, a café, or fast food.
Each option provides different narrative outcomes related to food quality, cost, and healthiness.
This function demonstrates simple branching choices with no variable changes, focusing on narrative
experience and lifestyle decisions.

baking():
This function simulates a dorm-based baking activity. The player chooses between baking cookies,
banana bread, or brownies.
Each option results in a positive social and happiness outcome due to sharing food with others.
This function demonstrates creativity-based decision making and rewards social interaction and
kindness through shared experiences.

dayOverWednesday():
This function represents the end-of-day decision after lunch. The player chooses whether to bake
something or study in their dorm.
If the player chooses baking, the baking function is called and leads to social and happiness gains.
If the player chooses to study, GPA increases due to productivity. This function demonstrates
trade-offs between academic productivity and social enjoyment.

wednesdayOlivia():
This is the main control function for Wednesday. It runs all events in order: starting the day,
computer science, philosophy, math, sociology, lunch, free-time decision, journal entry, and final
stats. It ensures that all decisions made throughout the day affect the final outcome of the simulation.
---------------------------------------------------------------------------------

THURSDAY

thursdayMorning():
This function simulates the player’s early morning routine before class. The player chooses
between going for a run, scrolling on their phone, or going back to sleep. Each option results
in a different emotional outcome. Running increases happiness due to exercise and fresh air.
Scrolling decreases happiness due to social comparison and passive behavior. Sleeping in increases
happiness slightly due to rest but may have minor narrative consequences. Input validation ensures
a valid choice is entered.

philGame():
This function simulates a philosophy-themed guessing game. The player is given partially completed
words related to philosophers such as Aristotle, Plato, and Socrates. The player attempts to guess
each word correctly. A local variable tracks philosophyPoints, which increases for each correct answer.
At the end, performance feedback is given based on total points, with higher scores receiving more
positive messages. This function demonstrates iteration through multiple rounds and scoring logic.

philThursday():
This function simulates philosophy class on Thursday. The player is introduced to a class activity
in which they can choose to participate in a word-based review game. If the player participates,
the philGame function is called, and they gain social and happiness due to interaction and engagement.
If they do not participate, they lose social and happiness and also experience a GPA decrease.
This function emphasizes the consequences of participation versus isolation in a classroom setting.

chinaTownQuestions():
This function simulates a presentation question-and-answer session based on the players Chinatown
research experience. The questions asked depend on the value of researchTopic, which determines
what type of cultural content the player explored (food, medicine, music, or clothing).
For each topic, the player is asked multiple factual questions. Correct answers increase GPA and
presentationPoints, while incorrect answers decrease GPA. At the end, the function builds the
players presentation score based on accumulated correct responses. This function demonstrates
conditional logic based on prior choices and cumulative scoring.

dormQuestions():
This function is similar to chinaTownQuestions, but it is used when the player stays in their dorm
instead of visiting Chinatown. The questions still depend on researchTopic, but they are based on
online research rather than firsthand experiences. The player answers multiple questions, gaining or
losing GPA depending on correctness. This function also contributes to presentationPoints.

presentationScore():
This function evaluates the final presentation score stored in presentationPoints. If the player
scores 100, they receive a perfect performance message. Lower scores result in progressively more
critical feedback. This function summarizes the outcome of the presentation assessment.

chineseQuestions():
This function determines which set of presentation questions the player will receive. If the player
visited Chinatown (chinaTownTravel is true), chinaTownQuestions is called. Otherwise, dormQuestions
is used. This function acts as a conditional controller based on earlier decisions.

chineseThursday():
This function simulates the Chinese culture presentation. The player presents their research topic
and then answers questions from classmates. The questions are selected based on prior choices made
during the week. After answering questions, presentationScore is called to evaluate performance.
This function demonstrates cumulative gameplay where earlier decisions directly affect final outcomes.

thursdayOlivia():
This is the main control function for Thursday. It runs all parts of the day in sequence: morning
routine, philosophy class game, Chinese presentation, journal entry, and final stats display. It
ensures that all previous decisions and variables are carried through to the end of the simulation.
-------------------------------------------------------
FRIDAY



compQuiz():
This function simulates a computer science quiz focused on basic Python knowledge.
The player answers questions about comments, boolean values, and function definitions.
Each correct answer increases the global compPoints score, while incorrect answers decrease it.
At the end of the quiz, the total score out of 60 is calculated and feedback is given based on performance.
This function demonstrates simple input validation, scoring, and conditional feedback based on correctness.


compFriday():
This function simulates the final computer science class of the week.
The player is introduced to a pop quiz and then completes compQuiz.
After the quiz, the class concludes and the player reflects on their experience.
The function adjusts global stats such as happiness, social, and GPA depending on quiz performance.
This function represents the end of a recurring academic subject with a final assessment.


ethicsDebateShow():
This function simulates a philosophy class activity in the form of an ethics debate game show.
The player responds to moral dilemmas through multiple-choice options such as arguing seriously,
making humorous comments, or staying quiet.
Each choice affects social, happiness, and GPA differently.
This function demonstrates scenario-based decision making and the consequences of different moral approaches.


philFriday():
This function simulates the final philosophy class of the week.
It begins by calling ethicsDebateShow, where the player participates in ethical scenario discussions.
After the activity, the class ends with a reflective conclusion about the experience.
This function emphasizes engagement, classroom participation, and social interaction within an academic setting.


mathTestFriday():
This function simulates a final math test consisting of four questions covering arithmetic,
geometry, square roots, and the value of pi.
Each correct answer increases the playerS score, with a maximum possible score of 100.
At the end, the total score is evaluated and GPA is adjusted based on performance.
This function demonstrates structured assessment, scoring accumulation, and conditional evaluation.


mathFriday():
This function simulates the final math class of the week.
The player is informed that a test will take place and then completes mathTestFriday.
After the test, the class ends and the player transitions out of the math storyline.
This function represents a formal academic assessment concluding a course segment.


soclGame():
This function simulates a sociology review game where the player matches sociologists
to their countries of origin.
The game consists of three rounds, each awarding points for correct answers.
At the end, the total score is evaluated and used to adjust GPA.
This function demonstrates knowledge recall, repetition, and performance-based scoring.


soclFriday():
This function simulates the final sociology class of the week.
Instead of a traditional lecture, the class is replaced with a matching game using soclGame.
The player participates in the activity and completes the final sociology lesson.
This function emphasizes gamified learning and ends the sociology course segment.


fridayOlivia():
This is the main control function for Friday.
It runs all events in order: starting the day, computer science class, philosophy class,
math class, and sociology class.
After all classes are completed, the function calls journalEntry and finalStats.
This function ensures that all academic and social decisions across the day contribute
to the final outcome of the simulation.
-------------------------------------------------------------------------
FINAL FUNCTIONS

completeStats():
This function displays the final results of the players week by evaluating three main stats:
GPA, happiness, and social level. It prints a formatted summary for each category and
then uses conditional statements to determine performance ranges.

For GPA, the function evaluates academic success and assigns a final letter grade from A+ to F.
Higher GPA values reflect strong academic performance, while lower values indicate academic struggle.

For happiness, the function evaluates the players emotional well-being throughout the week.
Higher values indicate a positive and successful experience, while lower values reflect stress or
unfavorable events.

For social, the function evaluates the players level of social interaction and engagement.
Higher values indicate strong social participation, while lower values indicate isolation or limited
interaction.

This function serves as the conclusion of the simulation, summarizing the impact of all decisions
made throughout the week.


oliviasWeek():
This is the main control function for the entire game simulation.
It runs the full storyline in order, beginning with setup functions such as title() and whatsYourName(),
followed by each day of the week from Monday through Friday.
Each day function is called here (mondayOlivia, tuesdayOlivia, wednesdayOlivia, thursdayOlivia, fridayOlivia)
After all days are completed, the function calls completeStats() to display final results and
evaluate overall performance.
This function acts as the central game loop and ensures that all events, choices, and outcomes
are connected into one continuous narrative experience.


oliviasWeek():
This function is executed at the end of the program and starts the entire simulation.
It controls the full flow of the game from beginning to end, ensuring that all functions
run in the correct order and that the player experiences a complete week in the game world.

------------------------------------------------------------------



'''












#code starts here! :)



# key variables
gpa = 100
social = 0
happiness = 100


#---enterContinue------------------------
#This function pauses the narrative until the player presses Enter.
#It allows the player to read messages at their own pace and creates
#a natural break between scenes or choices. It does not take input
#parameters and does not return a value.

def enterContinue():
    print()
    input('Press Enter to continue...')
    print()


#--------schedule for class-----------------------------------------------------------------        
#This function prints Olivia's class schedule depending on the day.
#If the day is Monday, Wednesday, or Friday, it prints MWF classes:
#Computer Science, Philosophy, Math, and Sociology.
#If the day is Tuesday or Thursday, it prints TTh classes:
#Philosophy and Chinese Literature & Film.
#This function is purely informational and does not affect game variables.       
def dailyScheduleOlivia(day): 
    if(day == 'Monday' or day == 'Wednesday' or day == 'Friday'):
        print( '''  9:20-10:10: Computer Science 
              
                    10:30-11:20: Philosophy
              
                    11:30-12:20: Math
              
                    12:30-1:20: Sociology ''')
    else:
        print('''   1:00 - 2:15: Philosophy
                      
                    2:30 - 3:45: Chinese liturature & film ''')
#---------------------------------------------------------------------




#--------------------day decor------------------------------
#This function prints a cute decorative title for each day.
#It adds aesthetic styling before showing the schedule.
#It does not take input parameters and does not return values.
def cuteTitle():
     print('''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                      ꒰ঌ࿔────⊹˖₊˚⊹⋆────⋆˚˖⟡˖˚⋆────⋆⊹˚₊˖⊹────࿔໒꒱
              //ᐢ⑅ᐢ\\   ♡   ₊˚  
            ꒰ ˶• ༝ •˶꒱       ♡‧₊˚                   ♡  Schedule:    ♡‧₊˚    ♡
            ./づ~ :¨·.·¨:     ₊˚                         
  
            ''')
#---------------------------------------------------------------



#---------------day start title--------------------------
#This function begins the day for Olivia's week.
#It prints the day of the week, calls the cuteTitle function
#to display a decorative header, then shows the daily schedule
#by calling dailyScheduleOlivia(day). It also pauses with enterContinue
#so the player can absorb the information before making decisions.
def startDayTitleOlivia(day):
    print("\n                                                          " + day)
    cuteTitle()
    dailyScheduleOlivia(day)
    enterContinue()
#--------------------------------------------------------



#---------whats your name?----------------------
#This function prompts the player to enter their name at the start of the game.
#It welcomes the player by name and sets the stage for the university experience.
def whatsYourName():
    fullName = input("Welcome to University Simulator! What is your full name (First Last)? ")
    nameList = fullName.split()
    firstName = nameList[0]
    lastName = nameList[1]

    print("Welcome, " + firstName + "! We're so excited to have you here at Loyola University Chicago. Let's get started with your first week of classes!")
    enterContinue()
#----------------------------------------------------------------

#Journal function----------------
def journalEntry(day):
    print('''Philosophy Assignment: Daily Journal - ''' + str(day) + ''')
          
            Take a moment to reflect on your day, and write down your thoughts and feelings about your experiences.         
          
         ''')
    
    with open('journal.txt', 'w') as journal:
        entry = input("Write your journal entry here (x to submt): ").lower()
        while entry != 'x':
            journal.write(day + ": " + entry + "\n")
            entry = input("Continue writing...(x to submit): ").lower()


    print("You have finished your journal entry. Good work today!")





#MONDAY---------MONDAY---------MONDAY---------MONDAY---------MONDAY---------MONDAY---------MONDAY---------MONDAY---------
#------------------------------------------------------------------------------------------------------------------------
#------computer science------------------------------------------------------
#This function simulates the Computer Science class on Monday.
#The player chooses whether to introduce themselves to the classmate
#or stay isolated. Introducing increases the social variable,
#while isolation decreases social and happiness. Invalid input
#recursively calls the same function to ensure valid input using a while loop.
#This function directly updates the social and happiness global variables.


def introduceYourself():
    
    global social
    global happiness
    print('''
        You take your seat, and think you should meet some of your classmates. Do you:
        1. Introduce yourself to the person sitting next to you
        2. Keep to yourself and hope someone talks to you''')
    
    while True:
        talkChoice = input('Enter 1 or 2: ')
        if talkChoice == '1':
            print('You introduce yourself to the person sitting next to you, and they seem nice. You have a good conversation, and exchange contact information. This is a great start to making friends in your class!')
            social += 10
            print("Social: +10")
            return
        elif talkChoice == '2':
            print('You decide to keep to yourself, and hope someone talks to you. Unfortunately, no one does, and you spend the entire class feeling lonely and isolated. This is not a great start to making friends in your class.')
            print("Social: -10")
            print("Happiness: -10")
            happiness -= 10
            social -= 10
            return
        else:
            print('Invalid choice, please try again.')



def compSciMonday():
    global social
    global happiness
    print('''Welcome to your first computer science class!
        In this class, you will learn the basics of programming, algorithms, and data structures. ''')
    enterContinue()
    introduceYourself()
    
    

def passingPeriodCompToPhil():
    #This function simulates the passing period between Computer Science and Philosophy.
    print("After some preliminary introductions and icebreakers, ")
    print("computer science has ended! You have fifteen minutes before Philosophy starts.")
    enterContinue()

#----compsci end--------------------------------
#philosophy start------------------------------
    
def philMonday():
#This function simulates Philosophy class on Monday.
#The first choice is social: introduce oneself or stay isolated,
#affecting social and happiness variables.
#The second choice is academic: pretend to have done the reading
#or admit not doing it. Pretending slightly decreases happiness,
#admitting can decrease GPA, social, and happiness.
#This demonstrates cumulative effects of multiple decisions in a single class.
    global social
    global happiness
    global gpa
    print('''Welcome to your first philosophy class!
        In this class, you will learn about the history of philosophy, and the different branches of philosophy.''')
    introduceYourself()
    enterContinue()
    print('''        Oh no! After the teacher begins asking reading questions, you realize there was a reading due before class. You didn't do it! Do you:
        1. Pretend you did the reading and hope the teacher doesn't notice
        2. Admit that you didn't do the reading and hope the teacher is understanding''')
   
    while True:
        readingChoice = input('Enter 1 or 2: ')
        print()
        if readingChoice == '1':
            print("You decide to pretend you did the reading, and hope the teacher doesn't notice. You get away with it, (barely) but you feel guilty about it. This is not a great way to start off your philosophy class, but at least you didn't get in trouble.")
            print("Happiness: -5")
            happiness -= 5
            return
        elif readingChoice == '2':
            print("You decide to admit that you didn't do the reading, and hope the teacher is understanding. Unfortunately, the teacher is not understanding, and shames you infront of the class. This is not a great way to start off your philosophy class, and it will be hard socially recover from this.")
            print("On top of this, you receive a bad grade on the reading assignment, which will affect your overall grade in the class.")
            print("Happiness: -10")
            print("Social: -20")
            print("GPA: -10")
            gpa -= 10
            happiness -= 20
            social -= 20
            return
        else:
            print('Invalid choice, please try again.')
    


def philToMath():
#This function simulates the passing period between Philosophy and Math.
    print("Philosophy has ended, thank goodness. Your teacher gave you one assignment: Journal each day this week.")
    print("You have ten minutes before Math starts.")
    enterContinue()
#---phil end----------------------------------------
#---math start---------------------------------------
#Simulates Math class on Monday. Includes a social choice
#(interacting with classmates or staying isolated), which affects
#social and happiness variables. Then the player chooses how to focus
#during class: paying attention increases GPA, scrolling slightly
#increases happiness, and napping decreases GPA, social, and happiness.
#This models consequences of attentiveness and engagement in school.

def mathMonday():
    global social
    global happiness
    global gpa
    mathLonely = False
    print('''Welcome to your first math class!
        In this class, you will learn about calculus, linear algebra, and differential equations. ''')
    enterContinue()
    introduceYourself()
    print()
    print(''' Luckly for you, there was no reading due before class, so you don't have to worry about that. Your teacher seems nice, but very boring.''')
    print(''' About fifteen minutes into class, you start to feel very bored and distracted. Do you:
          1. Try to pay attention and take notes
          2. Give up and start scrolling through your phone
          3. Take a power nap''')
    
    while True: 
        focusChoice = input('Enter 1, 2, or 3: ')
        if focusChoice == '1':
            print('You decide to take notes, and try to pay attention. This is a good choice, as there is an assignment due next class, and you understand how to do it. Great work!''')
            print("GPA: +5")
            gpa += 5
            happiness += 5
            return
        elif focusChoice == '2':
            print("You decide to scross through social media for the rest of class. You're not sure what was taught, but at least the time went by faster. ")
            print("You think you heard someone mention an assignment due next class, but you're not sure. ")
            happiness += 2
            return
        elif focusChoice == '3':
            print("You decide to take a power nap, and hope you don't miss anything. ")
            enterContinue()
            print("You wake up about thirty minutes later, to a poke on your shoulder.")
            enterContinue()
            print('''It's the teacher of the next class. 
              You look around to see about 20 strangers staring at you, and you realize you missed the entire math class. ''')
            print("This is not a great way to start off your math class, and it will be hard to catch up. Additionally, you've embarassed yourself!")
            print("GPA: -5")
            print("Happiness: -20")
            print("Social: -20")
            happiness -= 20
            social -= 20
            gpa -= 5
            enterContinue()
            return
        else:
            print('Invalid choice, please try again.')


#-----------------------------------------------------------------
#Socl start-------------------------------------------------------
#Simulates Sociology class on Monday with a social choice.
#Introducing oneself increases social variable, while isolation
#decreases social and happiness. This class has no academic effect.

def soclMonday():
    global social
    global happiness
    soclLonely = False
    print('''Welcome to your first sociology class!
        In this class, you will learn about the different theories of society, and how they apply to the world around you. ''')
    enterContinue()
    introduceYourself()
    enterContinue()
    print('Your teacher writes a few things on the board, which will be important to remember.')
    enterContinue()
    print('''
          My name is Mr. Johnson. Quizzes: 3, Exams: 2 (midterm and final), Paper: 1 (due at the end of the semester).

          Looking forward to a great semester!
          
          ''')

#---Study, Fitness, and Dinner Monday Functions-----------
#These functions simulate free-time activities at the end of Monday.
#studyMonday allows the player to complete homework, increasing GPA.
#gFitMonday represents attending a group fitness class, which increases
#happiness and social connections. dinnerMonday represents going out
#with friends, increasing happiness and social. Each function uses
#enterContinue to pause and narrate events, reinforcing player immersion.

def studyMonday():
    global gpa
    global happiness
    print('''You decide to go to the library and start some of you're homework.
          You want to acomplish two things: a) your philosophy reading and b) your math homework. ''')
    enterContinue()
    print('''Which one do you want to start with? ''')
    
    while True:
        studyChoice = input('Enter a or b: ').lower()
        if studyChoice == 'a':
            print('You decide to start with your philosophy reading. You read the assigned text, and take some notes on it. This is a good choice, as there is a reading quiz next class, and you want to do well on it.')
            print("GPA: +5")
            gpa += 5
            return
        elif studyChoice == 'b':
            print('You decide to start with your math homework. You work through the problems, and feel more confident about the material.')
            print("GPA: +5")
            gpa += 5 
            enterContinue()
            print('''One hour later...''')
            enterContinue()
            print('''You've finished your homework! You feel accomplished, and ready for the rest of the day.''')
            print("Happiness: +10")
            happiness += 10
            return
        else:
            print('Invalid choice, please try again.')


def gFitMonday():
    global social
    global happiness
    print('''You decide to check the group fitness schedule, and see that there is a cycling class starting in thirty minutes.
          You change into your workout clothes, grab your water bottle, and head to the gym.''')
    enterContinue()
    print('''The instructor is very energetic, and the music is pumping. You have a great workout, and feel energized afterwards. This is a great way to spend your free time, and it will help you stay healthy and happy throughout the semester!''')
    print("Happiness: +10")
    happiness += 10
    enterContinue()
    print('''After your workout, the instructor invites everyone to stay for a free smoothie. You decide to stay, and you have a delicious strawberry banana smoothie. ''')
    enterContinue()
    print('''While enjoying your smoothie,
          you chat with some of the other people in the class, and you make a new friend! You decide to exchange contact information,
          and decide to grab dinner later. This is a great way to make friends, and feel your best!
          social: +10''')
    social += 10


def dinnerMonday():
    global social
    global happiness
    print('''You decide to go grab dinner with your new friend from the cycling class at a nice place by Water Tower Campus.
          You take the shuttle downtown, and have a wonderful dinner, and a sunset view of the city.
          You have a great time chatting and getting to know each other better. This is a great way to end your first day of classes, and you feel happy and fulfilled!''')
    print("Happiness: +10")
    happiness += 10
    enterContinue()

#---Day Over Monday Function------------------------------
#Summarizes the events of Monday and allows the player to choose
#how to spend free time. It calls studyMonday, gFitMonday,
#and dinnerMonday in order to simulate the evening activities.
#This function encapsulates the entire day’s progression and
#ensures global variables (GPA, social, happiness) are updated.

def dayOverMonday():
    print('''You've finished your first day of classes! 
          You had some ups and downs, but overall it was a good day. 
          You have a lot of work to do for your classes, but you're excited to learn and grow this semester!''')
    enterContinue()
    print('''It's only 2:00 PM, so you have the rest of the day to yourself. 
          Heres how you decide to spend your free time:
          1. Go to the library and start on your homework
          2. Check the group-fitness schedule and go to a class
          3. Go out and explore the city''')
    enterContinue()
    studyMonday()
    enterContinue()
    gFitMonday()
    enterContinue()
    dinnerMonday()
    enterContinue()
    print('''After a long day, you decide to head back to your dorm and relax for the rest of the night.
          You take a shower, change into your pajamas, and get into bed. You reflect on your day, and feel grateful for the experiences you had. 
          You can't wait to see what the rest of the week has in store for you!''')
    enterContinue()
    print("...")
    enterContinue()

#------------------------------------------------------------------
#Displays final stats for the day, including GPA, social, and happiness.       
def finalStats():
    statNums()



    print('''Final stats:
          GPA: ''' + str(gpa) + '''
          Social: ''' + str(social) + '''
          Happiness: ''' + str(happiness))
    enterContinue()

#This function ensures that the GPA, social, and happiness variables stay within a reasonable range (0-100). 
#It checks each variable and adjusts it if it goes above 100 or below 0. 
#This prevents unrealistic values and maintains the integrity of the simulation's scoring system.
def statNums():
    global gpa
    global happiness 
    global social
    if gpa > 100:
        gpa = 100
    if gpa < 0:
        gpa = 0
    if happiness > 100:
        happiness = 100
    if happiness < 0:
        happiness = 0
    if social > 100:
        social = 100
    if social < 0:
        social = 0




#---Full Monday Function----------------------------------
#Combines all Monday functions into one sequence.
#It starts the day, simulates each class in order, and then
#runs the end-of-day summary and free-time activities.

def mondayOlivia():
    day = 'Monday'
    startDayTitleOlivia(day)
    compSciMonday()
    passingPeriodCompToPhil()
    philMonday()
    philToMath()
    mathMonday()
    soclMonday()
    dayOverMonday()
    journalEntry(day)
    finalStats()

    
#mondayOlivia()



#TUESDAY---------TUESDAY---------TUESDAY---------TUESDAY---------TUESDAY---------TUESDAY---------TUESDAY---------TUESDAY---------

def syllabusQuiz():
    score = 0
    name = input("What is the name of your philosophy teacher? ").lower()
    if name == "dr. smith":
        score += 25
    years = input("How many years has your philosophy teacher been teaching? (integer)")
    if years == "15":
        score += 25
    reading = input("Is there a reading quiz each week? (yes or no) ")
    if reading == "yes":
        score += 25
    exam = input("How many exams are there in the philosophy class? ")
    if exam == "1":
        score += 25
    print("Your score on the syllabus quiz is: " + str(score) + "%")
    if score == 100:
        print("Great job! You know the syllabus well, and you will do great in this class!")
    elif score >= 75:
        print("Not bad! You know most of the syllabus, but you should review it more to do well in this class.")
    elif score >= 50:
        print("You know some of the syllabus, but you should review it more to do well in this class.")
    else:
        print("You don't know the syllabus very well, and you should review it more to do well in this class.")







def philTuesday():
    global social
    global happiness
    philLonely = False
    print('''Welcome to your first history of philosophy class!
        In this class, you will learn about the history of philosophy, and the different branches of philosophy. ''')
    enterContinue()
    print(''' Your teacher's name is Dr. Smith,and he has been teaching philosophy for 15 years. 
          There will only be one exam, but there is a short reading quiz each week. ''') 
    enterContinue()
    print('''       Since this is a different philosophy class, you have different classmates.''')
    introduceYourself()
    enterContinue()
    print('''About half way into class, your teacher introduces a syllabus quiz. 
          Let's hope you read it! ''')
    enterContinue()
    syllabusQuiz()
    enterContinue()
    print('''Class is now over, and you have to head to your next class. You have fifteen minutes!''')
    enterContinue()

def chineseTuesday():
    global happiness
    global social
    
    print('''Welcome to your first Chinese literature and film class!
        In this class, you will learn about Chinese literature, and how it has influenced Chinese film. ''')
    enterContinue()
    introduceYourself()
    enterContinue()
    print('Your teacher seems very nice. This will be a great class!')
    enterContinue()
    print('''You've never studied Chinese history or culture before, so you find the material very interesting. You can't wait to learn more about it!
          Your teacher assigns a short paper for next class about Chinese culture in Chicago. You think you may want to go to Chinatown to
          do some research for the paper, but you're not sure if you have time yet. Let's see how your week goes!''')
    enterContinue() 


#AFTER SCHOOL STUFF

researchTopic = "" 

def chineseRestaurant():
    global happiness
    global social
    global researchTopic
    researchTopic = "food"
    print('餐馆')
    print('''You decide to visit a few restaurants and try some foods from different regions. 
          
         ~~ remember to write down your experiences, it will help with your presentation later!! ~~
          
          ''')
    enterContinue()
    print('''First, you visit a Sichuan restaurant, and try some spicy dishes. You really enjoy the bold flavors and the numbing sensation from the Sichuan peppercorns.''')
    enterContinue() 
    print('''Next, you visit a Cantonese restaurant, and try some dim sum. You love the variety of small dishes, and the delicate flavors of the Cantonese cuisine. You especially enjoy the shrimp dumplings and the egg tarts.''')
    enterContinue()
    print('''Third, you visit Taiwanese restaurant, and try some bubble tea and some street food. You really enjoy the sweet and refreshing taste of the bubble tea, and the crispy and flavorful street food. You especially enjoy the fried chicken.''')
    enterContinue()
    print('''finally, you visit a northern Chinese restaurant, and try some dumplings and noodles. You really enjoy the hearty and comforting flavors of the northern chinese cuisine. You especially enjoy the pork dumplings and the beef noodles. ''')
    enterContinue()
    print('''While at the northern Chinese restaurant, the elderly owner strikes up a conversation with you, and you have a great time chatting with him. 
          He tells you about his life, and how he came from China 30 years ago to Chicago.''')
    enterContinue()
    print('''      
           His favorite menu item is the pork dumplings, which you just tried, and he is so happy to hear that you enjoyed them. 
          You tell him about your class, and he stresses you mention the vast diversity of Chinese culture in your paper, and how it is important to recognize that there is not just one "Chinese culture".
          You have gained so much insight from this conversation, and you are so grateful that you had the opportunity to talk to him.
          
           This is a great way to learn more about the culture, and make a new friend!''')
    print("Happiness: +10")
    print("Social: +10")
    happiness += 10
    social += 10
    
def herbalMedicine():
    global happiness
    global social
    global researchTopic
    researchTopic = "medicine"
    print('草药店')
    print('''You decide to go to a traditional Chinese herbal medicine shop, and learn about different herbal remedies used in Chinese culture.

                        ~~ remember to write down your experiences, it will help with your presentation later!! ~~


          The shop is filled with the smell of herbs, and you see jars of different herbs lining the walls. 
          The shop owner is very knowledgeable, and he tells you about the different herbs and their uses. ''')
    enterContinue()
    print('''He makes you a cup of Anti-Aging Peach Gum Soup', which is made from:
          -peach gum, which is a resin from peach trees that is believed to have anti-aging properties
          -lotus seeds, which are believed to have calming properties
          -red dates, which are believed to have a sweet and nourishing effect on the body
          -Snow fungus, which is believed to have a cooling and moisturizing effect on the body
          -Goji berries, which are believed to have a sweet and nourishing effect on the body
          -Rock sugar, which is used to sweeten the soup''')
    enterContinue()
    print('''
          You learn about how traditional Chinese medicine is based on the concept of balance (yin and yang), and how different herbs can be used to restore balance in the body. 
          You also learn about how traditional Chinese medicine is often used in conjunction with Western medicine, and how it can be used to treat a variety of ailments. 
          This is a great way to learn more about Chinese culture, and you are so grateful for the opportunity to talk to the shop owner!''')
    print("Happiness: +10")
    print("Social: +10")
    happiness += 10
    social += 10


def musicalPerformance():
    global happiness
    global social
    global researchTopic
    researchTopic = "music"
    print('音乐表演')
    print('''You decide to go to a musical performance, and research unique Chinese instruments. 
          
          
                        ~~ remember to write down your experiences, it will help with your presentation later!! ~~
          


          The performance is held in a small theater, and you see a variety of traditional Chinese instruments on stage, such as the erhu, the pipa, and the guzheng. 
          The performers are very talented, and they play beautiful music that is both soothing and uplifting.''')
    enterContinue()
    print('''After the performance, you have the opportunity to talk to the performers and learn more about the instruments they play. ''')
    enterContinue()
    print('''Erhu: a two-stringed bowed instrument that is often used in Chinese folk music. It has a distinctive sound that is both melancholic and expressive.
             Pipa: a four-stringed plucked instrument that is often used in Chinese classical music. It has a bright and lively sound that is both virtuosic and expressive.
             Guzheng: a plucked zither that is often used in Chinese classical music. It has a rich and resonant sound that is both soothing and uplifting.''')      
          

    print('''This is a great way to learn more about Chinese culture, and you are so grateful for the opportunity to attend this performance!''')
    print("Happiness: +10")
    print("Social: +10")
    happiness += 10
    social += 10

    
def clothingShops():
    global happiness
    global social
    global researchTopic
    researchTopic = "clothes"
    print('服装店')
    print('''You decide to visit some traditional Chinese clothing shops, and learn about the different styles of clothing in different regions of China. 
          
                            ~~ remember to write down your experiences, it will help with your presentation later!! ~~



          The shops are filled with beautiful and intricate clothing, such as qipao, hanfu, and tangzhuang. 
          The shop owners are very knowledgeable, and they tell you about the different styles of clothing and their significance in Chinese culture. ''')
    enterContinue()
    print('''Qipao: a form-fitting dress that is often made of silk and features intricate embroidery. It is often worn for formal occasions, and it is a symbol of Chinese femininity and elegance.
             Hanfu: a traditional style of clothing that is often made of silk and features flowing sleeves and intricate embroidery. 
             Tangzhuang: a traditional style of clothing that is often made of silk and features a mandarin collar and frog buttons.''')      
          

    print('''This is a great way to learn more about Chinese culture, and you are so grateful for the opportunity to talk to the shop owners!''')
    print("Happiness: +10")
    print("Social: +10")
    happiness += 10
    social += 10






def chinaTown():
    global happiness
    global social
    print('''You decide to head to Chinatown to do some research for your paper. ''')
    print('''You have a few choices for how to spend your time here! 
          You can
          a) visit a couple of little restaurants and try some foods from different regions of China
          b) go to a traditional Chinese herbal medicine shop, and learn about different herbal remedies used in Chinese culture
          c) visit a musical performance, and research unique Chinese instruments
          d) visit some traditional Chinese clothings shops, and learn about the different styles of clothing in different regions of China''')
    

    
    while True:
        chinaTownChoice = input('Enter a, b, c, or d: ').lower()
        if chinaTownChoice == 'a':
            chineseRestaurant()
            return
        elif chinaTownChoice == 'b':
            herbalMedicine()
            return
        elif chinaTownChoice == 'c':
            musicalPerformance()
            return
        elif chinaTownChoice == 'd':
            clothingShops()
            return
        else:
            print('Invalid choice, please try again.')
        

 


def dormResearch():
    global researchTopic
    print('''You decide to go back to your dorm and research for your paper there. ''')
    enterContinue()
    print('''What would you like to research about?
          a) Chinese food culture in Chicago
          b) Traditional Chinese medicine in Chicago
          c) Chinese music and instruments in Chicago
          d) Traditional Chinese clothing in Chicago''')
    
    while True:
        researchChoice = input('Enter a, b, c, or d: ').lower()
        if researchChoice == 'a':
            researchTopic = "food"
            print('''You decide to research Chinese food culture in Chicago. You find a variety of articles and videos about the different types of Chinese cuisine in Chicago, and the history of Chinese food in the city. 
              You learn about the different regions of China and their unique culinary traditions, and you find some great sources for your paper!

              Some important dishes you learn about include: ''')
            enterContinue()
            print(''')
              -Sichuan cuisine, which is known for its bold and spicy flavors, and its use of Sichuan peppercorns, which create a numbing sensation in the mouth.

              -Cantonese cuisine, which is known for its delicate and subtle flavors, and its use of fresh ingredients. Dim sum is a popular Cantonese dish that consists of small, bite-sized portions of food that are often served in steamer baskets or on small plates.

              -Taiwanese cuisine, which is known for its sweet and savory flavors, and its use of street food. Bubble tea is a popular Taiwanese drink that consists of tea, milk, and chewy tapioca balls.

              -Northern Chinese cuisine, which is known for its hearty and comforting flavors, and its use of wheat-based products. Dumplings and noodles are popular dishes in northern Chinese cuisine.
              ''')
            return
        elif researchChoice == 'b':
            researchTopic = "medicine"
            print('''You decide to research Traditional Chinese medicine in Chicago. You find a variety of articles and videos about the different types of Chinese medicine in Chicago, and the history of Chinese medicine in the city. 
              You learn about the different regions of China and their unique medical traditions, and you find some great sources for your paper!''')
            enterContinue()
            print('''Some important concepts you learn about include:
                -Yin and yang, which is the concept of balance in traditional Chinese medicine. Yin represents the feminine, passive, and dark aspects of the body, while yang represents the masculine, active, and light aspects of the body. Traditional Chinese medicine aims to restore balance between yin and yang in the body.
              
                -Qi, which is the vital energy that flows through the body. Traditional Chinese medicine believes that qi can be blocked or disrupted, leading to illness. Acupuncture and herbal remedies are often used to restore the flow of qi in the body.
              
                -The five elements, which are wood, fire, earth, metal, and water. Traditional Chinese medicine believes that each element corresponds to different organs and functions in the body, and that imbalances in the elements can lead to illness.
                ''')
            return
        elif researchChoice == 'c':
            researchTopic = "music"
            print('''You decide to research Chinese music and instruments in Chicago. You find a variety of articles and videos about the different types of Chinese music in Chicago, and the history of Chinese instruments in the city. 
              You learn about the different regions of China and their unique musical traditions, and you find some great sources for your paper!''')
            enterContinue()
            print('''Some important instruments you learn about include:
                -Erhu, which is a two-stringed bowed instrument that is often used in Chinese folk music. It has a distinctive sound that is both melancholic and expressive.
              
                -Pipa, which is a four-stringed plucked instrument that is often used in Chinese classical music. It has a bright and lively sound that is both virtuosic and expressive.
              
                -Guzheng, which is a plucked zither that is often used in Chinese classical music. It has a rich and resonant sound that is both soothing and uplifting.
                ''')
            return
        elif researchChoice == 'd':
            researchTopic = "clothes"
            print('''You decide to research Traditional Chinese clothing in Chicago. You find a variety of articles and videos about the different types of Chinese clothing in Chicago, and the history of Chinese clothing in the city. 
              You learn about the different regions of China and their unique fashion traditions, and you find some great sources for your paper!''')
            enterContinue()
            print('''Some important aspects of Chinese clothing you learn about include:
                - Qipao, which is a form-fitting dress that is often made of silk and features intricate embroidery. It is often worn for formal occasions, and it is a symbol of Chinese femininity and elegance.
              
                - Hanfu, which is a traditional style of clothing that is often made of silk and features flowing sleeves and intricate embroidery. It is often worn for cultural events and festivals, and it is a symbol of Chinese cultural heritage.
              
                - Tangzhuang, which is a traditional style of clothing that is often made of silk and features a mandarin collar and frog buttons. It is often worn for formal occasions, and it is a symbol of Chinese cultural identity.
              
                ''')
            return

        else:
            print('Invalid choice, please try again.')
        

chinaTownTravel = False

def afterSchoolTuesday():
    global happiness
    global social
    global chinaTownTravel
    print('''Your classes are now over for today. Would you like to:
          1. Head to Chinatown to do some research for your paper
          2. Go back to your dorm and research for your paper there''')
    
    while True:
        afterSchoolChoice = input('Enter 1, or 2: ')
        if afterSchoolChoice == '1':
            chinaTownTravel = True
            chinaTown()
            print('''After spending the day in Chinatown, you feel like you have learned so much about Chinese culture, and you have had a great time exploring the city.
          You take the train back to campus, and make your way to your dorm. You feel happy and fulfilled, and you can't wait to start writing your paper!''')
            print()
            return
        elif afterSchoolChoice == '2':
            dormResearch()
            return
        else:
            print('Invalid choice, please try again.')
        






def tuesdayOlivia():
    day = 'Tuesday'
    startDayTitleOlivia(day)
    philTuesday()
    chineseTuesday()
    afterSchoolTuesday()
    journalEntry(day)
    finalStats()

#tuesdayOlivia()

#WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------WEDNESDAY---------

def compWednesday():
    global happiness
    global gpa
    global social
    print('''Welcome to your second computer science class!''')
    print('''Today's class is offered online in addition to the regular class. Would you like to attend online? 
          
          ''')

         
    classChoice = input('Enter yes or no: ').lower()
    if classChoice == 'yes':
        print('''You'll be attending from your dorm room. 
          You log into the zoom, and set your computer onto the desk, putting in your headphones. The teacher starts the class, and you follow along with the lecture.
          ''')
        enterContinue()
        print('''About five minutes into the lecture, your roomate walks into the room.''')
        enterContinue()
        print('''ROOMATE: "Hey, I'm back from the gym. What are you up to?''')
        print('''YOU: "Just attending my computer science class. It's online today."''')
        enterContinue() 
        print('''ROOMATE: "Ugh, that's so boring. OMG your class looks like its full of weirdos.''')
        enterContinue()
        print('''YOU: I know, but it's a required course.''')
        enterContinue()
        print('''TEACHER: Excuse me? You seem to be having an extremely disrespectful conversation in my class. I am going to have to ask you to leave.''')
        enterContinue()
        print('''That was not good.
          
          You scold your roommate, and put your head in your hands. You can't believe that just happened.
          
          You will have to find a time to talk to your teacher and explain the situation.''')
        print("Happiness: -20")
        print("Social: -20")
        print("GPA: -10")
        happiness -= 20 
        social -= 20
        gpa -= 10
    
    elif classChoice == 'no':
        print('''You decide to attend the regular in-person class. You get ready, and head to class. The teacher starts the lecture, and you follow along with it.
          
              
              About fifteen minutes into the lecture, you feel a slight pop, and hear a little crack.''')
        enterContinue()
        print('''Suddenly, you go crashing to the ground!
              


              your chair broke! (っ╥﹏╥ς)
              

              
              The room goes silent, and everyone looks at you as you try to process what just happened. 
              
              You feel embarrassed, and you quickly get up and try to fix the chair, but it's no use. The chair is completely broken.''') 
        enterContinue()
        print('''TEACHER: Are you okay? Do you need to go to the health center?''')
        enterContinue()
        print('''YOU: No, I'm fine. I just need to get a new chair''')
        enterContinue()
        print('''Your classmate offers you a new chair, and you take it happily.''')
        print("You try to focus as much as possible, but you can't stop thinking about how embarrassing that was. You hope that no one remembers it, but you know that it's going to be hard to live down.")
        happiness -= 10
        print("Happiness: -10")
        enterContinue()
    

def philWednesday():
    global social     
    global happiness
    global gpa
    print('''After that disaster of a morning, you would rather do anything than go to class.''')
    enterContinue()

    while True:
        skipChoice = input('''Do you want to skip class today? (yes or no) '''). lower()
        if skipChoice == 'yes':
            print('''You decide to skip class, how would you like to spend your time? 
              a) Go to the library and do some homework
              b) Go to the gym and work out
              c) Go to a cafe and relax''')
            while True:
                skipActivity = input('Enter a, b, or c: ').lower()
                if skipActivity == 'a':
                    print('''You decide to go to the library and do some homework. You find a quiet spot, and get to work on your philosophy reading. 
                  You feel productive, and you are glad that you decided to skip class and do something productive instead!''')
                    print("GPA: +5")
                    gpa += 5
                    return
                elif skipActivity == 'b':
                    print('''You decide to go to the gym and work out. You have a great workout, and you feel energized afterwards. 
                  You are glad that you decided to skip class and do something healthy instead!''')
                    print("Happiness: +10")
                    happiness += 10
                    return
                elif skipActivity == 'c':
                    print('''You decide to go to a cafe and relax. You find a cozy cafe, and order a coffee. You sit down and enjoy your coffee, and you feel relaxed and refreshed. 
                  You are glad that you decided to skip class and do something enjoyable instead!''')
                    print("Happiness: +10")
                    happiness += 10
                    return
                else:
                    print('Invalid choice, please try again.')
               
        elif skipChoice == 'no':
            print('''You decide to go to class, and try to have a good experience. You get ready, and head to class. ''')

            print('''You walk into class, and see that your teacher has brought cupcakes for everyone!
          
            TEACHER: "I know that the first week of classes can be stressful, so I thought I would bring some cupcakes to help everyone relax and feel welcome!" ''')
            enterContinue()
            print('''
          
            You are so surprised and grateful for this kind gesture. You take a cupcake, and sit down next to a classmate who also took a cupcake. 
          
            You strike up a conversation about how nice the teacher is, and you exchange contact information. 
          
            This is a great way to make friends in your class, and you feel much better after that morning's incident!

          ''')
            enterContinue()
            print('TEACHER: "Also, I just wanted to remind everyone that there is a reading quiz next class, so make sure to read the syllabus and do the reading!')
            enterContinue()
            print('''Social: +10''')
            social += 10
            print('''Happiness: +10''')
            happiness += 10
            return
        else:
            print('Invalid choice, please try again.')
            


def mathGame():
    mathPoints = 0

    questions = ["2+2=?", "5-3=?", "3*3=?"]
    answers = ["4", "2", "9"]


    for i in range(len(questions)):
        answer = input(f"Solve this math problem: {questions[i]} ")
        if answer == answers[i]:
            print("Correct!")
            print("Math points: +10")
            mathPoints += 10
    else:
        print("Oops, that's wrong.")

    print("Total math points:" + str(mathPoints))

    if mathPoints == 30:
        print("Wow, you got a perfect score on the math game! You must be a math genius!")
    elif mathPoints >= 20:
        print("Not bad! You got " + str(mathPoints) + " points on the math game, but you could have done better.")
    elif mathPoints >= 10:
        print("You did okay on the math game, you got " + str(mathPoints) + " points, but you definitely struggled with some of the problems.")
    else:
        print("Yikes, you did not do well on the math game. You got " + str(mathPoints) + " points. You should probably review your math skills before the exam.")
    
    



def mathWednesday():
    global social
    global happiness
    enterContinue()
    print('''It is now time for math class, and you're hoping for another good experience.''')
    enterContinue()
    print('''You walk into class, and see that your teacher has set up a little game for everyone to play. 
          The game is called "Math Jeopardy," and it's a fun way to review the material before the first exam. ''')
    enterContinue()
    
    while True:
        mathChoice = input("Would you like to participate in the game? (yes or no) ").lower()
        if mathChoice == 'yes':
            mathGame()
            print('''You decide to participate, and you have a great time playing the game with your classmates. 
          This is a great way to make friends in your class, and you feel much more confident about the material after playing the game!''')
            print('''Social: +10''')
            social += 10
            print('''Happiness: +10''')
            happiness += 10
            return
        elif mathChoice == 'no':
            print('''You decide not to participate, and you sit on the sidelines while your classmates play the game. 
          You feel a little left out, and you wish that you had participated in the game. 
          This is not a great way to make friends in your class, and you've missed out on some math review.''')
            print('''Social: -10''')
            social -= 10
            print('''Happiness: -10''')
            happiness -= 10
            return
        else:
            print('Invalid choice, please try again.')
        
        enterContinue()


def soclSyllabusQuiz():
    global gpa
    score = 0
    name = input("What is the name of your sociology teacher? ").lower()
    if name == "mr. johnson":
        score += 25
    quizzes = input("How many quizzes are there in the sociology class? ").lower()
    if quizzes == "3":
        score += 25
    exam = input("How many exams are there in the sociology class? ")
    if exam == "2":
        score += 25
    paper = input("How many papers are there in the sociology class? ")
    if paper == "1":
        score += 25

    print()
    print("Your score on the syllabus quiz is: " + str(score) + "%")
    if score == 100:
        print("Great job! You know the syllabus well, and you will do great in this class!")
        gpa += 20
        print("GPA: +20")
    elif score >= 75:
        print("Not bad! You know most of the syllabus, but you should review it more to do well in this class.")
        gpa += 10
        print("GPA: +10")
    elif score >= 50:
        print("You know some of the syllabus, but you should review it more to do well in this class.")
        gpa += 5
        print("GPA: +5")
    else:
        print("You don't know the syllabus very well, and you should review it more to do well in this class.")
        gpa -= 10
        print("GPA: -10")



def soclWednesday():
    global social
    global happiness
    print('''After your math class, you head to sociology.''')
    enterContinue()
    print('''Your teacher has set up a syllabus quiz for today, lets see what you remember from monday!''')
    print('''Good Luck!''')
    soclSyllabusQuiz()
    print()
    print('''After the quiz, your teacher goes over the syllabus again, and explains the course requirements.''')
    enterContinue()
    print('''While your teacher is nice, you can't wait for the class to end, so you can grab lunch.''')
    enterContinue()

def daylunchWednesday():
    print('''After your sociology class, you are starving, and need to grab lunch!''')
    print('''You have a few options for where to eat:
          a) The dining hall, where you can get a variety of different foods, but the quality is not great
          b) A nearby cafe, where you can get a sandwich and a salad, but it's a little expensive
          c) A fast food restaurant, where you can get a quick and cheap meal, but it's not very healthy''')
    
    while True:
        lunchChoice = input('Enter a, b, or c: ').lower()
        if lunchChoice == 'a':
            print('''You decide to go to the dining hall, and you find a variety of different foods to choose from. 
                  You end up getting a slice of pizza, some fries, and a salad. The food is not great, but it's filling and it's free!''')
            return
        elif lunchChoice == 'b':
            print('''You decide to go to a nearby cafe, and you order a sandwich and a salad. The food is delicious, but it's a little expensive. 
                  You enjoy your meal, and you feel satisfied after eating it!''')
            return
        elif lunchChoice == 'c':
            print('''You decide to go to a fast food restaurant, and you order a burger and fries. The food is quick and cheap, but it's not very healthy. 
                  You enjoy your meal, but you could have made a healthier choice!''')
            return
        else:
            print('Invalid choice, please try again.')
        
        


def baking():
    global happiness
    global social
    print('''You've decided to bake something! There are a few options.''')
    enterContinue()
    print('''You can bake:
          a) Chocolate chip cookies, which are a classic and delicious treat.
          b) Banana bread, which is a great way to use up those overripe bananas in your dorm.
          c) Brownies, which are a rich and indulgent dessert that is perfect for sharing with friends.''')
    
    while True:
        bakeChoice = input('Enter a, b, or c: ').lower()
        if bakeChoice == 'a':
            print('''You decide to bake chocolate chip cookies, and you gather the ingredients. You have a great time baking, and you enjoy the delicious cookies that you made!
                You decide to share the cookies with the rest of your floor, and they all love them!
                 This is a great way to make friends on your floor, and you feel happy that you were able to share something you made with others!
               
              
                ''')
            print("Happiness: +10")
            print("Social: +10")
            happiness += 10
            social += 10
            return
        elif bakeChoice == 'b':
            print('''You decide to bake banana bread, and you gather the ingredients. You have a great time baking, and you enjoy the delicious banana bread that you made!
              You decide to share the banana bread with your roommate, and they love it! 
              This is a great way to strengthen your relationship with your roommate, and you feel happy that you were able to share something you made with them!''')

            print("Happiness: +10")
            print("Social: +10")
            social += 10
            happiness += 10
            return
        elif bakeChoice == 'c':
            print('''You decide to bake brownies, and you gather the ingredients. You have a great time baking, and you enjoy the delicious brownies that you made!
              You decide to share the brownies with the rest of your floor, and they all love them! 
              This is a great way to make friends, and you feel happy that you were able to share something you made with others!''')
        
            print("Happiness: +10")
            print("Social: +10")
            social += 10
            happiness += 10
            return
        else:
            print('Invalid choice, please try again.')
        
    




def dayOverWednesday():
    global gpa

    enterContinue()
    print('''After you finish your lunch, you head back to your dorm. ''')
    print('''You notice the large kitchenette on the first floor of your dorm, and wonder if you should bake something...''')
    
    while True:
        bakeChoice = input('Do you want to bake something, or go to your dorm and study? (enter bake or study) ').lower()
        if bakeChoice == 'bake':
            print()
            baking()
            return
        elif bakeChoice == 'study':
            print()
            print('''You decide to go to your dorm and study, and you spend the evening reviewing your notes and doing some practice problems. 
              You feel productive, and you are glad that you decided to study, but could have used a sweet treat!''')
            print("GPA: +5")
            gpa += 5
            return
        else:
            print('Invalid choice, please try again.')
        




def wednesdayOlivia():
    day = 'Wednesday'
    startDayTitleOlivia(day)
    compWednesday()
    philWednesday()
    mathWednesday()
    soclWednesday()
    daylunchWednesday()
    dayOverWednesday()
    enterContinue()
    journalEntry(day)
    print()
    finalStats()


#--------------------------------------------------------------------
#-THURSDAY---------THURSDAY---------THURSDAY---------THURSDAY---------THURSDAY---------

def thursdayMorning():
    global happiness
    print("You wake up earlier than usual on Thursday morning, and you have some extra time before you have to get ready. What would you like to do before breakfast?")
    
    while True:
        morningChoice = input('''Enter a, b, or c:
          a) Go for a morning run around campus
          b) Scroll on your phone and check social media
          c) Go back to sleep                 choice: ''').lower()
        if morningChoice == 'a':
            print()
            print('''You decide to go for a morning run around campus, and you have a great time exploring the different paths and trails around campus.
              The sun is shining, the birds are chirping, and all the good endorphins are flowing.

              You feel energized and refreshed after your run, and you are glad that you decided to start your day with some exercise!''')
            print("Happiness: +10")
            happiness += 10
            return
        elif morningChoice == 'b':
            print()
            print('''You decide to scroll on your phone and check social media, and you end up spending a lot of time looking at other people's posts and comparing yourself to them. 
              You feel a little down after scrolling through social media, and you wish that you had done something more productive with your time!''')
            print("Happiness: -10")
            happiness -= 10
            return
        elif morningChoice == 'c':
            print()
            print('''You decide to go back to sleep, and you end up sleeping in for a few more hours. You feel rested and refreshed after sleeping in, but you also feel a little hungry since you missed breakfast!''')
            print("Happiness: +10")
            happiness += 10
            return
        else:
            print('Invalid choice, please try again.')



def philGame():
    print('''You have to guess the philosophy-themed word based on the few letters you are given.''')
    print('''ROUND ONE: ''')
    word1 = "Aristotle"
    letters1 = "A _ i _ o t l e"
    print(letters1)
    guess1 = input("Enter your guess: ").lower()
    if guess1 == word1.lower():
        print("Correct! You guessed the word!")
        print("Philosophy points: +10")
        philosophyPoints = 10
    else:
        print("Oops, that's wrong. The correct word was: " + word1)
        philosophyPoints = 0
    print('''ROUND TWO: ''')
    word2 = "Plato"
    letters2 = "P l a _ o"
    print(letters2)
    guess2 = input("Enter your guess: ").lower()
    if guess2 == word2.lower():
        print("Correct! You guessed the word!")
        print("Philosophy points: +10")
        philosophyPoints += 10
    else:
        print("Oops, that's wrong. The correct word was: " + word2)
    print('''ROUND THREE: ''')
    word3 = "Socrates"
    letters3 = "S _ c r a t e s"
    print(letters3)
    guess3 = input("Enter your guess: ").lower()
    if guess3 == word3.lower():
        print("Correct! You guessed the word!")
        print("Philosophy points: +10")
        philosophyPoints += 10
    else:
        print("Oops, that's wrong. The correct word was: " + word3)
    print()
    print("Total philosophy points: " + str(philosophyPoints))
    if philosophyPoints == 30:
        print("Wow, you got a perfect score on the philosophy game! You must be a philosophy genius!")
    elif philosophyPoints >= 20:
        print("Not bad! You got " + str(philosophyPoints) + " points on the philosophy game, but you could have done better.")
    elif philosophyPoints >= 10:
        print("You did okay on the philosophy game, you got " + str(philosophyPoints) + " points, but you definitely struggled with some of the questions.")
    else:
        print("Yikes, you did not do well on the philosophy game. You got " + str(philosophyPoints) + " points. You should probably review your philosophy notes before the exam.")




def philThursday():
    global social
    global happiness
    global gpa
    print('''You head to your philosophy class, and you are surprised to see that your teacher has set up a little game for everyone to play.''')
    enterContinue()
    print(''' lot of games this week, huh.''')
    enterContinue()
    print('''The game is called "Philosophy Word Guess," and it's a fun way to review the material before the first exam. 
          The teacher gives you a philosophical concept, and you have to draw it on the board while your classmates try to guess what it is. ''')
    enterContinue()
    participateChoice = input('''Would you like to participate in the game? (yes or no) ''').lower()
    
    while True:
        if participateChoice == 'yes':
            philGame()
            print('''You had a great time playing with your classmates. 
              This is a great way to make friends in your class, and you feel much more confident about the material after playing the game!''')
            print('''Social: +10''')
            social += 10
            print('''Happiness: +10''')
            happiness += 10
            return
        elif participateChoice == 'no':
            print('''You decide not to participate, and you sit on the sidelines while your classmates play the game. 
          You feel a little left out, and you wish that you had participated in the game. 
          This is not a great way to make friends in your class, and you've lost out on some philosophy review.''')
            print('''Social: -10''')
            social -= 10
            print('''Happiness: -10''')
            happiness -= 10
            gpa -= 5
            print('''GPA: -5''')
            return
        else:
            print('Invalid choice, please try again.')
        


presentationPoints = 0

def chinaTownQuestions():
    global gpa
    global presentationPoints
    global researchTopic
    if researchTopic == "food":
        sichuanCuisine = input("Johnny: What is the name of the cuisine that is known for its bold and spicy flavors, and its use of Sichuan peppercorns? ").lower()
        if sichuanCuisine == "sichuan cuisine" or sichuanCuisine == "sichuan":
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Sichuan cuisine.")
            gpa -= 5
            print("GPA: -5")

        shopKeeperFood = input("Alyssa: What was the shop owner's favorite dish? ").lower()
        if shopKeeperFood == "pork dumplings":
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Pork Dumplings.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "medicine":
        yinYang = input("Johnny: What is the concept of balance in traditional Chinese medicine? ").lower()
        if yinYang == "yin and yang" or yinYang == "yin & yang":
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Yin and Yang.")
            gpa -= 5
            print("GPA: -5")
        shopKeeperMedicine = input("Alyssa: What was the medicinal property of the Peach Gum soup you tried? ").lower()
        if shopKeeperMedicine == "anti-aging" or shopKeeperMedicine == "anti aging":
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Anti-Aging.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "music":
        erhuStrings = input("Johnny: How many strings does the Erhu have? ").lower()
        if erhuStrings == "2" or erhuStrings == "two":
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: 2.")
            gpa -= 5
            print("GPA: -5")
        placeHeld = input("Alyssa: Where was the musical performance you attended held? ").lower()
        if placeHeld == "theatre" or placeHeld == "theater":
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Theatre.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "clothes":
        qipaoMaterial = input("Johnny: What material is the Qipao often made of? ").lower()
        if qipaoMaterial == "silk":
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Silk.")
            gpa -= 5
            print("GPA: -5")
        frogButtons = input("Alyssa: What type of buttons does the Tangzhuang often feature? ").lower()
        if frogButtons == "frog buttons" or frogButtons == "frog":
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: Frog buttons.")
            gpa -= 5
            print("GPA: -5")
    
        
def dormQuestions():
    global presentationPoints
    global gpa
    global researchTopic
    if researchTopic == "food":
        sichuanCuisine = input("Johnny: What is the name of the cuisine that is known for its bold and spicy flavors, and its use of Sichuan peppercorns? ").lower()
        if sichuanCuisine == "sichuan cuisine" or sichuanCuisine == "sichuan":
            print()
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Sichuan cuisine.")
            gpa -= 5
            print("GPA: -5")
        northernCuisine = input("Alyssa: What type of cuisine is known for its hearty and comforting flavors, and its use of wheat-based products? ").lower()
        if northernCuisine == "northern chinese cuisine" or northernCuisine == "northern cuisine" or northernCuisine == "northern":
            print()
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Northern Chinese cuisine.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "medicine":
        yinYang = input("Johnny: What is the concept of balance in traditional Chinese medicine? ").lower()
        if yinYang == "yin and yang" or yinYang == "yin & yang":
            print()
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            presentationPoints += 50
            gpa += 15
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Yin and Yang.")
            gpa -= 5
            print("GPA: -5")
        fiveElements = input("Alyssa: What are the five elements in traditional Chinese medicine? ").lower()
        if fiveElements == "wood, fire, earth, metal, and water" or fiveElements == "wood fire earth metal and water":
            print()
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Wood, Fire, Earth, Metal, and Water.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "music":
        erhuStrings = input("Johnny: How many strings does the Erhu have? ").lower()
        if erhuStrings == "2" or erhuStrings == "two":
            print()
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: 2.")
            gpa -= 5
            print("GPA: -5")
        pipaStrings = input("Alyssa: How many strings does the Pipa have? ").lower()
        if pipaStrings == "4" or pipaStrings == "four":
            print()
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print("Oops, that's wrong. The correct answer was: 4.")
            gpa -= 5
            print("GPA: -5")
    elif researchTopic == "clothes":
        qipaoMaterial = input("Johnny: What material is the Qipao often made of? ").lower()
        if qipaoMaterial == "silk":
            print()
            print("You correctly answered Johnny's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Silk.")
            gpa -= 5
            print("GPA: -5")
        hanfuSleeves = input("Alyssa: What type of sleeves does the Hanfu often feature? ").lower()
        if hanfuSleeves == "flowing sleeves" or hanfuSleeves == "flowing":
            print()
            print("You correctly answered Alyssa's question!")
            print("GPA: + 15")
            gpa += 15
            presentationPoints += 50
        else:
            print()
            print("Oops, that's wrong. The correct answer was: Flowing sleeves.")
            gpa -= 5
            print("GPA: -5")
     
def presentationScore():
    global presentationPoints
    if presentationPoints == 100:
        print("Wow, you got a perfect score on your presentation! You must be a presentation pro!")
    elif presentationPoints == 50:
        print("Not bad! You got " + str(presentationPoints) + " points on your presentation, but you could have done better.")
    elif presentationPoints == 0:
        print("Yikes, you did not do well on your presentation. You got " + str(presentationPoints) + " points. You should probably review your presentation skills before the next one.")




def chineseQuestions():
    global chinaTownTravel
    if chinaTownTravel == True:
        chinaTownQuestions()
    else:
        dormQuestions()
       

def chineseThursday():
    print('''Today is your Chinese culture presentation! Hopefully it goes well.''')
    enterContinue()
    print('''Your classmates will ask you some questions about your presentation, so be ready!''')
    enterContinue()
    print("You complete your presentation about " + str(researchTopic) + ", and you feel pretty good about it.")
    print("Your classmates will ask you a few questions now!")
    enterContinue()
    chineseQuestions()
    presentationScore()



def thursdayOlivia():
    day = 'Thursday'
    startDayTitleOlivia(day)
    thursdayMorning()
    philThursday()
    chineseThursday()
    enterContinue()
    journalEntry(day)
    print()
    finalStats()
    



#----------------------------------------------------
#- FRIDAY---------FRIDAY---------FRIDAY---------FRIDAY---------FRIDAY---------FRIDAY---------FRIDAY---------FRIDAY---------

compPoints = 0

def compQuiz():
    global compPoints
    comment = input("What symbol begins a comment in Python? ")
    if comment == "#":
        print()
        print("Correct! You know how to write comments in Python!")
        print("+20 points")
        compPoints += 20
    else:
        print()
        print("Oops, that's wrong. The correct answer was: #.")
        print("-10 points")
        compPoints -= 10
    boolean = input("What variable stores 'True' or 'False' values? ")
    if boolean == "boolean" or boolean == "bool":
        print()
        print("Correct! You know about boolean variables in Python!")
        print("+20 points")
        compPoints += 20
    else:
        print()
        print("Oops, that's wrong. The correct answer was: Boolean or bool.")
        print("-10 points")
        compPoints -= 10
    defineFunction = input("What keyword is used to define a function in Python? ")
    if defineFunction == "def":
        print()
        print("Correct! You know how to define a function in Python!")
        print("+20 points")
        compPoints += 20
    else:
        print()
        print("Oops, that's wrong. The correct answer was: def.")
        print("-10 points")
        compPoints -= 10
    
    print()
    print("Your score on the computer science quiz is: " + str(compPoints) + " out of 60 points.")
    if compPoints == 60:
        print("Wow, you got a perfect score on the computer science quiz! You must be a coding genius!")
    elif compPoints == 40:
        print("Not bad! You got " + str(compPoints) + " points on the computer science quiz out of 60, but you could have done better.")
    elif compPoints == 20:
        print("You did okay on the computer science quiz, you got " + str(compPoints) + " points out of 60, but you definitely struggled with some of the questions.")
    else:
        print("Yikes, you did not do well on the computer science quiz. You got " + str(compPoints) + " points out of 60. You should probably review your computer science notes before the next quiz.")
    

def compFriday():
    global happiness
    global gpa
    global social
    print('''Welcome to your final computer science class! We are sad to see you go. :(''')
    print()
    print('''Honestly, you are just glad it is over.''')
    enterContinue()
    print('''You've not had great experiences this week in this class...but maybe today will make up for it?''')
    enterContinue()
    print('''Just your luck. You have a pop quiz.  Good Luck!''')
    enterContinue()
    compQuiz()
    print()
    print('''After the quiz, you leave class, and you are just glad that it's over. Time for philosophy!''')


def ethicsDebateShow():
    global social
    global happiness
    global gpa
   
    print("You walk into class, and the professor has turned it into an Ethics Debate Game Show!")
    enterContinue()

    # --- Scenario 1 ---
    print('''Scenario 1: You find a wallet on the street with $500 inside. Do you keep it or try to return it?''')
    print('''How do you respond?
                    1. Argue honesty
                    2. Make a funny argument
                    3. Stay quiet''')

    choice = ""
    while choice not in ['1','2','3']:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            print("You explain that returning the wallet demonstrates honesty. Classmates nod approvingly.")
            social += 5
            happiness += 5
            gpa += 10
            print("Social: +5, Happiness: +5, GPA: +10")
        elif choice == '2':
            print("You joke about your goldfish needing the money. Everyone laughs!")
            social += 10
            happiness += 10
            gpa -= 5
            print("Social: +10, Happiness: +10, GPA: -5")
        elif choice == '3':
            print("You stay quiet and feel a little invisible.")
            social -= 5
            happiness -= 5
            print("Social: -5, Happiness: -5")
        else:
            print("Invalid choice, try again.")

    enterContinue()

    # --- Scenario 2 ---
    print('''Scenario 2: A robot at a grocery store drops a shipment of apples. Do you help it or walk away?''')
    print('''How do you respond?
1. Argue moral duty
2. Make a funny comment
3. Ignore it''')

    choice = ""
    while choice not in ['1','2','3']:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            print("You argue helping is the right thing. Professor nods in approval.")
            social += 5
            happiness += 5
            gpa += 10
            print("Social: +5, Happiness: +5, GPA: +10")
        elif choice == '2':
            print("You joke about robots needing manners. Classmates laugh!")
            social += 10
            happiness += 10
            gpa -= 5
            print("Social: +10, Happiness: +10, GPA: -5")
        elif choice == '3':
            print("You ignore it. You feel a little guilty.")
            social -= 5
            happiness -= 5
            print("Social: -5, Happiness: -5")
        else:
            print("Invalid choice, try again.")

    enterContinue()







def philFriday():
    global happiness
    global social
    ethicsDebateShow()
    print("You had a good time in class today, and you enjoyed listening to your classmates' arguments.")
    print("What a good end to the week!")
    print('''
          
          
          ''')


fridayQuizPoints = 0

def mathTestFriday():
    global fridayQuizPoints
    global gpa
    question1 = input("What is (10 + 5) * 2? ")
    if question1 == "30":
        print("Correct! You know how to do order of operations!")
        fridayQuizPoints += 25
    else:
        print("Oops, that's wrong. The correct answer was: 30.")
    question2 = input("How many sides does a pentagon have? ")
    if question2 == "5":
        print("Correct! A pentagon has 5 sides.")
        fridayQuizPoints += 25
    else:
        print("Oops, that's wrong. The correct answer was: 5.")
    question3 = input("What is the square root of 16? ")
    if question3 == "4":
        print("Correct! The square root of 16 is 4.")
        fridayQuizPoints += 25
    else:
        print("Oops, that's wrong. The correct answer was: 4.")
    question4 = input("What is the value of pi (to 2 decimal places)? ")
    if question4 == "3.14":     
        print("Correct! The value of pi to 2 decimal places is 3.14.")
        fridayQuizPoints += 25
    else:
        print("Oops, that's wrong. The correct answer was: 3.14.")
    print()
    print("Your score on the math test is: " + str(fridayQuizPoints) + " out of 100 points.")
    if fridayQuizPoints == 100:
        print("Wow, you got a perfect score on the math test! You must be a math genius!")
        gpa += 20
        print("GPA: +20")
    elif fridayQuizPoints == 75:
        print("Not bad! You got " + str(fridayQuizPoints) + " points on the math test out of 100, but you could have done better.")
        gpa += 10
        print("GPA: +10")
    elif fridayQuizPoints == 50:
        print("You did okay on the math test, you got " + str(fridayQuizPoints) + " points out of 100, but you definitely struggled with some of the questions.")
        gpa += 5
        print("GPA: +5")
    else:
        print("Yikes, you did not do well on the math test. You got " + str(fridayQuizPoints) + " points out of 100. You should probably review your math notes before the next test.")
        gpa -= 10
        print("GPA: -10")





def mathFriday():
    print("Welcome to your last math class!")
    print("True to math form, you have another test today. :(")
    enterContinue()
    mathTestFriday()
    print()
    print("That was a tough test, but you are glad that it's over. Time for your final sociology class!")
    enterContinue()



soclGamePoints = 0

def soclGame():
    global soclGamePoints
    global gpa
    print('''The premise of the game is to match the famous sociologist to their country of origin.''')
    print('''ROUND ONE: ''')
    sociologist1 = "Karl Marx"
    country1 = "Germany"
    print("Sociologist: " + sociologist1)
    guess1 = input("Enter the country of origin: ").lower()
    if guess1 == country1.lower():
        print()
        print("Correct! You guessed the country of origin!")
        print("Sociology points: +10")
        soclGamePoints += 10
    else:
        print()
        print("Oops, that's wrong. The correct answer was: " + country1)
    print()
    print('''ROUND TWO: ''')
    sociologist2 = "Emile Durkheim"
    country2 = "France"
    print("Sociologist: " + sociologist2)
    guess2 = input("Enter the country of origin: ").lower()
    if guess2 == country2.lower():
        print()
        print("Correct! You guessed the country of origin!")
        print("Sociology points: +10")
        soclGamePoints += 10
    else:
        print("Oops, that's wrong. The correct answer was: " + country2)
    print()
    print('''ROUND THREE: ''')
    sociologist3 = "Max Weber"
    country3 = "Germany"
    print("Sociologist: " + sociologist3)
    guess3 = input("Enter the country of origin: ").lower()
    if guess3 == country3.lower():
        print()
        print("Correct! You guessed the country of origin!")
        print("Sociology points: +10")
        soclGamePoints += 10
    else:
        print("Oops, that's wrong. The correct answer was: " + country3)
    
    print()
    print("Total sociology points: " + str(soclGamePoints) + " out of 30 points.")
    if soclGamePoints == 30:
        print("Wow, you got a perfect score on the sociology game! You must be a sociology genius!")
        print("GPA: +20")
        gpa += 20
    elif soclGamePoints >= 20:
        print("Not bad! You got " + str(soclGamePoints) + " points on the sociology game, but you could have done better.")
        print("GPA: +10")
        gpa += 10
    elif soclGamePoints >= 10:
        print("You did okay on the sociology game, you got " + str(soclGamePoints) + " points, but you definitely struggled with some of the questions.")
        print("GPA: +5")
        gpa += 5
    else:
        print("Yikes, you did not do well on the sociology game. You got " + str(soclGamePoints) + " points. You should probably review your sociology notes.")
        print("GPA: -5")
        gpa -= 5


def soclFriday():
    print("Welcome to your last sociology class!")
    print("As you sit down, your teacher announces that class will be short today, and that you will have a fun activity instead of a lecture.")
    enterContinue()
    print("The premise of the game is to match the famous sociologist to their country of origin.")
    soclGame()
    print()


def fridayOlivia():
    day = 'Friday'
    startDayTitleOlivia(day)
    compFriday()
    philFriday()
    mathFriday()
    soclFriday()
    enterContinue()
    journalEntry(day)
    print()
    finalStats()

#FINAL STATS

def completeStats():
    print(''' Here are your final stats for the week! ~~ ''')


    global gpa
    global happiness
    global social
    print()
    print("GRADE: ")
    if gpa >= 95:
        print("Congratulations! You had an amazing week, and you are on track to have a fantastic semester! Your final grade is: A+")
    elif gpa >= 90:
        print("Great job! You had a good week, and you are on track to have a great semester! Your final grade is: A")
    elif gpa >= 85:
        print("Not bad! You had a decent week, and you are on track to have a good semester! Your final grade is: B")
    elif gpa >= 80:
        print("You had a bit of a rough week, and you are on track to have an okay semester. Your final grade is: C")
    elif gpa >= 70:
        print("Yikes, you had a rough week, and you are on track to have a not great semester. Your final grade is: D")
    else:
        print("Oh no, you had a terrible week, and you are on track to have a terrible semester. Your final grade is: F")
    print()
    enterContinue()
    print("HAPPINESS: ")
    if happiness >= 80:
        print("Congratulations! You had a fantastic week, and you are on track to have a great semester! Your happiness level is: " + str(happiness) + " out of 100.")
    elif happiness >= 60:
        print("Great job! You had a good week, and you are on track to have a good semester! Your happiness level is: " + str(happiness) + " out of 100.")
    elif happiness >= 40:
        print("Not bad! You had a decent week, and you are on track to have an okay semester! Your happiness level is: " + str(happiness) + " out of 100.")
    elif happiness >= 20:
        print("You had a bit of a rough week, and you are on track to have a not great semester. Your happiness level is: " + str(happiness) + " out of 100.")
    else:
        print("Oh no, you had a terrible week, and you are on track to have a terrible semester. Your happiness level is: " + str(happiness) + " out of 100.")
    print()
    enterContinue()
    print("SOCIAL: ")
    if social >= 80:
        print("Congratulations! You had a fantastic week, and you are on track to have a great semester! Your social level is: " + str(social) + " out of 100.")
    elif social >= 60:
        print("Great job! You had a good week, and you are on track to have a good semester! Your social level is: " + str(social) + " out of 100.")
    elif social >= 40:
        print("Not bad! You had a decent week, and you are on track to have an okay semester! Your social level is: " + str(social) + " out of 100.")
    elif social >= 20:
        print("You had a bit of a rough week, and you are on track to have a not great semester. Your social level is: " + str(social) + " out of 100.")
    else:
        print("Oh no, you had a terrible week, and you are on track to have a terrible semester. Your social level is: " + str(social) + " out of 100.")
    print()






def oliviasWeek():
    title()
    whatsYourName()
    mondayOlivia()
    tuesdayOlivia()
    wednesdayOlivia()
    thursdayOlivia()
    fridayOlivia()
    completeStats()
    


oliviasWeek()
    


#RILEY'S WEEK
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

#MONDAY BEGINS
def comp170Monday():
    global gpa
    global happiness
    global social

    print("COMP 170 at 9:20 AM - 10:15 AM")
    go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
    while go != "a" and go != "b":
        go = input("Invalid input. Please enter a or b: ").lower()

    if go == "a":
        gpa += 10
        happiness += 10
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


def breakMonday():
    global gpa
    global happiness
    global social

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


def theologyMonday():
    global gpa
    global happiness
    global social

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


def mathMonday():
    global gpa

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


def mondayEvening():
    global gpa
    global happiness
    global social

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


def mondayRiley():
    print("----- Monday -----")
    enter()

    comp170Monday()
    breakMonday()
    theologyMonday()
    mathMonday()
    mondayEvening()

    show_stats()



#TUESDAY BEGINS

def comp163Tuesday():
    global gpa
    global happiness

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

        q1 = input("Q1: What is this function definition missing? def function()  ").lower()
        if q1 == ":" or q1 == "colon":
            print("Correct!")
            quiz_score += 1
        else:
            print("Incorrect. The answer is: :")

        q2 = input("Q2: What does OOP stand for? ").lower()
        if q2 == "object-oriented programming" or q2 == "object oriented programming":
            print("Correct!")
            quiz_score += 1
        else:
            print("Incorrect. The answer is: object-oriented programming")

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


def cjcTuesday():
    global gpa
    global happiness
    global social

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


def chineseCultureTuesday():
    global gpa
    global happiness
    global social

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


def tuesdayEvening():
    global gpa
    global happiness
    global social

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


def tuesdayRiley():
    print("----- Tuesday -----")
    enter()

    comp163Tuesday()
    cjcTuesday()
    chineseCultureTuesday()
    tuesdayEvening()

    show_stats()




#WEDNESDAY BEGINS

# ---------- WEDNESDAY ----------

def comp170SyllabusQuiz():
    global gpa
    global happiness

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
        print("You skip quiz day. That is an automatic zero and Dr. Kelly marks you absent.")
        enter()


def theologyWednesday():
    global gpa
    global happiness
    global social

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
            enter()

    elif go == "b":
        gpa -= 2
        social -= 1
        print("You skip and miss the group activity. Your group had to cover for you.")
        enter()


def mathWednesday():
    global gpa

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


def wednesdayAfternoon():
    global gpa
    global happiness
    global social

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
        print("You run into your floormates at the gym. You feel great afterward.")
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
        enter()
    elif afternoon == "d":
        happiness += 1
        print("A mid-week nap hits different. You feel recharged.")
        enter()


def wednesdayRiley():
    print("----- Wednesday -----")
    enter()

    comp170SyllabusQuiz()
    theologyWednesday()
    mathWednesday()
    wednesdayAfternoon()

    show_stats()


#THURSDAY BEGINS

# ---------- THURSDAY ----------

def thursdayWeather():
    global happiness
    global gpa

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


def comp163Thursday():
    global gpa
    global happiness
    global social

    print("COMP 163 at 10:00 AM - 11:30 AM")

    go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
    while go != "a" and go != "b":
        go = input("Invalid input. Enter a or b: ").lower()

    if go == "a":
        gpa += 2
        happiness += 1

        print("The professor announces a small coding project!")
        enter()

        partner = input("A classmate asks if you want to be partners. Do you (a) say yes enthusiastically, (b) hesitate but say yes, or (c) say you will think about it? ").lower()
        while partner != "a" and partner != "b" and partner != "c":
            partner = input("Invalid input. Enter a, b, or c: ").lower()

        if partner == "a":
            social += 2
            gpa += 1
            print("Your new partner is a great coder. This will really help your grade. Excellent move!")
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


def cjcThursday():
    global gpa
    global happiness
    global social

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


def chineseCultureThursday():
    global gpa
    global happiness
    global social

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
            enter()

    elif go == "b":
        gpa -= 2
        happiness -= 1
        print("You miss the Silk Road documentary. A classmate says it was the best class so far. Devastating.")
        enter()


paperDone = False

def thursdayEvening():
    global gpa
    global happiness
    global social

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
        paperDone = True
        enter()

    elif thursday_eve == "d":
        happiness += 2
        social += 3
        print("A student performs original music that gives you chills.")
        print("You talk to them for twenty minutes afterward. A real connection made.")
        enter()


def thursdayRiley():
    print("----- Thursday -----")
    enter()

    thursdayWeather()
    comp163Thursday()
    cjcThursday()
    chineseCultureThursday()
    thursdayEvening()

    show_stats()


#FRIDAY BEGINS

# ---------- FRIDAY ----------

def comp170Friday():
    global gpa
    global happiness
    global social

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
            enter()

        elif coding == "b":
            gpa -= 1
            print("You copy your neighbor's code and it does not even run because they also have no idea.")
            enter()

        elif coding == "c":
            gpa += 1
            print("Dr. Kelly actually explains it really well. You understand it now.")
            enter()

    elif go == "b":
        gpa -= 2
        social -= 1
        print("You skip the lab. You will have to figure it all out on your own.")
        enter()


def theologyFriday():
    global gpa
    global happiness
    global social
    global paperDone

    print("Theology 11:30 AM - 12:30 PM")
    print("Weekly reflection paper is DUE TODAY.")
    enter()

    if paperDone == True:
        print("Good news - you already wrote it last night. You walk in confident and relaxed.")
        
    else:
        print("You forgot to write the paper. You have to finish it in the hallway before class starts.")
        enter()

    go = input("Do you (a) want to go to class? or (b) skip class? ").lower()
    while go != "a" and go != "b":
        go = input("Invalid input. Enter a or b: ").lower()

    if go == "a":
        gpa += 2
        happiness += 1
        social += 1

        if paperDone == True:
            gpa += 3
            print("You turn in your paper with confidence. Mr. Han seems genuinely pleased.")
        else:
            gpa -= 1
            print("You finish the last paragraph in the hallway and turn it in barely on time.")

        enter()

        discuss = input("Do you (a) share your honest thoughts, (b) agree with whatever others say, or (c) just listen? ").lower()
        while discuss != "a" and discuss != "b" and discuss != "c":
            discuss = input("Invalid input. Enter a, b, or c: ").lower()

        if discuss == "a":
            social += 1
            happiness += 1
            gpa += 1
            print("You say something genuine and the room goes quiet in the best way.")
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
        enter()


def mathFriday():
    global gpa
    global happiness

    print("Math 1:40 PM - 2:30 PM")

    print("Dr. Torres announces a surprise pop quiz!")
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

        q3 = input("Q3: What is the slope of y = 3x + 7? ")
        if q3 == "3":
            print("Correct!")
            math_score += 1
        else:
            print("Incorrect - the slope is 3.")

        print("You scored " + str(math_score) + "/3 on the pop quiz!")

        if math_score == 3:
            gpa += 5
            happiness += 2
            print("Perfect score! You float out of class.")
        elif math_score >= 1:
            gpa += 2
            print("Decent! You held your ground.")
        else:
            gpa -= 3
            print("Rough quiz. Study more next time.")

        enter()

    elif ans == "b":
        gpa -= 3
        print("You walk out. That is a zero you cannot make up.")
        enter()


def fridayCelebration():
    global gpa
    global happiness
    global social

    print("FRIDAY AFTERNOON - YOU SURVIVED THE WEEK!")
    print("How do you celebrate?")
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
        print("You go downtown for deep dish pizza with new friends.")
        enter()

    elif friday_end == "b":
        happiness += 3
        social += 2
        print("The comedy show has everyone laughing nonstop.")
        enter()

    elif friday_end == "c":
        happiness += 2
        gpa += 1
        print("You journal and reflect on your first week of college.")
        enter()

    elif friday_end == "d":
        happiness += 2
        social += 1
        print("You laugh with a high school friend about your chaotic weeks.")
        enter()


def fridayRiley():
    print("----- Friday -----")
    enter()

    print("It's FRIDAY! The finish line is right there.")
    print("Today: COMP 170 lab day, Theology paper, and Math pop quiz.")
    enter()

    comp170Friday()
    theologyFriday()
    mathFriday()
    fridayCelebration()

    show_stats()


# ---------- FINAL CALL ----------
# ---------- END OF WEEK ----------

def endOfWeekStats():
    print("\nEnd of Week Stats:")
    print("GPA:", gpa)
    print("Happiness:", happiness)
    print("Social:", social)
    print()
    enter()


def academicResult():
    global gpa

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


def happinessResult():
    global happiness

    if happiness >= 15:
        print("Happiness result: You are genuinely thriving. College suits you!")
    elif happiness >= 8:
        print("Happiness result: Decent week. Some highlights, some lows.")
    elif happiness >= 0:
        print("Happiness result: You are surviving. Make time for things that recharge you.")
    else:
        print("Happiness result: This week took a toll. Be kind to yourself next week.")


def socialResult():
    global social

    if social >= 12:
        print("Social result: You have built real connections already. Great start!")
    elif social >= 5:
        print("Social result: You made some solid connections. Keep putting yourself out there.")
    elif social >= 0:
        print("Social result: A bit of a lone wolf this week. Try saying yes to more things.")
    else:
        print("Social result: Isolation adds up. Reach out to someone next week.")


def completeStats():
    endOfWeekStats()
    academicResult()
    happinessResult()
    socialResult()





def finalCall():
    print("Welcome to your second week!")
    mondayRiley()
    tuesdayRiley()
    wednesdayRiley()
    thursdayRiley()
    fridayRiley()
    completeStats()

finalCall()










#ALONA VALVERDE
#
# functions for the week to work:

#function advice:
#takes a focus like school and happiness and that focuses stat as paramters
#a for loop determines what the focus is and assigns it a value
# if it is one value, then it cycles through if/elif/else statements to give advice based on where that stat falls
#ex if your gpa is less than 2.6 it tells you you aren't doing well but to keep trying
def keep_track(focus, stat):
    which_focus = ["School", "Happy"]
    for i in range(0, len(which_focus)):
        if focus == which_focus[i]:
            which = i  
    if which == 0:#forSchool(GPA)
        if stat <= 2.6:
            statement = """
        You're not doing too well in school! Keep trying your hardest."""
            print(statement)
    
        elif stat < 3.4:
            statement = """
        Your doing well in school keep it up!"""
            print(statement)
    
        else:
            statement = """
        You might make the dean's list"""
            print(statement)

    if which == 1:#forHappy(happiness, social)
        if stat <= 39:
            statement = """
        Balancing everything can be hard but you got this!"""
            print(statement)
    
        elif stat < 78:
            statement = """
        You're doing amazing!"""
            print(statement)
    
        else:
            statement = """
        Everyone can see how you're glowing, wow!"""
            print(statement)
    
#function check:
#takes all the stats as parameters
#checks if the stat is exceeding the amount it's allowed or if its below that amount
#returns that stat
#this is so that if the player makes a choice that would be over the max or minimum, it would just be at the max/min and keep updating after every choice
#returns each stat
def check(gpa, happiness, social): 
    if gpa > 4.0:
        gpa = 4.0
    elif gpa < 0.0:
        gpa = 0.0

    if happiness > 100:
        happiness = 100
    elif happiness < 0:
        happiness = 0

    if social > 100:
        social = 100
    elif social< 0:
        social = 0
    return gpa, happiness, social
#function user:
#options = true (will keep track of this)
#asks the user to enter y or n for yes or no
#while loop to make sure that user is typing in only y or n
#if not they get asked again
#if/elif conditions to return options as either true or false. true is yes, false is no
#return options
def user_options():
    options = True
    user = input("Enter Y or N: ")

    while user.lower() != "y" and user.lower() != "n":
       user = input("Enter Y or N: ")
       break

    if user.lower() == "y":
        options = True
        
    elif user.lower() == "n":
        options = False
        
    return options
#functions class:
#takes gpa as parameter
#asks the user if they want to go to their next class
# calls function user under a variable to get the yes or no
# if they go to class, gpa goes up
#if not, gpa goes down
#returns gpa
def classes(g):
    print("Do you want to go to your next class?")
    attendance = user_options()
    if attendance ==True:
        g += 0.1
    else:
        g -= 0.2
    return attendance, g

#function stats:
#takes all the stats and prints them out as they are
#lets the user know where they stand in terms of their stats
def show_stats(g, h, so):
    print(f"""
        Stats:
        
        GPA : {g}
        Happiness : {h}
        Social : {so}""")
#function intro:
#cute intro that also prints out the schedule of that day depending on the day
#day is the parameter
# if state that compares the first letter of the day
#if it doesn't start with t it prints the schedule for monday, wednesday, friday
#else it prints the schedule for tuesday thirsday 
def intro(day):
    print('''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                      ꒰ঌ࿔────⊹˖₊˚⊹⋆────⋆˚˖⟡˖˚⋆────⋆⊹˚₊˖⊹────࿔໒꒱
              //ᐢ⑅ᐢ\\   ♡   ₊˚  
            ꒰ ˶• ༝ •˶꒱       ♡‧₊˚                   ♡  Schedule:    ♡‧₊˚    ♡
            ./づ~ :¨·.·¨:     ₊˚                         
  
            ''')
    if day[0] != 't' and day[0] != 'T':
        print( '''
                    9:20-10:10: COMP 170
              
                    11:30-12:20: MATH 118
              
                    12:35-1:25: SOCL 101

                    1:40-2:30: SPAN 101''')
    else:
        print('''   4:15-5:15: COMP 141 ''')
#Basic template for each day
#paramters are all the stats
#each time the user picks something it is assigned its own variable
#each pick comes with some type of change to the stats
#uses the intros
# then the user functions
#if/elif/else conditions to see which route it goes down
#def day(g, h, so):
#        intro(day)
#    pick1 = user_options()
#    if pick1 == True:
#        print()
#        pick2 = user_option()
#        if pick2 == True:
#            print()
#            g, h, so= = check(g, h, so)
#        elif pick2 == False:
#            print()
#            g, h, so = check(g, h, so)          

#        pick3 = user_options()
#        if pick3 == True:
#            print()
#            g, h, so = check(g, h, so)
#          
#        elif pick3 ==False:
#            print()
#            g, h, so = check(g, h, so)
#    elif pick1 == False:
#        print()
#        pick2 = user_option()
#        if pick2 == True:
#            print()
#            g, h, so= = check(g, h, so)
#        elif pick2 == False:
#            print()
#            g, h, so = check(g, h, so)     

#        pick3 = user_options()
#        if pick3 == True:
#            print()
#            g, h, so = check(g, h, so)
#          
#        elif pick3 ==False:
#            print()
#            g, h, so = check(g, h, so)
#    show_stats(g, h, so)
#   return g, h, so


def monday(g, h, so):
    intro('monday')
    print("""
          
            ~~Welcome to your final week!! Make good choices and have fun!!~~

        You wake up late!! There's only 20 minutes until COMP 170 class.
        However, you've been wanting to catch up on sleep and it's only
        one class right??? There's not much time to decide, do you go to
        class or sleep in?
        Type Y or N to go to class.""")
    pick1 = user_options()
    while pick1 == True:
        g += 0.1
        h -= 4
        so = so
        print("""
        COMP 170 9:20 - 10:10
        
        You walk in a little late but good news for you, your professor
        decides to go over the homework in class together!

        COMP 170 Worksheet""")

        work_grade = 0 
        q1 = input("""
        Question 1.
        True or False: int and str are both the same classification.
        a) True
        b) False
        Your answer: """)
        while q1.lower() != "a" and q1.lower() != "b":
            q1 = input("Invalid answer. Must be either a or b :")
            break
        if q1.lower() == "b":
            work_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")

        q2 = input("""
        Question 2.
        True or False: while and for are both types of loops.
        a) True
        b) False
        Your Answer: """)
        while q2.lower() != "a" and q2.lower() != "b":
            q2 = input("Invalid answer. Must be either a or b :")
            break
        if q2.lower() == "a":
            work_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")

        q3 = input("""
        What classification deals with True an False?
        a) bool
        b) int
        c) str
        d) float
        Your Answer:""")
        while q3.lower() != "a" and q3.lower() != "b" and q3.lower != "c" and q3.lower() != "d":
            q3 = input("Invalid answer. Must be either a, b, c, or d :")
            break
        if q3.lower() == "a":
            work_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")
        score = (work_grade/ 3)*100

        print(f"""
        Score : {score}
        
        GPA +0.1
        Happiness -4
        Social +0

        You leave class and head over to the dining hall for some breakfast.
        The dining hall is packed but luckily your friend from math class,
        Jack, saved you a seat. As time gets closer to math class, Jack says
        he's not going since he wants to catch up on other work. He asks if
        you are going to go to class. Attendance isn't even taken but you also
        don't want to skip too much class.

        MATH 118 11:30 - 12:20""")
        a1, g = classes(g) #a for attendance
        if a1 == True:
            print("""
        You head over to class and walk in right on time. Your professor,
        Mr.Hills goes over the weekly schedule and reminds the class of
        the weekly Wednesday math quiz.

        GPA +0.1

        
        SOCL 101 12:35 - 1:25
        Class lets out and you have 15 minutes till your Sociology class.
        Unfortunately your professor, Mr. Smith, told the class about a reading
        quiz. Even though you really want to nap, you walk to class to take the
        quiz.
        
        GPA +0.1""")
            g+= 0.1
        elif a1 == False:
            print("""
        You decide to skip for once and rush to your dorm to take a nap. Next
        class you'll go but what's wrong with needing a nap!

        1 hour later...
        You wake up from your nap and see that you have 15 minutes until your
        next class. Last class Mr. Smith, your professor, warned the class
        about a reading quiz! Despite wanting to sleep more, you walk over
        to your Sociology class.

        GPA +0.1""")
            g +=1
        print("""
        SOCIOLOGY Reading:
        A Theory is a set of statements that seeks to explain problems,
        actions, or behaviors. A Scientific Theory is capable of predicting
        future occurences and can be tested through experiments. You can
        use the Scientific Method to do this as it uses objective systematic
        observations to test these theories. The term Sociology comes from
        Auguste Comte, a scholar/ philosopher from the 19th Century. He
        believed in Positivism, the idea that science can be applied to
        society. This is how we got sociology.""")
        quiz_grade = 0
        sq1 = input("""
        Question 1.
        What century is Auguste Comte from?
        a) 18th
        b) 20th
        c) 19th
        d) 17th
        Your Answer: """)
        while sq1.lower() != "a" and sq1.lower() != "b" and sq1.lower() != "c" and sq1.lower() != "d":
            sq1 = input("Invalid answer. Must be either a, b, c, or d :")
            break
        if sq1 == "c":
            quiz_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")
        sq2 = input("""
        Question 2.
        True or False: The Scientific Method is done through guessing.
        a) True
        b) False
        Your Answer: """)
        while sq2.lower() != "a" and sq2.lower() != "b":
            sq2 = input("Invalid answer. Must be either a, b, c, or d :")
            break
        if sq2 == "b":
            quiz_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")
        
        sq3 = input("""
        Question 3.
        Which of the options can predict the future?
        a) Scientific Theory
        b) Theory
        c) Scientific Method
        Your Answer: """)
        while sq3.lower() != "a" and sq3.lower() != "b" and sq3.lower() != "c":
            sq3 = input("Invalid answer. Must be either a, b, or c:")
            break
        if sq3 == "a":
            quiz_grade += 1
            print("Correct! 1 point")
        else:
            print("Incorrect. 0 points")
        score = (quiz_grade / 3)*100
        print(f"""
        Score: {score}

        Mr. Smith lets out class early! You have 25 minutes before your
        next class, Spanish 101.

        SPAN 101 1:40 - 2:30""")
        a2, g = classes(g)
        if a2 == True:
            print("""
        You walk into class and see some people there already. Should you
        go over and talk to them?""")
            talk = user_options()
            if talk == True:
                so +=6
                print("""
        You sit down and introduce yourself. It's two girls and two guys.
        They introduce themselves so you meet Marcus, Jayden, Angelina,
        and Cailynn.

        The rest of class you guys all talk together and make plans to visit
        the zoo at some point in the semester.

        Social +6""")
            else:
                so +=2
                print("""
        You sit by yourself and keep your head down the rest of class.
        Your spanish professor, Ms. Lull, says to get into groups of 5
        to do a worksheet together. One of the people in the group from
        before go up to you and ask if you want to join their group.
        Eventually, you sit down with them to do work. Thet introduce
        themselves as Marcus, Jayden, Angelina, and Cailynn. The rest of
        class you guys spend making jokes and talking.

        Social +2""")
        
        
        print("""
        After class your friends, Melita and Olu, ask if you want to go
        to the dining hall but you were thinking about taking a nap. What
        should you do,go to the dining hall or nap?
        Type Y or N to go to the dining hall.""")
        g, h, so = check(g, h, so)
        pick2 = user_options()
        if pick2 == True:
            h +=5
            so += 13
            print("""
        You end up making two new friends, Juli and Sultan, and one of
        them is also a Cybersecurity major!
        Social +2

        Overall ->
        GPA +0.0
        Happiness +5
        Social +13""")
            g, h, so = check(g, h, so)
            break
        elif pick2 == False:
            h +=2
            so -= 8
            print("""
        Your friends text you later saying they made two new friends
        and how cool they are. They tell you all the fun things they
        did and how you should've been there. Now your FOMO is hitting!
        Social -3

        Overall ->
        GPA +0.0
        Happiness +2
        Social -8""")
            g, h, so = check(g, h, so)
            break
        break
    while pick1 == False:
        g -=0.3
        h +=4
        print("""
        You wake up at 10:30 and have enough time to get dressed and
        get breakfast.

        GPA -0.3
        Happiness +4
        Social +0
        
        The dining hall is packed but luckily your friend from math class,
        Jack, saved you a seat. As time gets closer to math class, Jack says
        he's not going since he wants to catch up on other work. He asks if
        you are going to go to class. Attendance isn't even taken but you also
        don't want to skip too much class.

        MATH 118 11:30 - 12:20""")
        a1, g = classes(g) #a for attendance
        if a1 == True:
            print("""
        You head over to class and walk in right on time. Your professor,
        Mr.Hills goes over the weekly schedule and reminds the class of
        the weekly Wednesday math quiz.

        GPA +0.1
        
        SOCL 101 12:35 - 1:25
        Class lets out and you have 15 minutes till your Sociology class.
        Unfortunately your professor, Mr. Smith, told the class about a reading
        quiz. Even though you really want to nap, you walk to class to take the
        quiz.
        
        GPA +0.1""")
            g+= 0.1
        elif a1 == False:
            print("""
        You decide to skip to meet up with your friend Lezley. She comes to your
        dorm and she catches you up on all her girl drama.

        1 hour later...
        You realize you have your sociology class in 10 minutes. You want to keep
        talking with Lezley, but Mr. Smith, your sociology professor, reminded
        the class about a reading quiz last class. Luckily Lezley also has a class
        in the same building, so you guys continue talking on the way.

        GPA +0.1""")
            g +=1
            
        print("""
        SOCIOLOGY Reading:
        A Theory is a set of statements that seeks to explain problems,
        actions, or behaviors. A Scientific Theory is capable of predicting
        future occurences and can be tested through experiments. You can
        use the Scientific Method to do this as it uses objective systematic
        observations to test these theories. The term Sociology comes from
        Auguste Comte, a scholar/ philosopher from the 19th Century. He
        believed in Positivism, the idea that science can be applied to
        society. This is how we got sociology.""")
        quiz_grade = 0
        sq1 = input("""
        Question 1.
        What century is Auguste Comte from?
        a) 18th
        b) 20th
        c) 19th
        d) 17th
        Your Answer: """)
        while sq1.lower() != "a" and sq1.lower() != "b" and sq1.lower() != "c" and sq1.lower() != "d":
            sq1 = input("""
        Invalid answer. Must be either a, b, c, or d :""")
            break
        if sq1 == "c":
            quiz_grade += 1
            print("""
        Correct! 1 point""")
        else:
            print("""
        Incorrect. 0 points""")
        sq2 = input("""
        Question 2.
        True or False: The Scientific Method is done through guessing.
        a) True
        b) False
        Your Answer: """)
        while sq2.lower() != "a" and sq2.lower() != "b":
            sq2 = input("""
        Invalid answer. Must be either a, b, c, or d : """)
            break
        if sq2 == "b":
            quiz_grade += 1
            print("""
        Correct! 1 point""")
        else:
            print("""
        Incorrect. 0 points""")
        
        sq3 = input("""
        Question 3.
        Which of the options can predict the future?
        a) Scientific Theory
        b) Theory
        c) Scientific Method
        Your Answer: """)
        while sq3.lower() != "a" and sq3.lower() != "b" and sq3.lower() != "c":
            sq3 = input("""
        Invalid answer. Must be either a, b, or c: """)
            break
        if sq3 == "a":
            quiz_grade += 1
            print("""
        Correct! 1 point""")
        else:
            print("""
        Incorrect. 0 points""")
        score = (quiz_grade / 3)*100
        print(f"""
        Score: {score}

        Mr. Smith lets out class early! You have 25 minutes before your
        next class, Spanish 101.

        SPAN 101 1:40 - 2:30""")
        a2, g = classes(g)
        if a2 == True:
            print("""
        You walk into class and see some people there already. Should you
        go over and talk to them?""")
            talk = user_options()
            if talk == True:
                so +=6
                print("""
        You sit down and introduce yourself. It's two girls and two guys.
        They introduce themselves so you meet Marcus, Jayden, Angelina,
        and Cailynn.

        The rest of class you guys all talk together and make plans to visit
        the zoo at some point in the semester.

        Social +6""")
            else:
                so +=2
                print("""
        You sit by yourself and keep your head down the rest of class.
        Your spanish professor, Ms. Lull, says to get into groups of 5
        to do a worksheet together. One of the people in the group from
        before go up to you and ask if you want to join their group.
        Eventually, you sit down with them to do work. Thet introduce
        themselves as Marcus, Jayden, Angelina, and Cailynn. The rest of
        class you guys spend making jokes and talking.

        Social +2""")
        elif a2 == False:
            print("""
        You decide to accompany your friends Melita and Olu to the library
        downtown. They do a project for their shared philosophy class while
        you catch up on the work you missed from COMP 170.

        COMP 170 WORK:""")
            work_grade = 0 
            q1 = input("""
        Question 1.
        True or False: int and str are both the same classification.
        a) True
        b) False
        Your answer: """)
            while q1.lower() != "a" and q1.lower() != "b":
                q1 = input("""
        Invalid answer. Must be either a or b : """)
                break
            if q1 == "b":
                work_grade += 1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")

            q2 = input("""
        Question 2.
        True or False: while and for are both types of loops.
        a) True
        b) False
        Your Answer: """)
            while q2.lower() != "a" and q2.lower() != "b":
                q2 = input("""
        Invalid answer. Must be either a or b : """)
                break
            if q2 == "a":
                work_grade += 1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")

            q3 = input("""
         What classification deals with True an False?
        a) bool
        b) int
        c) str
        d) float
        Your Answer:""")
            while q3.lower() != "a" and q3.lower() != "b" and q3.lower != "c" and q3.lower() != "d":
                q3 = input("""
        Invalid answer. Must be either a, b, c, or d :""")
                break
            if q3 == "a":
                work_grade += 1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")
            score = (work_grade/ 3)*100
            print(f"""
        Score: {score}

        After they finish their project, you all head over to back to campus.

        40 minutes later...""")

        print("""You realize that you need to go to Target to restock on soap
        and moisturizer. However at the same time your friends ask if
        you want to go to Cane's with them after they finish class.
        You don't want to use the money in your card since you want to
        use it on the weekend and you only have enough cash to do one
        or the other. Restock or get food?
        Type Y or N to go restock on items.""")
        g, h, so = check(g, h, so)
        pick2 = user_options()
        if pick2 == True:
            h -= 6
            so -= 8
            print("""

        Your friends were nice enough to bring you some food as a treat!
        Now you get to have a treat and have everything you need.

        GPA +0.0
        Happiness -6
        Social -8""")
            g, h, so = check(g, h, so)
            break
        elif pick2 == False:
            h +=2
            so +=4
            print("""
        You have fun with your friends and go back to the dorm. Later
        on you go to take a shower and forget you have no soap!
        You ask your clase friend to borrow their body wash. They give
        it to you but they make a joke about how you don't shower
        which spreads through your groupchat.

        GPA +0
        Happiness +2
        Social +4""")
            g, h, so = check(g, h, so)
            break
        break
    show_stats(g, h, so)
    return g, h, so

def tuesday(g, h, so):
    intro("Tuesday")
    print("""
        You wake and relax since you have a lot of time before your 4:15 class.
        It's been a bit since you've gone to the gym and summer's coming up.
        However you have homework to do for SPAN 101 due tomorrow. You check the
        assignment and see that it isn't hard, but it is long. Should you go to the
        gym or do your homework?
        Type Y or N to go to the gym.""")
    pick1 = user_options()
    while pick1 ==True:
        g -= 0.1
        h += 10
        so +=7
        print("""
        You end up seeing some people you haven't seen in a while and catch
        up for a bit. Now you feel refreshed and happy to see people.
        Social +2

        Overall ->
        GPA -0.1
        Happiness +10
        Social +7

        After a nice shower, you have 3 hours before class. It's time to
        have lunch with Amaiya, the girl from your environmental class
        last semeter. She asks if you want to watch the new Terri Joe
        Tubi movie that just came out after eating. This would mean not
        going to class at all today.

        Type Y or N to watch the movie.""")
        g, h, so = check(g, h, so)
        pick2 = user_options()
        if pick2 == True:
            g -= 0.2
            h += 10
            so += 4
            print("""
        GPA - 0.2
        Happiness +10
        Social +4

        After the movie you and Amaiya relax and do some work. The only
        work you can remember to do is Spanish

        SPANISH WORK: """)
            work_grade = 0
            sq1 = input("""
        Pregunta 1.
        Cómo saludas en español?
        **How do you say hi in spanish**
        a) hola
        b) hala
        c)adios
        Your answer: """)
            while sq1.lower() != 'a' and sq1.lower() != 'b' and sq1.lower() != 'c':
                sq1 = input("""
        Invalid input, Must be a, b, or c: """)
                break
            if sq1.lower() == 'a':
                work_grade +=1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")
            sq2 = input("""
        Pregunta 2.
        Cómo preguntar '¿cómo te llamas?
        **How do you ask 'what's your name'?**
        Type your answer: """)
            for tries in range(3):
                if sq2.lower() == "como te llamas?" and sq2.lower() == "como te llamas":
                    print("""
        Correct. 1 point""")
                    work_grade += 1
                else:
                    if 2-tries != 0:
                        print(f"""
        Incorrect. You have {2-tries} more tries.""")
                        sq2 = input("""
        Enter you answer: """)
            else:
                print("""
        Correct answer: Como te llamas
        0 points""")
            sq3 = input("""
        Pregunta 3.
        Cómo se dice "good morning"?
        a) buenas tardes
        b) buenos dias
        c) bueanas noches
        Your answer: """)
            while sq3.lower() != 'a' and sq3.lower() != 'b' and sq3.lower() != 'c':
                sq3 = input("""
        Invalid input, Must be a, b, or c: """)
                break
            if sq3.lower() == 'b':
                work_grade +=1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")
            score = (work_grade /3)*100
            print(f"""
        Score: {score}
        
        GPA +0.2
        Happiness +2
        Social -6""")
            g += 0.2
            h += 2
            so -=6
            g, h, so = check(g, h, so)
            keep_track("School", g)
            break
        elif pick2 == False:
            print("""
        COMP 141 4:15 - 5:15
        
        You walk into class and sit next to your friend, Matteo. As you're both talking
        the professor for the class, Mr. Nax, emails the class that his car broke down
        and class is canceled for today. Oh no for Mr. Nax but yay for you! You and Matteo
        instead head the Student Center to play pool with his friend group.

        Before you play, Jayden from Spanish texts you.
        Jayden: The work isn't hard but i wish i was fluent already
        Jayden: did you do it yet??

        You: you just reminded me actually :/
        You: i was gonna play pool </3

        Jayden: lowkey do it first its due tomorrow before class
        Jayden:ms lull forgot to tell us about it

        You: gotcha


        You tell Matteo that you have an assignment to do before you can play, so you'll sit
        the first game out. After finding a table you pull out your computer to get started.

        SPANISH WORK:""")
            work_grade = 0
            sq1 = input("""
        Pregunta 1.
        Cómo saludas en español?
        **How do you say hi in spanish**
        a) hola
        b) hala
        c)adios
        Your answer: """)
            while sq1.lower() != 'a' and sq1.lower() != 'b' and sq1.lower() != 'c':
                sq1 = input("Invalid input, Must be a, b, or c: ")
                break
            if sq1.lower() == 'a':
                work_grade +=1
                print("Correct! 1 point")
            else:
                print("Incorrect. 0 points")
            sq2 = input("""
        Pregunta 2.
        Cómo preguntar 'what's your name'?
        Type your answer: """)
            for tries in range(3):
                if sq2.lower() == "como te llamas?" and sq2.lower() == "como te llamas":
                    print("""
        Correct. 1 point""")
                    work_grade += 1
                else:
                    if 2-tries != 0:
                        print(f"""
        Incorrect. You have {2-tries} more tries.""")
                        sq2 = input("""
        Enter you answer: """)
            else:
                print("""
        Correct answer: Como te llamas
        0 points""")
            sq3 = input("""
        Pregunta 3.
        Cómo se dice "good morning"?
        a) buenas tardes
        b) buenos dias
        c) bueanas noches
        Your answer: """)
            while sq3.lower() != 'a' and sq3.lower() != 'b' and sq3.lower() != 'c':
                sq3 = input("""
        Invalid input, Must be a, b, or c: """)
                break
            if sq3.lower() == 'b':
                work_grade +=1
                print("""
        Correct! 1 point""")
            else:
                print("""
        Incorrect. 0 points""")
            score = (work_grade /3)*100
            print(f"""
        Score: {score}

        Overall ->
        GPA +0.3
        Happiness +12
        Social +15

        You go to Matteo and his friends while they play. You tell them
        that you've never played before and want to learn but are scared
        of looking dumb. Matteo's friend Maddy offers to teach you so you
        could play a couple of rounds. Should you take her offer and play?
        Type Y or N to play pool.""")
            g +=0.3
            h+=12
            so+=15
            pick3 = user_options()
            if pick3 == True:
                print("""
        Maddy teaches you how to play and you're actually not bad for a
        first timer, except when you hit it so hard that the ball went flying
        and almost hit a girl. She wasn't too happy about that... Let's just
        say you needed to bribe her snacks for her to not call Campus Safety.

        You join everyone else to play and they all roast you for not making
        getting the balls. With Maddy on your team, she gets most of the balls
        in so now it's just up to the black ball... and it's your turn!
        Everyone holds their breath and by some miracle(or Maddys praying)
        you make it in and won. The whole group freaks out and says you should
        hang out with them more. More friends !!

        GPA +0.0
        Happiness +15
        Social +15""")
                g = g
                h+=15
                so+=15
            elif pick3 == False:
                print("""
        You decline and just watch them play. Although you aren't playing,
        you become the DJ for music and they love your music! After talking
        about music, art, and shows they invite you to hang out with them again
        as long as you promise to learn how to play. This time you agree since
        it can't be that bad!

        GPA +0.0
        Happiness +5
        Social +10""")
                g =g
                h+=5
                so+=10
            g, h, so = check(g, h, so)
            keep_track("Happy", h)
            break
        
        print("""
        It's getting a little late so you decide to grab some late
        night food with your friend Juli. She tells you about a club event
        on Friday and tells you once she has more info she'll text you about it.""")
        g, h, so = check(g, h, so)
        break
    while pick1 == False:
        g += 0.4
        h -= 2
        so += 2
        print("""
        As you are walking to the IC a squirrel chases you!
        Just your luck, someone takes a video and posts it on Fizz.
        It goes viral and becomes a TikTok trend! Now everyone on
        campus wants to talk to you.

        Social +2
        Embarrasment +10000000
        
        Overall ->
        GPA +0.4
        Happiness -2
        Social +2

        You get to the IC and check what work you have to do. You see
        that all you have for today is Spanish work.

        SPANISH WORK:""")
        work_grade = 0
        sq1 = input("""
        Pregunta 1.
        Cómo saludas en español?
        **How do you say hi in spanish**
        a) hola
        b) hala
        c)adios
        Your answer: """)
        while sq1.lower() != 'a' and sq1.lower() != 'b' and sq1.lower() != 'c':
            sq1 = input("""
        Invalid input, Must be a, b, or c: """)
            break
        if sq1.lower() == 'a':
            work_grade +=1
            print("""
        Correct! 1 point""")
        else:
            print("""
        Incorrect. 0 points""")
        sq2 = input("""
        Pregunta 2.
        Cómo preguntar 'what's your name'?
        Type your answer: """)
        for tries in range(3):
            if sq2.lower() == "como te llamas?" and sq2.lower() == "como te llamas":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                    print(f"""
        Incorrect. You have {2-tries} more tries.""")
                    sq2 = input("""
        Enter you answer: """)
        else:
                print("""
        Correct answer: Como te llamas
        0 points""")
        sq3 = input("""
        Pregunta 3.
        Cómo se dice "good morning"?
        a) buenas tardes
        b) buenos dias
        c) bueanas noches
        Your answer: """)
        while sq3.lower() != 'a' and sq3.lower() != 'b' and sq3.lower() != 'c':
            sq3 = input("""
        Invalid input, Must be a, b, or c: """)
            break
        if sq3.lower() == 'b':
            work_grade +=1
            print("""
        Correct! 1 point""")
        else:
            print("""
        Incorrect. 0 points""")
        score = (work_grade /3)*100
        print(f"""
        Score: {score}
        
        Yay you got your work done! Sultan, your friend, finds you in the IC
        and invites you to a club event. At the event you meet Sultans
        friends. One of them cuts hair for their friends and offers to cut
        yours after you complained about the length.Should you get a haircut?
        Type Y or N to get a haircut.""")
        g, h, so = check(g, h, so)
        pick2 = user_options()
        if pick2 == True:
            h += 6
            so += 7
            print("""
        The haircut came out amazing and everyone who sees you compliments
        your hair! On top of that, Sultans friends now like you.
        
        GPA +0.0
        Happiness +6
        Social +7""")
            g, h, so = check(g, h, so)
        elif pick2 == False:
            g = g
            h -= 8
            so -= 3
            print("""
        After leaving the event a random person spits their gum out in
        your direction. Now you have gum stuck in your hair and have to cut
        it by yourself. The haircut comes out choppy, so it looks like you'll
        be wearing a hat for a couple of months.
        
        GPA +0.0
        Happiness -8
        Social -3""")
            g, h, so = check(g, h, so)
        break
    print("""
        Your friends want to stay up and get work done. Do you want to do stay up
        or go to bed?
        Type Y or N""")
    pick5 = user_options()
    if pick5 == True:
        g +=0.1
        h +=6
        so +=1
        print("""
        You decide to catch up on some shows instead of doing work. You only
        get 4 hours of sleep but you and your friends had a good time making
        jokes and going on a late night 7-11 run, where you end up meeting
        Justin Bieber?!

        GPA +0.1
        Happiness +6
        Social +1 """)
        g, h, so = check(g, h, so)
    elif pick5 == False:
        g = g
        h += 12
        so = so
        print("""
        You do some work with your friends but go to sleep at a decent time.
        In the groupchat, your friends are sending videos about how they saw
        Justin Bieber in 7-11!

        GPA +0.0
        Happiness +12
        Social +0""")
        g, h, so = check(g, h, so)
    show_stats(g, h, so)
    return g, h, so

def wednesday(g, h, so):
    intro("Wednesday")
    print("""
        You wake up at 8 am, just in time to get ready for COMP 170. Do you end up
        going to class?
        Type Y or N to go to class?""")
    pick = user_options()
    if pick == True:
        g+=0.1
        print("""
        You take your time getting ready and walk over to class.

        COMP 170 9:20 - 10:10
        Ms. Woods, the professor, spends class time going over the lecture. At the last
        15 minutes of class, she tells everyone to do the lab and to ask her any questions.

        COMP 170 LAB:""")
        work_grade = 0
        cq1 = input("""
        Question 1.
        If you want to make a program that asks the user a question and takes that answer
        what would have to go in the beginning of the question.
        (Before the '()')
        Type your answer: """)
        for tries in range(3):
            if cq1.lower() == "input":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                        print(f"""
        Incorrect. You have {2-tries} more tries.""")
                cq1 = input("""
        Enter you answer: """)
        else:
                print("""
        Correct answer: input
        0 points""")

        cq2 = input("""
        Question 2.
        Write a for loop with the range going up to 5. Use i as a variable.
        Type your answer: """)
        for tries in range(3):
            if cq2.lower() == "for i in range(6)" and cq2.lower() == "for i in range (0, 6)":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                    print(f"""
        Incorrect. You have {2-tries} more tries.""")
                    cq2 = input("""
        Enter you answer: """)
        else:
            print("""
        Correct answer: 'for i in range(6)' or 'for i in range(0, 6)'
        0 points""")

        cq3 = input("""
        Question 3.
        Follow the program:
        x = 3
        y = 3
        z = 6
        w = (((x*y)*x)+(z-y))/z
        Type your answer: """)
        for tries in range(3):
            if cq3 == "5" and cq3 == "5.0":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                    print(f"""
        Incorrect. You have {2-tries} more tries.""")
                    cq3 = input("""
        Enter you answer: """)
        else:
            print("""
        Correct answer: 5 or 5.0
        0 points""")
        score = (work_grade /3)*100
        print(f"""
        Score: {score}

        GPA +0.3""")
    elif pick == False:
        print("""
        Class can wait right?

        You head over to Juli's dorm after getting dressed and help her with her hair.
        She's busy telling you about her boy drama while you dye her hair black. As she
        washes out the dye you complete your COMP 170 work to not fall behind.

        COMP 170 WORK:""")
        work_grade = 0
        cq1 = input("""
        Question 1.
        If you want to make a program that asks the user a question and takes that answer
        what would have to go in the beginning of the question.
        (Before the '()')
        Type your answer: """)
        for tries in range(3):
            if cq1.lower() == "input":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                        print(f"""
        Incorrect. You have {2-tries} more tries.""")
                cq1 = input("""
        Enter you answer: """)
        else:
                print("""
        Correct answer: input
        0 points""")
        
        cq2 = input("""
        Question 2.
        Write a for loop with the range going up to 5. Use i as a variable.
        Type your answer: """)
        for tries in range(3):
            if cq2.lower() == "for i in range(6)" and cq2.lower() == "for i in range (0, 6)":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                    print(f"""
        Incorrect. You have {2-tries} more tries.""")
                    cq2 = input("""
        Enter you answer: """)
        else:
            print("""
        Correct answer: 'for i in range(6)' or 'for i in range(0, 6)'
        0 points""")

        cq3 = input("""
        Question 3.
        Follow the program:
        x = 3
        y = 3
        z = 6
        w = (((x*y)*x)+(z-y))/z
        Type your answer: """)
        for tries in range(3):
            if cq3 == "5" and cq3 == "5.0":
                print("""
        Correct. 1 point""")
                work_grade += 1
            else:
                if 2-tries != 0:
                    print(f"""
        Incorrect. You have {2-tries} more tries.""")
                    cq3 = input("""
        Enter you answer: """)
        else:
            print("""
        Correct answer: 5 or 5.0
        0 points""")
        score = (work_grade /3)*100
        print(f"""
        Score: {score}

        She comes back with her hair dyed perfectly. After drying it she takes a picture
        and posts on Fizz to go to you if someone wants their hair done with your Insta
        username at the bottom. You gain 20 new followers and everyone in the comments
        gas you up!

        Happiness +10
        Social +20""")
        h +=10
        so +=20
        g, h, so = check(g, h, so)

    print("""
        You head to the dining hall after class for some breakfast.
        While in the dining hall you see two of your friends, Alex and Haley. Alex is
        the type of friend you can unwind with more than do anything academic (or
        productive) while Haley is the type of friend that you hear about academic
        opportunities from and she focuses on her work more than social life. Who do
        you sit with, Alex or Haley?
        Type Y or N to sit with Alex.""")
    pick1 = user_options()
    
    while pick1 == True:
        print("""
        You and Alex talk about all the things you guys have been up to lately. He tells
        you about a party happening on Friday. According to him it "will be so lit and
        everyone is going". He asks if you would be interested in going. You tell him
        you're not sure yet. Didn't someone else ask you about doing something Friday?
        He says he will text you on Friday about it""")
        print("""
        After breakfast, you head over to your meeting with your advisor. Thankfully you
        had told your math professor about this ahead of time so you are excused!

        At the meeting she tells you about a couple of clubs that accepting new members.
        The clubs are holding a joint event sometime after your last class. Do you go to
        the event and become a member of the clubs?
        Type Y or N to go to the event.""")
        pick3 = user_options()
        if pick3 == True:
            g += 0.1
            h += 8
            so += 17
            print("""
        The event was very engaging and had food! You meet others with the same major
        and have a good time seeing what the clubs have to offer. The president of one of them
        recomended you for a position in the club next semester. Overall, you had a great
        time!

        GPA +0.1
        Happiness +8
        Social +17

        Afterwards, Mr. Hill emails you that he forgot to include the take home math quiz
        in his last email. He tells you it shouldn't take a while and good luck!

        MATH QUIZ:""")
            quiz_grade = 0
            mq1 = input("""
        Question 1.
        A right triangle has a side length of 10 ft and another side length of 5 ft.
        What is the hypotenuse in ft?
        a)11.18 ft
        b)11.19
        c)11.28
        Your Answer: """)
            while mq1.lower() != "a" and mq1.lower() != "b" and mq1.lower() != "c":
                mq1 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq1.lower() == "a":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq2 = input("""
        Question 1.
        If two sides of the triangle are equal, which triangle is it?
        a)right
        b)equilateral 
        c)isosceles
        Your Answer: """)
            while mq2.lower() != "a" and mq2.lower() != "b" and mq2.lower() != "c":
                mq2 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq2.lower() == "b":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq3 = input("""
        Question 3.
        True or False: a^2 is the same as square rooting a.
        a)True
        b)False
        Your Answer: """)
            while mq3.lower() != "a" and mq3.lower() != "b":
                mq3 = input("""
        Invalid answer. Must be a or b: """)
            if mq3.lower() == "b":
                quiz_grade+=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            score = (quiz_grade/3)*100
            print(f"""
        Score: [score]""")
            g, h, so = check(g, h, so)
            break
        elif pick3 ==False:
            g -= 0.3
            h += 6
            so -= 14
            print("""
        You tell her you'll think about it. After the meeting you end up going to
        your dorm to nap. The whole day goes by before you know it and now you have to
        rush doing your take home math quiz </3.

        GPA -0.3
        Happiness +6
        Social -14

        MATH QUIZ: """)
            quiz_grade = 0
            mq1 = input("""
        Question 1.
        A right triangle has a side length of 10 ft and another side length of 5 ft.
        What is the hypotenuse in ft?
        a)11.18 ft
        b)11.19
        c)11.28
        Your Answer: """)
            while mq1.lower() != "a" and mq1.lower() != "b" and mq1.lower() != "c":
                mq1 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq1.lower() == "a":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq2 = input("""
        Question 1.
        If two sides of th
        e triangle are equal, which triangle is it?
        a)right
        b)equilateral 
        c)isosceles
        Your Answer: """)
            while mq2.lower() != "a" and mq2.lower() != "b" and mq2.lower() != "c":
                mq2 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq2.lower() == "b":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq3 = input("""
        Question 3.
        True or False: a^2 is the same as square rooting a.
        a)True
        b)False
        Your Answer: """)
            while mq3.lower() != "a" and mq3.lower() != "b":
                mq3 = input("""
        Invalid answer. Must be a or b: """)
            if mq3.lower() == "b":
                quiz_grade+=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            score = (quiz_grade/3)*100
            print(f"""
        Score: [score]""")
            g, h, so = check(g, h, so)
            break
        break
    while pick1 == False:
        print("""
        You decide to with Haley and catch up. Yall talk about your classes, and how
        things are going. Haley tells you about a Job Fest going on and how
        she's going. She invites you to come with her. The only problem is that the Event
        during your classes as it has presenters and a luch with recruiters. If you go,
        you can get more connections and explore different jobs and internships. However,
        midterm exams are coming up soon so missing might come back to bite you unless
        you start studying this week. Do you go?
        Type Y or N to go to the Job Fest""")
        pick2 = user_options()
        if pick2 == True:
            g +=0.2
            h +=7
            so +=9
            print("""
        You and Haley head over to the Job Fest. There, you meet April, a recruiter from Google
        and shares an app where recruiters discuss what they are looking for in candidates. It is
        still new, so not too many unemployed people are using it but recruiters from the biggest
        companies and corporations began joining it. April gives you her work email so that she can
        tell you if anything big is going on in the Tech field, but also in case you ever want to
        ask her questions. What a great connection!

        GPA +0.2
        Happiness +7
        Social +9

        After the event, you and Hayley head over to the dining hall to debrief about everything.
        While at the dining hall you get a reminder email from MATH 118.

        OH NO!! There was a take home math quiz you forgot about!

        You quickly take out your laptop and begin the quiz.

        MATH QUIZ:""")
            quiz_grade = 0
            mq1 = input("""
        Question 1.
        A right triangle has a side length of 10 ft and another side length of 5 ft.
        What is the hypotenuse in ft?
        a)11.18 ft
        b)11.19
        c)11.28
        Your Answer: """)
            while mq1.lower() != "a" and mq1.lower() != "b" and mq1.lower() != "c":
                mq1 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq1.lower() == "a":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq2 = input("""
        Question 1.
        If two sides of th
        e triangle are equal, which triangle is it?
        a)right
        b)equilateral 
        c)isosceles
        Your Answer: """)
            while mq2.lower() != "a" and mq2.lower() != "b" and mq2.lower() != "c":
                mq2 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq2.lower() == "b":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq3 = input("""
        Question 3.
        True or False: a^2 is the same as square rooting a.
        a)True
        b)False
        Your Answer: """)
            while mq3.lower() != "a" and mq3.lower() != "b":
                mq3 = input("""
        Invalid answer. Must be a or b: """)
            if mq3.lower() == "b":
                quiz_grade+=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            score = (quiz_grade/3)*100
            print(f"""
        Score: [score]

        Phew! At least now it is done. You apologize to Hayley for interupting the meal
        by doing the quiz. She laughs it off and you guys head over to your dorm to
        relax and continue hanging out.""")
            g, h, so = check(g, h, so)
            break
        elif pick2 == False:
            print("""
        MATH 118 11:30 - 12:20
        You walk to MATH 118 and sit down. Mr. Hill pulls out the weekly Wednesday quiz.
        It shouldn't be too bad right?

        MATH QUIZ:""")
            quiz_grade = 0
            mq1 = input("""
        Question 1.
        A right triangle has a side length of 10 ft and another side length of 5 ft.
        What is the hypotenuse in ft?
        a)11.18 ft
        b)11.19
        c)11.28
        Your Answer: """)
            while mq1.lower() != "a" and mq1.lower() != "b" and mq1.lower() != "c":
                mq1 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq1.lower() == "a":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq2 = input("""
        Question 1.
        If two sides of th
        e triangle are equal, which triangle is it?
        a)right
        b)equilateral 
        c)isosceles
        Your Answer: """)
            while mq2.lower() != "a" and mq2.lower() != "b" and mq2.lower() != "c":
                mq2 = input("""
        Invalid answer. Must be a, b, or c: """)
            if mq2.lower() == "b":
                quiz_grade +=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            mq3 = input("""
        Question 3.
        True or False: a^2 is the same as square rooting a.
        a)True
        b)False
        Your Answer: """)
            while mq3.lower() != "a" and mq3.lower() != "b":
                mq3 = input("""
        Invalid answer. Must be a or b: """)
            if mq3.lower() == "b":
                quiz_grade+=1
                print("""
        Correct answer! 1 point""")
            else:
                print("""
        Incorrect answer. 0 points""")
            score = (quiz_grade/3)*100
            print(f"""
        Score: [score]

        Phew! At least it wasn't too long. The rest of class is going over the material done on Monday.


        As class ends you end up getting an email that the Crown Center is flooded from pumbling! Classes move to
        Zoom instead of in person for today. This means a mid day nap!""")
            g, h, so = check(g, h, so)
            break
        break


    print("""
        Since it is Wednesday, it's Wing Night! Your friends invite you to Wing Night with the full
        friend group. It sounds tempting but you were also thinking about doing a late night gym session.
        Unlike the other times you go, there's no one at night and it's a little self-care alone time just
        for you. Do you go to Wing Night or the gym?
        Type Y or N to go to WIng Night.""")
    pick3 = user_options()
    if pick3 == True:
        h += 5
        so+=1
        print("""
        You meet up with everyone and enjoy some good wings in the dining hall. You guys end up staying until
        they close and hit up 7-11 on the way back for some snacks for an impulsive movie night.

        Instead of going to bed at 12 like you said you would, you return to your room at 3 AM and promptly
        pass out

        Happiness +5
        Social +1""")
        g, h, so = check(g, h, so)
    elif pick3 == False:
        h += 13
        so -=3
        print("""
        You decline and instead head over to the gym.

        Happiness +10
        Social -3
        
        OH NO! As you are doing your core work out a weight falls on your face. As your nose starts
        bleeding you call your friend Sultan since he also declined to work out. He comes and helps
        you with all the blood. Of course he also gets some photos as evidence.

        As you both head out the gym you see Matteo and his friends. They tell you that it's a good thing
        you didn't go to Wing Night, some people got food poisoning! Your nose might still hurt but at least
        it isn't your stomach.

        Happiness +3

        After returning to the dorm and showering, Melita, Olu, and Juli barge into your room for a movie night
        Instead of letting you sleep, they force you into Sultans room to watch another terrible Tubi movie.

        You end up falling asleep in Sultans room and you all have a sleep over.

        Social +5""")
        so +=5
        g, h, so = check(g, h, so)
    show_stats(g, h, so)
    return g, h, so

def thursday(g, h, so):
    intro("Thursaday")
    print("""
        You wake up at 10 and get breakfast with Matteo. Since you both are in COMP 141, you guys do your
        homework together.

        COMP WORK:

        To access the terminal we will be using Ubuntu. The first directory available to you is the
        Home directory. To change directories, you write "cd [filename]". To check if you are in that
        direcotry, use "pwd" to see what directory you are in. Use "touch >" or "cat > " followed
        by a name to create a file and add content to that file. To write in the files use "vim"
        followed by the file name.""")
    
    work_grade = 0
    q1 = input("""
        Question 1.
        True or False. You can use 'touch >>' to create a file.
        a) True
        b) False
        Your Answer: """)
    while q1.lower() != "a" and q1.lower() != "b":
        q1 = input("""
        Invalid answer. Must be a or b: """)
    if q1.lower() =="a":
        work_grade +=1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect answer. 0 points""")
    
    q2  = input("""
        Question 2.
        What command can you use to change directories?
        a) cd
        b) pwd
        c) vim
        Your Answer: """)
    while q2.lower() != "a" and q2.lower() != "b" and q2.lower() != "c":
        q2 = input("""
        Invalid answer. Must be a, b, or c: """)
    if q2.lower() =="a":
        work_grade +=1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect answer. 0 points""")
    
    q3 = input("""
        Question 3.
        True or False: Ubuntu is how you access the terminal
        a) True
        b) False
        You Answer:""")
    while q3.lower() != "a" and q3.lower() != "b":
        q3 = input("""
        Invalid answer. Must be a or b: """)
    if q3.lower() =="a":
        work_grade +=1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect answer. 0 points""")
    score = (work_grade/3)*100
    print(f"""
        Score: {score}

        After finishing homework, Matteo tells you that he's volunterring at a pet adoption place
        downtown. He asks if you want to come with him. Should you go?
        Type Y or N to go with Matteo. """)
    pick1 = user_options()
    if pick1 == True:
        h +=8
        so+= 12
        print("""
        Happiness +8
        Social +12
        
        You walk three dogs and play with some kittens. One of the volunteers goes up to you and
        comments on how well you are with the animals. She asks if you want to join the place as
        a volunteer and you can talk to her boss now to set it up. Should you meet the boss?
        Type Y or N to meet the boss.""")
        pick2 = user_options()
        if pick2 == True:
            g+= 0.1
            h+= 7
            so += 15
            print("""
        The boss comes out of her office and meets you at the front. You talk about the animals
        you want and the past ones you've had. She likes you so much that she says you can start
        next week!

        GPA +0.1
        Happiness +7
        Social +15""")
            g, h, so == check(g, h, so)
        elif pick2 == False:
            h -= 10
            so -=5
            print("""
        You decline since you're so busy already!

        As you go to walk another dog, it ends up peeing on your shoes!

        Happiness - 10
        Social -5

        Since your shoes are now ruined, you and Matteo head back to campus so you can change.
        He says he would rather hit the gym than go to class and asks if you're still going.
        Should you go to class or also go to the gym with him?
        Type Y or N to go to class.""")
            g, h, so = check(g, h, so)          
        pick3 = user_options()
        if pick3 == True:
            g+=0.1
            h+= 12
            so-=6
            print("""
        You tell him that you plan on going to class since you don't want to get behind in class.

        Later...
        
        After showering and changing you head to class. Less than 10 people are there so the Mr. Nax
        decides to give extra credit to all of the students who showed up!

        GPA +0.1
        Happiness +12
        Social -6""")
            g, h, so = check(g, h, so)
        elif pick3 ==False:
            g-=0.3
            h-=17
            so+=0
            print("""
        You tell him you'll join him since you're trying to get consistent in the gym.

        Later...

        While at the gym, Mr. Nax angrily emails everyone who skipped that those who showed up recieved
        extra credit for attendance. He stresses that attendance is important and should not be taken
        lightly.

        GPA -0.3
        Happiness -17
        Social +0""")
            g, h, so = check(g, h, so)
    elif pick1 == False:
        h+=5
        so+= 10
        print("""
        You decline and tell him that if you went you would want to adopt all of the animals.
        Instead you head to Whole Foods with Amaiya and her friends. They get mostly snacks and
        drinks. After an hour they decide they want to go to Chinatown for lunch and ask if you want
        to go, however this would mean no class at all today. Is Chinatown worth it?
        Type Y or N to go to Chinatown.""")
        pick2 = user_options()
        if pick2 == True:
            g-=0.3
            h+=5
            so+=13
            print("""
        GPA -0.3
        Happiness +5
        Social +13
        
        You guys take the trip to Chinatown and find a hidden gem. A little resturaunt that had
        THE BEST dumplings you've ever had. It was so amazing it brought tears to your eyes.

         After eating and walking for an hour, you all head to the station and it starts to downpour
         on all of you. Once you get to your dorm, you take a shower and have a spa day with the
         girls.

         Happiness +3""")
            h+=3
            g, h, so == check(g, h, so)
        elif pick2 == False:
            g +=0.2
            h -=6
            so +=2
            print("""
        You tell them you can't go to Chinatown today but next week you would love to go.

        GPA +0.2
        Happiness -6
        Social +2

        After saying by and walking towards your dorm, you see your friend Cait from your hometown.
        Since you haven't seen her in a bit, she gives you a dorm tour while you guys catch up.
        As the time gets closer to your COMP 141 class Cait trie to convince you to stay with her.
        Should you stay to keep talking or go to class?
        Type Y or N to go to class.""")
            g, h, so = check(g, h, so)          
        pick3 = user_options()
        if pick3 == True:
            g+=0.1
            h+=12
            so-=6
            print("""
        You tell her you would love to stay but you should really go to class. You guys make plans
        to hang out Saturday instead!

        When you go to class less than 10 people are there so the Mr. Nax
        decides to give extra credit to all of the students who showed up!

        GPA +0.1
        Happiness +12
        Social -6""")
            g, h, so = check(g, h, so)
        elif pick3 ==False:
            g+=0.3
            h-=10
            so-=3
            print("""
        You decide to just hang out with her instead since it's been so long. It's only one class
        right??

        Later..

        Mr. Nax angrily emails everyone who skipped that those who showed up recieved
        extra credit for attendance. He stresses that attendance is important and should not be taken
        lightly.

        GPA -0.3
        Happiness -10
        Social -3""")
            g, h, so = check(g, h, so)
    print("""
        After getting into bed, you sister calls you. It has been a long day so you debate if you
        shoud pick up. Do you pick up the phone?
        Type Y or N to pick up.""")
    pick4 =user_options()
    if pick4 == True:
        h+=25
        print("""
        She tells you she got tickets to your favorite artist's concert and wants to go with you!

        Happiness +25""")
        g, h, so = check(g, h, so)
    else:
        h-=30
        print("""
        You don't answer and decide to just scroll on your phone. She angrily texts you that she
        got tickets to your favorite artist's concert but since you don't want to pick up, she'll
        go with her friend.

        Happiness -30""")
        g, h, so = check(g, h, so)
    show_stats(g, h, so)
    return g, h, so

def friday(g, h, so):
    intro("Friday")
    print("""
        Your alarm goes off to wake you up for COMP 170. You don't have too much energy to go to class,
        but it's only Friday so you won't have class tomorrow and can sleep in. Also Ms. Woods sent out
        an email saying class on Friday would go over new material. Is it worth it to go to class and
        leave your nice, comfy bed?
        Type Y or N to go to class.""")
    pick1 = user_options()
    if pick1 == True:
        g+=0.3
        h -=  12
        so +=0
        print("""
        Turns out the new material is things you already know so you left your bed to relearn the same
        topic. You think about your amazing bed as you walk over to the dining hall for breakfast.

        GPA +0.3
        Happiness -12
        Social +0

        You get an email about registration for next semester being a little over a month away. It feels
        like time is flying so quickly already. You decide that you need to do something tonight to make
        memories but what should you do?""")
        g, h, so == check(g, h, so)
    elif pick1 == False:
        print("""
        You're only granted 30 more minutes of sleep when Juli barges into your room. You curse yourself
        for not locking your door.

        She asks you to help her pick out an outfit for the day. you don't really want to get up but remember
        that your plan is for her to get famous so that you can get famous by association, so you go to her room
        to help her. So much for sleeping in.

        30 minutes later...
        She thanks you for helping her and as a token of appreciation, she takes you to a cafe so you can get
        whatever you want on her!""")
    print("""
        After eating you realize that there is 20 more minutes until your MATH 118 class.
        Type Y or N to go to MATH 118.""")
    pick2 = user_options()
    if pick2 == True:
        g += 0.2
        h +=5
        so+= 4
        print("""
        MATH 118 11:30 - 12:20
        
        You and Professor Hill walk into the building at the same time. You guys make small talk and
        he tells you that your work in class has been great and to keep up the good work!
        
        GPA +0.2
        Happiness +5
        Social +4""")
        g, h, so == check(g, h, so)
    elif pick2 == False:
        g -=0.3
        h += 12
        so += 7
        print("""
        Instead of going to class you walk to the thrift store next to McDonald's. As you're there, you
        find an amazing pair of shoes that are in your size! Not only that, you find a jean jacket that
        looks exactly like the one in your Pinterest board. Perfect finds!!

        GPA -0.3
        Happines +12
        Social +7""")
        g, h, so = check(g, h, so)
    print("""
        Once again, it is getting close to your Sociology class time. Nothing too crazy should be happening
        in class today but do you really want to get a habit of missing class?
        Type Y or N to go to SOCL 101.""")
    pick3 = user_options()
    if pick3 == True:
        g += 0.2
        h -=3
        so +=2
        print("""
        SOCL 101 12:35 - 1:25
        
        You walk into class a little late but it's ok since Mr. Smith wasn't there yet. Olive, the girl that
        sits next to you in class tells you that she knows the TA for class, and today Mr. Smith plans on
        giving extra credit for the Final Exam to any student who will get up and dance in front of the class.
        Thank god embarrassement is a state of mind to you...

        Mr. Smith puts on pop music for your turn and you dance like never before. Who would say no to extra
        credit like this? Thankfully you know some of the people in class so it's not even awkward!

        GPA +0.2
        Happiness -3
        Social +2""")
        g, h, so = check(g, h, so)          
    elif pick3 ==False:
        g -= 0.2
        h -=5
        so -=8
        print("""
        Class can wait, right? Instead you meet up with Melita and head to the Student Center to get free food from
        a club event. Today it's Chipotle!

        10 minutes later...
        Olive, the girl who sits next to you in class tells you that Mr. Smith is giving out extra credit on the
        Final Exam to students who dance in front of the class. Out of any day to skip you accidently chose the day
        when you would do nothing in class and just watch people dance. Maybe there will be a next time.

        GPA -0.2
        Happiness -5
        Social -8""")
        g, h, so = check(g, h, so)
    print("""
        Having 10 minutes until Spanish class, you get a text from Angelina.
        
        Angelina:Hey girl!
        Angelina: Don't forget we have our final task in spanish today
        Angelina: last time i skipped it, my grade tanked so you gotta come

        You: omg thanks for reminding me ill see you there

        SPAN 101 1:40 - 2:30

        SPANISH FINAL TASK:""")
    task_grade = 0
    q1 = input("""
        Pregunta 1.
        Qué número es cuarenta?
        a) 20
        b) 30
        c) 40
        d) 50
        Your answer: """)
    while q1.lower() != "a" and q1.lower() != "b" and q1.lower != "c" and q1.lower() != "d":
            q1 = input("Invalid answer. Must be either a, b, c, or d :")
            break
    if q1 == "c":
        task_grade += 1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect. 0 points""")
        
    q2 = input("""
        Pregunta 2.
        Qué número es doce + uno?
        a) 13
        b) 14
        c) 12
        Your Answer: """)
    while q2.lower() != "a" and q2.lower() != "b" and q2.lower != "c":
            q2 = input("Invalid answer. Must be either a, b,  or c:")
            break
    if q2 == "a":
        task_grade += 1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect. 0 points""")
    q3 = input("""
        Pregunta 3.
        Cuál es 20?
        a) vienti
        b) vienta
        c) veinte
        Your Answer: """)
    while q3.lower() != "a" and q3.lower() != "b" and q3.lower != "c":
            q2 = input("Invalid answer. Must be either a, b,  or c:")
            break
    if q3 == "c":
        task_grade += 1
        print("""
        Correct! 1 point""")
    else:
        print("""
        Incorrect. 0 points""")
    score = (task_grade/ 3) * 100
    print(f"""
        Score : {score}

        Afterwards, you go to your dorm to lay and relax after the long day.

        A little later...

        You get text from Juli and Alex.

        Juli: hey the club event is from 7-9 in the student center
        Juli: there's an after party and since im in the club you can come with!!

        Alex: suppp wyd
        Alex: the party is at like 10 i can send you the address
        Alex: are you gonna come?

        Which one should you go to?
        Type Y or N to go to the club event and after party with Juli.""")
    pick4 = user_options()
    if pick4 == True:
        h+=20
        so +=25
        print("""
        You (to Juli): yes i would love to go
        You: let me get dressed and ill head over to your dorm

        Juli: kk

        You(to Alex): i agreed to go to this club event with another friend im sorry
        You: I promise the next one ill go

        Alex: np lmk how your thing goes

        The club event is making bracelets. Since Juli's in the club you get to meet a bunch of her friends!

        Happiness +20
        Social +25""")
    elif pick4 == False:
        h+=15
        so +=20
        print("""
        You (to Alex): yes i would love to go
        You: let me get dressed and lmk when to go to yours

        Alex: alrrr

        You(to Juli): sorry queen i can't make it
        You: pls lmk how it is ill go next time I swear

        Juli: lol no worries have fun

        The party was loud and Alex was right there was so many people!

        Happiness +15
        Social +20""")
    print("""
        At the end of the night you end up in bed and wonder how the week went by so fast and so slow at the
        same time. At least now you have the weekend!!""")
    show_stats(g, h, so)
    return g, h, so

#dunction end:
#takes stats and prints them for the very end of the week
#asks the user to rate UniEpisode out of ten and then says bye
def end (g, h, so):
    print(f"""
        Somehow, you made it through the week, good job!
        Ending Stats:
        GPA: {g}
        Happiness: {h}
        Social: {so}""")
    end = input("""
        Rate UniEpisode out of ten: """)
    print("""
        Bye!! Thank you SOOO much for playing!!
          
                luv, Olivia, Alona, and Riley <3""")


def week3(g, h, so):
    g1, h1, so1 = monday(g, h, so)
    g2, h2, so2 = tuesday(g1, h1, so1)
    g3, h3, so3 = wednesday(g2, h2, so2)
    g4, h4, so4 = thursday(g3, h3, so3)
    g5, h5, so5 = friday(g4, h4, so4)
    end(g5, h5, so5)
week3(3.0, 50, 50)











