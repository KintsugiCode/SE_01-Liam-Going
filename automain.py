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

    puz = generate_puzzle()
    firstguesses = firstplay()
    play(firstguesses, puz)
    

def generate_puzzle():

    # Generate puzzle
    a = [0, 0, 0, 0]
    
    for i in range(4):
        a[i] = random.randint(1, 6)
        
    return a

def firstplay():

    guesses = [0, 0, 0, 0]

    # Initial guess
    for a in range(4)
        guesses[a] = random.randint(1, 6)

    return guesses
    
def play(guesses, puz)

    correctall, correct = hints(guesses, puz)

    

    play(guesses, puz)

def hints(g, p):
  
    # Enable print statements to make puzzle (and guesses) visible
    '''
    print(g)
    print(p)
    '''

    # Check user's input and give hints
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

    '''                
    print(tracker)
    '''
    
    if correctall == 4:
        print("You win!!")
        quit()

    print("You guessed " + str(correctall) + " colors AND positions correctly!")
    print("You guessed " + str(correct) + " colors correctly but they're in the WRONG position! What are your next guesses?")

    return(correctall, correct)

reset()