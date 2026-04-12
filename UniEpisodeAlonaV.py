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
        score : (quiz_grade / 3)*100
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
        score : (quiz_grade / 3)*100
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
        score = (word_grade /3)*100
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
        score = (word_grade /3)*100
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
        pick2 = user_option()
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
        pick2 = user_option()
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
            g, h, so= = check(g, h, so)
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
        pick2 = user_option()
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
            g, h, so= = check(g, h, so)
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
        g, h, so= = check(g, h, so)
    elif pick2 == False:
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
    pick2 = user_option()
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
        g, h, so= = check(g, h, so)
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
    task_grade:0
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
        Bye!!""")


def week3(g, h, so):
    g1, h1, so1 = monday(g, h, so)
    g2, h2, so2 = tuesday(g1, h1, so1)
    g3, h3, so3 = wednesday(g2, h2, so2)
    g4, h4, so4 = thursday(g3, h3, so3)
    g5, h5, so5 = friday(g4, h4, so4)
    end(g5, h5, so5)
week3(3.0, 50, 50)












