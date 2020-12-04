import random

a = '-' * 50

def hangman():
    word = random.choice(['alpha', 'bravo', 'charlie', 'delta', 'echo'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    made = ''

    while len(word) > 0:
        mainWord = ''
        missed = 0


        for letter in word:
            if letter in made:
                mainWord = mainWord + letter
            else:
                mainWord = mainWord + '_' + ''


        if mainWord == word:
            print(mainWord)
            print('You Win !')
            break

        print('Guess the Word : ', mainWord)
        guess = input()


        if guess in validLetters:
            made = made + guess
        else:
            print('Enter a valid character')
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 9:
                print('9 Turns Left')
                print(' ---------- ')
            if turns == 8:
                print('8 Turns Left')
                print(' ---------- ')
                print('     O      ')
            if turns == 7:
                print('7 Turns Left')
                print(' ---------- ')
                print('     O      ')
                print('     |      ')
            if turns == 6:
                print('6 Turns Left')
                print(' ---------- ')
                print('     O      ')
                print('     |      ')
                print('    /       ')
            if turns == 5:
                print('5 Turns Left')
                print(' ---------- ')
                print('     O      ')
                print('     |      ')
                print('    / \     ')
            if turns == 4:
                print('4 Turns Left')
                print(' ---------- ')
                print('    \O      ')
                print('     |      ')
                print('    / \     ')
            if turns == 3:
                print('3 Turns Left')
                print(' ---------- ')
                print('    \O/     ')
                print('     |      ')
                print('    / \     ')
            if turns == 2:
                print('2 Turns Left')
                print(' ---------- ')
                print('    \O/|    ')
                print('     |      ')
                print('    / \     ')
            if turns == 1:
                print('1 Turns Left')
                print('Last Breath')
                print(' ---------- ')
                print('    \O_|    ')
                print('     |\     ')
                print('    / \     ')
            if turns == 0:
                print('You Lose')
                print(' ---------- ')
                print('     O_|    ')
                print('    /|\     ')
                print('    / \     ')
                break


name = input('Enter your name : ')
print(f'Welcome {name}')
print(a)
print('Try to guess the word in less than 10 attempts')
print(a)

hangman()
print()
