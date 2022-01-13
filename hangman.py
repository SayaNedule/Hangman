# Write your code here
import random
answers = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(answers)

dash = ''
lives = 8
tried_letters = []
for letter in answer:
    dash += '-'

print('H A N G M A N')
choice = input('Type "play" to play the game, "exit" to quit:')

print('')
print(dash)

while lives > 0:
    user_input = input('Input a letter:')
    if len(user_input) != 1:
        print('You should input a single letter')
        print('')
        print(dash)
    elif user_input.isupper():
        print('Please enter a lowercase English letter')
        print('')
        print(dash)
    elif user_input.isalpha() == False:
        print('Please enter a lowercase English letter')
        print('')
        print(dash)
    elif lives == 1:
        if user_input in answer:
            letter_count = answer.count(user_input)
            if user_input in dash:
                print("You've already guessed this letter")
                print('')
                print(dash)
            elif letter_count == 2:
                place1 = answer.index(user_input)
                place2 = answer.rindex(user_input)
                place1 = int(place1)
                place2 = int(place2)
                dash = dash[:place1] + user_input + dash[place1+1:]
                dash = dash[:place2] + user_input + dash[place2+1:]
                print('')
                print(dash)
                if dash.count('-') == 0:
                    print('You guessed the word!')
                    print('You survived!')
                    break
                else:
                    continue
            else:
                place = answer.index(user_input)
                place = int(place)
                dash = dash[:place] + user_input + dash[place+1:]
                print('')
                print(dash)
                if dash.count('-') == 0:
                    print('You guessed the word!')
                    print('You survived!')
                    break
                else:
                    continue
        else:
            if user_input in tried_letters:
                print("You've already guessed this letter")
                print('')
                print(dash)
            else:
                print("That letter doesn't appear in the word")
                lives -= 1
                tried_letters.append(user_input)
    else:
        if user_input in answer:
            letter_count = answer.count(user_input)
            if user_input in dash:
                print("You've already guessed this letter")
                print('')
                print(dash)
            elif letter_count == 2:
                place1 = answer.index(user_input)
                place2 = answer.rindex(user_input)
                place1 = int(place1)
                place2 = int(place2)
                dash = dash[:place1] + user_input + dash[place1+1:]
                dash = dash[:place2] + user_input + dash[place2+1:]
                print('')
                print(dash)
                if dash.count('-') == 0:
                    print('You guessed the word!')
                    print('You survived!')
                    break
                else:
                    continue
            else:
                place = answer.index(user_input)
                place = int(place)
                dash = dash[:place] + user_input + dash[place+1:]
                print('')
                print(dash)
                if dash.count('-') == 0:
                    print('You guessed the word!')
                    print('You survived!')
                    break
                else:
                    continue
        else:
            if user_input in tried_letters:
                print("You've already guessed this letter")
                print('')
                print(dash)
            else:
                print("That letter doesn't appear in the word")
                print('')
                print(dash)
                lives -= 1
                tried_letters.append(user_input)

if dash.count('-') != 0:
    print('You lost!')
