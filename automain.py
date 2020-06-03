import random, replit
from termcolor import cprint

#Introduction
print()
cprint('Welcome to Master Mind!', 'red')
cprint('=============================', 'red')
print()

def reset():
    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To autoplay immediately, type 'P')
''')

    choice = input('Type here: ').upper()

    if choice == 'I':

        #Prints Instructions
        print(open('instructions.txt', 'r').read())

        input('Press [enter] when ready to play.')

    elif choice !='P':
        replit.clear()
        reset()

    # Generate Puzzle
    puz = generate_puzzle()

    # Generate first guess
    firstguesses = firstplay()

    # Pass puzzle and first guess to play
    play(firstguesses, puz)

    
# Generate puzzle
def generate_puzzle():

    
    a = [0, 0, 0, 0]
    
    for i in range(4):
        a[i] = random.randint(1, 6)
        
    return a

# Initial guess
def firstplay():

    guesses = [0, 0, 0, 0]

    
    for a in range(4):
        guesses[a] = random.randint(1, 6)

    return guesses


'''
This function first passes the puzzle and firstguess to hints - then uses the hints to optimize its possible pool of guesses - then calls itself again with an updated guess. 
This will keep going until the guess is correct and the program ends in the hints function'''
# UNFINISHED
def play(guesses, puz):

    # Runs the current guess through the hints function to see if it was correct and (if not) get updated hints
    correctall, correct = hints(guesses, puz)


    # UNFINISHED - Make a list of all possible guesses - Haven't figured out proper syntax yet for this situation

    possible = [[]]

    for a in range(4):
        for b in range(6):
            possible[a][b] = b+1


    # Calls itself again with an updated guess
    play(guesses, puz)


# Check user's input and give hints
def hints(g, p):

    
    correctall = 0
    correct = 0
    tracker = [0, 0, 0, 0]
    

    for b in range(4):

        if p[b] == g[b]:
            correctall += 1
            tracker[b] = p[b]

        else:
            for c in range(4):
                if p[b] == g[c] and p[b] not in tracker:
                    correct+= 1
                    tracker[b] = p[b]
                    break


    # This is where the program will end if the play function has optimized the possible guesses to the point where it guesses correctly
    if correctall == 4:
        print("You win!!")
        quit()

    print("You guessed " + str(correctall) + " colors AND positions correctly!")
    print("You guessed " + str(correct) + " colors correctly but they're in the WRONG position! What are your next guesses?")

    return(correctall, correct)

reset()