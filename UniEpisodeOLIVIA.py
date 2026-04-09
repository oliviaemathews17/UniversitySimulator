#This is the code for the university episode app. OLIVIA MATHEWS

#Each class is a function
#Each scenario is a function
#Each day is a function which contains the functions for the events of that day
#The main function will be the entire week, which will call the day functions in order

#If the user chooses something that is not an option, the program will print "Invalid choice, please try again" and ask the user to choose again
# Figure out how to make the user choose again without having to restart the program

#I have to make variables that will be affected by the user's choices, such as grades, social life, mental health, etc. 
# These variables will be used to determine the outcome of the week and the final result.



# for now, I am going to use my schedule for the week
#MWF: comp, phil, math, socl
#TTH: phil, chinese



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

#------------------------------------------------------------------------------------------------------------------


#THE FOLLOWING CODE IS OLIVIAS WEEK 


#variables
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

def journalEntry(day):
    print('''Let's unwind with some journaling. 
          
            Take a moment to reflect on your day, and write down your thoughts and feelings about your experiences.         
          
         ''')
    
    with open('journal.txt', 'w') as journal:
        entry = input("Write your journal entry here (x to exit): ").lower()
        while entry != 'x':
            journal.write(day + ": " + entry + "\n")
            entry = input("Continue writing...(x to exit): ").lower()


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
    print("Philosophy has ended, thank goodness. You have ten minutes before Math starts.")
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
    print('''Final stats:
          GPA: ''' + str(gpa) + '''
          Social: ''' + str(social) + '''
          Happiness: ''' + str(happiness))
    enterContinue()







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
    years = input("How many years has your philosophy teacher been teaching? ")
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
        

        print('''After spending the day in Chinatown, you feel like you have learned so much about Chinese culture, and you have had a great time exploring the city.
          You take the train back to campus, and make your way to your dorm. You feel happy and fulfilled, and you can't wait to start writing your paper!''')


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
    
