wrongguess=0
print('What do you get when you cross a snowman with a vampire?')
answer=input()
if answer == 'frostbite':
    print('you are correct')
else:
    print('You typed ' + answer + ' but the right answer is:')
    print('frostbite!')
    wrongguess=wrongguess+1

print()

print('What do dentists call a astronaut\'s cavity?')
answer=input()
if answer == 'a black hole':
    print('you are correct')
else:
    print('You typed ' + answer + ' but the right answer is:')
    print('A black hole!')
    wrongguess=wrongguess+1

print()
print('Knock knock.')
input()
print("Who's there?")
input()
print('Interrupting cow.')
input()
print('Interrupting cow wh', end='')
print('-MOO!')
if wrongguess==1:
    wrongguess=str(wrongguess)
    print('you had ' + wrongguess + ' wrongguess')
if wrongguess>1:
    wrongguess=str(wrongguess)
    print('you had ' + wrongguess + ' wrongguesses')
    

