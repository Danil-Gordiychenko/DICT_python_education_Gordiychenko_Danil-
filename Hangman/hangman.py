import random
print('HANGMAN')
print('The game will be available soon.')
print('Do you want to start the game?')
print('Type "play" to play the game, "exit" to quit:;')
while True:
    answer = input()
    if answer == "play":
        break
    elif answer == "exit":
        exit()
    else:
        print('Do you want to start the game?')
        print('Type "play" to play the game, "exit" to quit:;')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w,' 'x', 'y', 'z']
attempts = 8
my_list = ['python', 'java', 'javascript', 'php']
a = random.choice(my_list)
y = list(a)
guessed = ['_' for n in y]
while True:
    print('')
    print('HANGMAN')
    print(''.join(guessed))
    print('Input a letter:')
    char = input()[0]
    lne = len(char)
    make = ''.join(map(str, guessed))
    if char in y:
         for n, c in enumerate(y):
             if c == char:
                guessed[n] = char
         if "_" not in guessed:
            print('')
            print('HANGMAN')
            print("Thanks for playing! We'll see how well you did in the next stage")
            break
    if len(make) >= 2:
        print('You should input a single letter.')
    if char not in y:
        attempts -= 1
        print("That letter doesn't appear in the word")
    if char not in alphabet:
        print('Please enter a lowercase English letter.')
    if attempts == 0:
        print('You lost')
        break
