
"""
Created on Sun Oct 18 12:33:44 2020

@author: jinsoo.whang
"""

"""
    DocString:
    
    A) Introduction:
    This game is based on the Finals of the World Cup.
    It consists of four stages. This is a probability-game based on your choices.
    
    
    
    Stage 1: Introduction, kick-off and Full-time before user is subbed in.
    Stage 2: User is subbed in. User has choices to pass or dribble.
    Stage 3: User has choices to shoot, pass, or dribble.
    Stage 4: User takes a decision to score, pass, or dribble.
    
    B) Known Bugs and/or Errors:
    None.
    
"""

# Importing Random package
import random as rand
import time

def narration(word):
    """
    This will print text as if it were being narrated 
    
    PARAMETERS
    ----------
    word : the text you want to print as narration
    
    EXAMPLES
    ---------
    >>> narration("Hello World!")
    >>> Hello World!
    
    (Source: https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space/493399#493399)
    """
    for text in word:
        
        # Delaying time in seconds. 
        time.sleep(0.01)
        print(text, end="", flush=True)
        

def start_game():
    # These are global variables used throughout the game
    global user
    global user_country
    global user_rival
    global user_country_rival
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    narration("""\n\033[1mWelcome to the World Cup Finals!
    
    You are the star player joining the team towards the end of the World Cup Final. 
    You will be able to see the narration of the live game before you are subbed in.
    Once you are subbed in, you will be able to make decisions that determine the outcome of the game.
    Will you become a World Cup Champion?!
    
    \033[0m""")
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(2)
    
    # Print: What's your name?
    print("\nWhat is your name?")
    
    user = input('Input your name:\t').upper()
    
    # Print: What's your country? 
    print(f"\nHello {user}! Where are you from?")

    user_country = input('Input your country:\t').upper()

    # Print: What's your country's rival country?
    print(f"\n\U0001f600You are representing {user_country}\U0001f600! Which is your country's rival?")

    user_country_rival = input("Input your country's rival:\t").upper()

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(0.5)

    print(f"\n\U0001F62A{user_country_rival}\U0001F62A?! I hope you win!")

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(3)

    # Print: User in World Cup Final Announcement
    print(f"""\033[1m
    {"*" * 100}\033[0m""")
    narration(f"""\033[1m
        \U0001F4E3BREAKING NEWS\U0001F4E3:

        We have exciting news for {user_country}! Their \U0001F929star player\U0001F929, {user}, is back from
        a bad injury and will play the end of the World Cup Finals against {user_country_rival}!\033[0m
    """)
    print(f"""\n\033[1m
    {"*" * 100}\033[0m""")
    
    kick_off()
    
    
def kick_off():
    
    # This is a pause. User will have press a key to continue to the game
    print("Are you ready?")
    
    user_ready = input("Press < Enter > to continue:\n")
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(1)

    # Announcing kick off with some word play
    print("\n\033[1mKICK OFF! \n\nTHE \n\tWORLD \n\t\tCUP \n\t\t\tFINALS \n\t\t\t\t\tHAS \n\t\t\t\t\t\tSTARTED!!!\033[0m")
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument. 
    time.sleep(2)
    
    # This is the score of both teams
    user_country_score = 0
    user_country_rival_score = 0

    # These randomize the timestamp of the game
    time_randomizer_1 = rand.randint(a = 1, b = 30)
    time_randomizer_2 = rand.randint(a = 31, b = 50)
    time_randomizer_3 = rand.randint(a = 51, b = 70)
    time_randomizer_4 = rand.randint(a = 71, b = 80)
    
    # These randomize what will be in the narration of the game
    narrative_rand_1 = rand.randint(a = 0, b = 8)
    narrative_rand_2 = rand.randint(a = 0, b = 8)
    narrative_rand_3 = rand.randint(a = 0, b = 8)
    narrative_rand_4 = rand.randint(a = 0, b = 8)
    
    # These are lists of narration used in the game
    highlight_words = ['SAVE!', 'OPPORTUNITY!', 'CHANCE!', 'Highlight!', 'MISS!', 'Freekick!', 'Direct shot!', 'Throw-in!', 'GOOD PASS!', 'GOOD SHOT']
    ball_words = ['hit', 'stroke', 'contacted', 'smacked', 'tapped', 'touched', 'made contact on', 'lightly touched', 'blew to', 'flew to']
    player_positions = ['goalie', 'defender', 'midfielder', 'attacker', 'winger', 'striker', 'captain', 'player', 'last player', 'referee']
    goalie_save = ['feet', 'hand', 'head', 'chest', 'knee', 'shoulder', 'elbow', 'ankle', 'back', 'arm']
    ball_direction = ['trickled out for a corner', 'hit the post', 'left wide off the goal', 'left high off the goal', 'the defender cleared the ball', 'brushed the side of the post', 'launched off the goal', 'rebounded into the field', 'cleared to the sideline', 'the defender headed it off the field']
    
    
    # This is the first narration of the game
    narration(f"""
    \033[1mMinute {time_randomizer_1}:\033[0m {user_country}'s {highlight_words[narrative_rand_1]}\U0001F643 The ball {ball_words[narrative_rand_2]} the {player_positions[narrative_rand_3]}'s {goalie_save[narrative_rand_4]} and {ball_direction[narrative_rand_1]} 
    """)

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(1)

    narrative_rand_1 = rand.randint(a = 0, b = 8)
    narrative_rand_2 = rand.randint(a = 0, b = 8)
    narrative_rand_3 = rand.randint(a = 0, b = 8)
    narrative_rand_4 = rand.randint(a = 0, b = 8)

    # This is the second narration of the game
    narration(f"""
    \033[1mMinute {time_randomizer_2}:\033[0m {user_country_rival}'s {highlight_words[narrative_rand_1]}\U0001F605 The ball {ball_words[narrative_rand_2]} the {player_positions[narrative_rand_3]}'s {goalie_save[narrative_rand_4]} and {ball_direction[narrative_rand_1]} 
    """)

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(1)

    narrative_rand_1 = rand.randint(a = 0, b = 8)
    narrative_rand_2 = rand.randint(a = 0, b = 8)
    narrative_rand_3 = rand.randint(a = 0, b = 8)
    narrative_rand_4 = rand.randint(a = 0, b = 8)

    # This is the third narration of the game
    narration(f"""
    \033[1mMinute {time_randomizer_3}:\033[0m {user_country}'s {highlight_words[narrative_rand_1]}\U0001F643 The ball {ball_words[narrative_rand_2]} the {player_positions[narrative_rand_3]}'s {goalie_save[narrative_rand_4]} and {ball_direction[narrative_rand_1]} 
    """)

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(1)

    narrative_rand_1 = rand.randint(a = 0, b = 8)
    narrative_rand_2 = rand.randint(a = 0, b = 8)
    narrative_rand_3 = rand.randint(a = 0, b = 8)
    narrative_rand_4 = rand.randint(a = 0, b = 8)

    # This is the fourth narration of the game
    narration(f"""
    \033[1mMinute {time_randomizer_4}:\033[0m {user_country_rival}'s {highlight_words[narrative_rand_1]}\U0001F605 The ball {ball_words[narrative_rand_2]} the {player_positions[narrative_rand_3]}'s {goalie_save[narrative_rand_4]} and {ball_direction[narrative_rand_1]} 
    """)

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(1)

    # This is the announcement of Full Time before Over Time
    print(f"""
    \033[1mFULL TIME!\033[0m Score is tied {user_country} {user_country_score} : {user_country_rival} {user_country_rival_score}
    """)
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(2)
    
    # This is the announcement of Over Time
    print(f"""
    \033[1mIt is OVERTIME.\033[0m Golden Goal: Next team to score a goal WINS! 
    """)
    
    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(2)

    # This is the announcement when the user is subbed in
    narration(f"""

    \033[1m{user} is being subbed in!\033[0m Will {user} be able to score and become a World Cup Champion?

    """)

    # Pausing the game in seconds. Argument is not able to take 'seconds' as argument.
    time.sleep(2)
    
    user_plays()
    
    
def user_plays():
    # This is the first play that the user makes
    print(f""" 

        \033[1m{user_country} recovered the ball from their half of the field. {user} has the ball!\033[0m

        What will you do with the ball?

        1. short pass
        2. long pass 
        3. dribble   
    """)
    
    # User has 2 attempts to get past this room
    user_attempts = 2
    
    # While condition to see if user still has attempts to keep playing
    while user_attempts > 0:
        
        # This will randomnly select a number between 1 to 100.
        success_chances = rand.randint(a = 0, b = 100)
        
        # Recording the user's input
        first_play = input("Input your action: \n")
        
        # If user chooses this input, user has 95% chance of getting past this room
        if first_play == '1' or first_play.lower() == 'short pass' or 'short' in first_play.lower() or first_play.lower() == 'one':
            
            # If user succeeds, user moves to the next room
            if success_chances > 5:
                time.sleep(2)
                narration(f"\n\033[1mSuccessful pass! {user} is leading the attack!\033[0m")
                user_plays_2()
                break
                
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts -= 1
                narration(f"""\n\033[1m{user} missed the pass!\033[0m You have {user_attempts} attempt(s) remaining.\n""")

        # If user chooses this input, user has 90% chance of getting past this room
        elif first_play == '2' or first_play.lower() == 'long pass' or first_play.lower() in 'long' or first_play.lower() == 'two':
            
            # If user succeeds, user moves to the next room
            if success_chances > 10:
                time.sleep(2)
                narration(f"\n\033[1mSuccessful pass! {user} is leading the attack!\033[0m")
                user_plays_2()
                break
            
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts -= 1
                narration(f"""\n\033[1m{user} missed the pass!\033[0m \nYou have {user_attempts} attempt(s) remaining.\n""")   
               
        # If user chooses this input, user has 70% chance of getting past this room
        elif first_play == '3' or first_play.lower() == 'dribble' or first_play.lower() == 'three':
            if success_chances > 30:
                time.sleep(2)
                narration(f"\n\033[1mGood dribble! {user} goes past {user_country_rival}'s offense!\033[0m")
                user_plays_2()
                break
                
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts -= 1
                narration(f"""\n\033[1m{user} failed the dribble!\033[0m \nYou have {user_attempts} attempt(s) remaining.\n""")
        
        # User placed wrong input, so try again
        else:
            print("Wrong input. Please try again.")
            time.sleep(1)
    
    # If no more attempts remaining, user loses the game
    if user_attempts == 0:
        fail()

        
def user_plays_2():
    # This is the second play that the user makes

    print(f""" 

        \033[1m{user_country} is two-thirds of the way to {user_country_rival}'s goal. {user} has the ball again!\033[0m

        What will you do with the ball?

        1. long shot
        2. pass 
        3. dribble   
    """)
 
    # User has 2 attempts to get past this room
    user_attempts_2 = 2
    
    # While condition to see if user still has attempts to keep playing
    while user_attempts_2 > 0:
        
        # This will randomnly select a number between 1 to 100
        success_chances_2 = rand.randint(a = 0, b = 100)
        
        # Recording the user's input
        second_play = input("Input your action: \n")
        
        # If user chooses this input, user has 5% chance of getting past this room
        if second_play == '1' or 'long' in second_play.lower() or 'sho' in second_play.lower() or second_play.lower() == 'one':
            
            # If user succeeds, user moves to the next room
            if success_chances_2 > 95:
                time.sleep(2)
                narration(f"\n\033[1mGoal! {user} has scored the winning goal!\033[0m")
                print("""
 #####                       ### 
#     #  ####    ##   #      ### 
#       #    #  #  #  #      ### 
#  #### #    # #    # #       #  
#     # #    # ###### #          
#     # #    # #    # #      ### 
 #####   ####  #    # ###### ###           
            
            """)
                win()
                break
                
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts_2 -= 1
                narration(f"""\n\033[1m{user} stumbled! The ball is loss...\033[0m \nYou have {user_attempts_2} attempt(s) remaining.\n""")
        
        # If user chooses this input, user has 80% chance of getting past this room
        elif second_play == '2' or 'pass' in second_play.lower() or second_play.lower() == 'two':
            
            # If user succeeds, user moves to the next room
            if success_chances_2 > 20:
                time.sleep(2)
                narration(f"""\n\033[1m{user} finds a teammate with a GREAT PASS!\033[0m""")
                user_plays_3()
                break
                
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts_2 -= 1
                narration(f"""\n\033[1m{user} missed the pass! The ball is loss...\033[0m \nYou have {user_attempts_2} attempt(s) remaining.\n""")   
                
        # If user chooses this input, user has 40% chance of getting past this room        
        elif second_play == '3' or second_play.lower() == 'dribble' or second_play.lower() == 'three':
            
            # If user succeeds, user moves to the next room
            if success_chances_2 > 60:
                time.sleep(2)
                narration(f"\n\033[1mGreat dribble! What an elegant display from {user}!\033[0m")
                user_plays_3()
                break
                
            # If user does not succeed, user loses 1 attempt. If no attemps remaining, user loses the game
            else:
                time.sleep(2)
                user_attempts_2 -= 1
                narration(f"""\n\033[1m{user} failed the dribble! The ball is loss...\033[0m \nYou have {user_attempts_2} attempt(s) remaining.\n""")    
        
        # User placed wrong input, so try again
        else:
            print("Wrong input. Please try again.")
            time.sleep(1)
    
    # If no more attempts remaining, user loses the game
    if user_attempts_2 == 0:
        fail()
            
        
def user_plays_3():
    # This is the final play that the user makes

    print(f""" 

        \033[1m{user_country} is inside {user_country_rival}'s box! {user} has the ball!!!\033[0m

        What will you do with the ball?

        1. shoot
        2. pass 
        3. dribble   
    """)

    # This will randomnly select a number between 1 to 100
    success_chances_3 = rand.randint(a = 0, b = 100)
    
    final_play = input("Input your action: \n")
    
    # If user chooses this input, user has 85% chance of winning the game
    if final_play == '1' or 'sho' in final_play.lower() or final_play.lower() == 'one':
        
        # If user succeeds, user wins the game
        if success_chances_3 > 15:
            time.sleep(2)
            narration(f"\n\033[1mGOALLLLLLLLL! {user} HAS SCORED THE WINNING GOAL!\033[0m")
            print("""
 #####                       ### 
#     #  ####    ##   #      ### 
#       #    #  #  #  #      ### 
#  #### #    # #    # #       #  
#     # #    # ###### #          
#     # #    # #    # #      ### 
 #####   ####  #    # ###### ###           
            
            """)
            win()
            
        # If user does not succeed, loses the game
        else:
            time.sleep(2)
            narration(f"""\n\033[1m{user} MISSED AN EASY SHOT!\033[0m""")
            fail()
            
    # If user chooses this input, user has 80% chance of winning the game        
    elif final_play == '2' or 'pass' in final_play.lower() or final_play.lower() == 'two':
        
        # If user succeeds, user wins the game
        if success_chances_3 > 20:
            time.sleep(2)
            narration(f"""\n\033[1m{user} GIVES A GREAT PASS! {user_country} SCORESSS!!!\033[0m""")
            print("""
 #####                       ### 
#     #  ####    ##   #      ### 
#       #    #  #  #  #      ### 
#  #### #    # #    # #       #  
#     # #    # ###### #          
#     # #    # #    # #      ### 
 #####   ####  #    # ###### ###           
            
            """)
            win()
            
        # If user does not succeed, loses the game
        else:
            time.sleep(2)
            narration(f"""\n\033[1m{user} MISSED A SIMPLE PASS!\033[0m""")
            user_attempts_2 -= 1
            fail()
    
    # If user chooses this input, user has 50% chance of winning the game
    elif final_play == '3' or final_play.lower() == 'dribble' or final_play.lower() == 'three':
        
        # If user succeeds, user wins the game
        if success_chances_3 > 50:
            time.sleep(2)
            narration(f"\n\033[1m{user} DRIBBLES PAST THE GOALKEEPER!!! AND...\033[0m")
            time.sleep(2)
            narration(f"\n\033[1m{user} SCORESSS!!!\033[0m")
            
            # This print statement was borrowed from Professor Chase's lecture slides. Thanks Professor!!!
            print("""
 #####                       ### 
#     #  ####    ##   #      ### 
#       #    #  #  #  #      ### 
#  #### #    # #    # #       #  
#     # #    # ###### #          
#     # #    # #    # #      ### 
 #####   ####  #    # ###### ###           
            
            """)
            win()
            
        # If user does not succeed, loses the game
        else:
            time.sleep(2)
            narration(f"""\n\033[1m{user} FAILED THE DRIBBLE!\033[0m""")
            fail()
    
    # User placed wrong input, so try again
    else:
        print("Wrong input. Please try again.")
        time.sleep(1)
    
    
def fail():
    # User has lost
    time.sleep(1)
    narration(f"""\n\n\033[1m{user_country_rival} take the ball, counterattack and SCOREEE!!!\033[0m""")
    time.sleep(1)
    narration(f"\n\n\033[1m{user} has lost the World Cup Final.\033[0m")
    time.sleep(1)
    
    # User will be asked to play again
    try_again()
    
    
def win():
    # User has won 
    time.sleep(2)
    
    # Printing Champion Banner
    print(f"""
██╗░░░██╗░█████╗░██╗░░░██╗  ░█████╗░██████╗░███████╗  ████████╗██╗░░██╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██║░░██║██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ███████║██████╔╝█████╗░░  ░░░██║░░░███████║█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██╗██╔══╝░░  ░░░██║░░░██╔══██║██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║███████╗  ░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗░█████╗░███╗░░██╗██╗
██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██║██╔══██╗████╗░██║██║
██║░░╚═╝███████║███████║██╔████╔██║██████╔╝██║██║░░██║██╔██╗██║██║
██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝░██║██║░░██║██║╚████║╚═╝
╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░░░░██║╚█████╔╝██║░╚███║██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝
    
    """)
    time.sleep(1)
    
    # User will be asked to play again
    try_again()

def try_again():
    """
    This code will be used to ask the user if he/she wants to play again.
    If yes, user starts the game again. If no, user exits the game.
    """
    
    # Asking user to try again
    play_again = input("\nTry Again?\nType Yes or No:\t")
    
    # If yes, start game from beginning or the first play
    if "y" in play_again.lower():
        
        # Recording user input
        from_where = input("\nWould you like to try from the first play or from the introduction?\nType first play or introduction:\t")
        
        # If user chooses this input, user starts from first play
        if "first" in from_where.lower():
            user_plays()
         
        # If user chooses this input, user starts from introduction
        elif "intro" in from_where.lower():
            start_game()
        
        # Otherwise, user goes back to Try Again
        else:
            print("\nWrong input. Please try again")
            try_again()

    # If no, exit game
    elif "n" in play_again.lower():
        exit(0)
    
    # If input is wrong, try again to place input
    else:
        print("\nWrong input. Please try again")
        try_again()

# This starts the game
start_game()
