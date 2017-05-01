name1= input('Enter first name:')

name2= input('Enter second name:')

name = name1 + " " + name2


score = 0


for character in name:

    if character in 'aeiou':

      score += 5

    if character in 'friend':

      score +=10

    if character in 'love':

      score +=15

    if character in 'enemy':

      score -= 5


print('Your score is:', score)

if score>=100:

    print('Best Friends!!')

if score<=5:

    print('Enemy')