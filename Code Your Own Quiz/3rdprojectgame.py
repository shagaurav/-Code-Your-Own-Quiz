import time
# import the time module
import colorama
# import the module gives color
from colorama import init
init()
from colorama import Fore
# Four colors are used RED, GREEN, WHITE and YELLOW.
R, G, W, Y  = Fore.RED, Fore.GREEN, Fore.WHITE, Fore.YELLOW
print ''+G+'' "Welcome to my Quiz" ''+W+''
name = raw_input("Enter your name : ")
name = name[0].upper() + name[1:].lower()

"""
For easy level, Fill IN THE BLANKS SCIENCE GAME
""" 
easy = ''+G+''"""Our solar system is made up of the sun and everything that __1__ around it. 
This includes __2__ planets and their natural satellites such as Earth's moon; dwarf planets
such as Pluto and Ceres; asteroids; comets and meteoroids The Sun is the center of our __3__. 
It contains almost all of the mass in our solar system and exerts a tremendous gravitational 
pull on planets and other bodies. Our solar system formed about 4.6 billion __4__ ago. The four 
planets closest to the sun -- Mercury, Venus, __5__, and Mars -- are called the terrestrial 
planets because they have solid, rocky surfaces. Two of the outer planets beyond the orbit of 
Mars __6__ and Saturn are known as gas giants; the more distant Uranus and Neptune are 
called __7__ giants.
"""''+W+''
"""
Answers for easy level, fill in the blanks science game
"""
Answers_1 = [ 'travels', 'eight', 'solar system', 'years', 'earth', 'jupiter', 'ice']

"""
For medium level, Fill IN THE BLANKS MATHEMATICS GAME
"""
medium = ''+G+''"""Fill in the placeholders in worksheet on tens and ones by writing numbers in figures.

1. Fifty six   =   __1__ (Tens,Ones)

2. Seventy eight   =   __2__ (Tens,Ones)

3. Eighty five   =   __3__ tens (Tens,Ones)

4. Sixty nine   =   __4__ tens (Tens,Ones)

5. Seventy two   =   __5__ tens (Tens,Ones)

"""''+W+''
"""
Answers for medium level, fill in the blanks mathematics game
"""
Answers_2 = ['5,6','7,8', '8,5', '6,9', '7,2']

"""
For hard level, Fill IN THE BLANKS PSYCHOLOGICAL GAME
"""
hard = ''+G+''"""Psychology is the science of behavior and mind, embracing all aspects of 
conscious and unconscious experience as well as thought. It is an academic discipline and a social science 
which seeks to understand individuals and groups by establishing general principles and researching 
specific cases.In this field, a professional practitioner or researcher is called a psychologists and can be 
classified as a social, behavioral, or cognitive scientist. Psychologists attempt to understand 
the role of mental functions in individual and social behaviors, while also exploring the 
physiological and biological processes that underlie cognitive functions and behaviors.
"""''+W+''
"""
Answers for hard level, fill in the blanks psychological game
"""
Answers_3 = ['behavior', 'unconscious', 'psychologists', 'biological']

# setup strings into a list
paragraphs = [easy, medium, hard]
# here game function
input_list = [Answers_1, Answers_2, Answers_3]

# print(input_list).
def choose_level():
    """
    Choose your difficulty level("easy" or "e", "medium" or "m", "hard" or "h") 
    and fill in the blanks will appear on the basis of your selection.
    """
    level = raw_input("Enter your difficulty level (easy/medium/hard): ")
    # by typing easy or e, choose easy level.
    if level == "easy" or level == "e":
        print ''+Y+'' "Easy level selected\n" ''+W+''+"wait a second for question \n"
        time.sleep(1.5)
        return 0
    # by typing medium or m, choose meduim level.
    elif level == "medium" or level == 'm':
        print ''+Y+'' "Medium level selected\n" ''+W+''"wait a second for question \n"
        time.sleep(1.5)
        return 1
    # by typing hard or h, choose hard level.
    elif level == "hard" or level == 'h':
        print ''+Y+'' "Hard level selected\n" ''+W+''"wait a second for question \n"
        time.sleep(1.5)
        return 2
    else:
        print ''+R+'' "Invalid level selected" ''+W+''
        return choose_level()


# process the game level.
def process_game(level, blank):
    """
    process the paragraph for the given level and replaces the word in the input_list
    of the game whether the words are right or not and further processes the game.
    If it's right it goes on and if not try again.
    """
    paragraph = paragraphs[level]
    while blank < len(input_list[level]):
        word_to_replace = (input_list[level][blank])
        list_of_words = paragraph.split(" ")
        index = 0
        # Replace the word_to_replace with ___number___
        while index < len(list_of_words):
            if list_of_words[index] == word_to_replace:
                list_of_words[index] = "___" + str(blank + 1) + "___"
            index += 1

        blank += 1
        paragraph = " ".join(list_of_words)

    return paragraph


# The level prints out in the screen, play the game.
def operation(level):
    """
    play the given level, guess the answer and it prints
    the output answer and replace the answer with the blank.
    """
    blank = 0
    while blank < len(input_list[level]):
        print process_game(level, blank)
        # print "hi"
        question = "\nWhat should go in blank number "+str(blank+1)+" ? "
        answer = raw_input(question).lower()

        correct_answer = input_list[level][blank].lower()
        # used replace string which replaces blank answers with the correct answers
        if correct_answer == answer :
            print ''+Y+''"Correct"''+W+''
            paragraphs[level] = paragraphs[level].replace(("__"+str(blank+1)+"__"),correct_answer)
            blank += 1
        else:
            print ''+R+''"Try again"''+W+''

    print paragraphs[level]
    print "\n"+''+Y+''"Well played, you Rock!"''+W+''

# When all the levels are completed.
def gameplay():
    """
    It's the main part of the game here the game starts and ends and goes on, 
    when the level is completed choose your option to play the game 
    type "yes" or "y" to play further or "no" or "n" to leave the game, 
    after level 3 the game is in a loop mode. So, you only need to type the
    answer.
    """
    play_choice = raw_input(name + " are you ready to play game (yes/no): ")
    play_choice = play_choice.lower()
    # choose your options yes or no for different levels.
    if play_choice == 'yes' or play_choice == 'y':
        level = choose_level()
        while level < 3:
            operation(level)
            if level < 2:
                proceed = raw_input('Would you like to attempt a next level(y/n) : ')
                if proceed == 'yes' or proceed == 'y':
                    level += 1
                else:
                    break
        print ''+G+''"\n :) Thanks for playing! :) " ''+W+''

    elif play_choice == 'no' or play_choice == 'n':
        print ''+Y+'' "Thanks for visiting us" ''+W+''
        exit()


gameplay()