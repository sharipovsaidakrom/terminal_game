characters = int(input('Select your character (1 - 3) \n 1) Alex =_= \n 2) Cody +_+ \n 3) Neo  -_- \n'))
health = 100


if characters == 1:
  print('\n 💪 Alex \n Super Power: Strong Body \n Effect: Starts with 120 health instead of 100. \n Play Style: Tanky, good for lasting longer even with wrong answers.')
  health += 20

  answer = input('What is the center of our solar system? ')
  if answer == 'Sun':
    print('You`ve got it! Let`s move on to next step')
  else:  
    while answer != 'Sun':
      if health < 21:
        print('You lost the game. Try it over')
        break
      else: 
        health -= 20
        answer = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What is the center of our solar system? ') 

  if health > -1:
    answer2 = int(input('How many planets are in our solar system? '))
    if answer2 == 8: 
      print('Not bad let`s see you on the next one!')
    else:
      while answer2 != 8:
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer2 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n How many planets are in our solar system? ') 

  if health > -1:
    answer3 = input('Which planet is known as the Red Planet? ')
    if answer3 == 'Mars': 
      print('Woow buddy, you`re doing great. Don`t give up!')
    else:
      while answer3 != 'Mars':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer3 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is known as the Red Planet?  ') 

  if health > -1:
    answer4 = input('Which planet is the largest in our solar system? ')
    if answer4 == 'Jupiter': 
      print('I can not trust myself, you`re the one came here for the first time! Let`s check the nect one')
    else:
      while answer4 != 'Jupiter':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer4 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is the largest in our solar system?  ') 

  if health > -1:
    answer5 = input('What galaxy do we live in? ')
    if answer5 == 'Milky Way': 
      print('Congratulations! You won the game!')
    else:
      while answer5 != 'Milky Way':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer5 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What galaxy do we live in?  ') 

elif characters == 2:
  print('\n 🧠 Cody \n Super Power: Second Chance \n Effect: Can retry 1 wrong answer once per game. \n Play Style: Useful for tricky questions; great for smart guessing.')

  answer = input('What is the center of our solar system? ')
  if answer == 'Sun':
    print('You`ve got it! Let`s move on to next step')
  else:  
    while answer != 'Sun':
      if health < 21:
        print('You lost the game. Try it over')
        break
      else: 
        health -= 20
        answer = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What is the center of our solar system? ') 

  if health > -1:
    answer2 = int(input('How many planets are in our solar system? '))
    if answer2 == 8: 
      print('Not bad let`s see you on the next one!')
    else:
      while answer2 != 8:
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer2 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n How many planets are in our solar system? ') 

  if health > -1:
    answer3 = input('Which planet is known as the Red Planet? ')
    if answer3 == 'Mars': 
      print('Woow buddy, you`re doing great. Don`t give up!')
    else:
      while answer3 != 'Mars':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer3 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is known as the Red Planet?  ') 

  if health > -1:
    answer4 = input('Which planet is the largest in our solar system? ')
    if answer4 == 'Jupiter': 
      print('I can not trust myself, you`re the one came here for the first time! Let`s check the nect one')
    else:
      while answer4 != 'Jupiter':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer4 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is the largest in our solar system?  ') 

  if health > -1:
    answer5 = input('What galaxy do we live in? ')
    if answer5 == 'Milky Way': 
      print('Congratulations! You won the game!')
    else:
      while answer5 != 'Milky Way':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer5 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What galaxy do we live in?  ') 


elif characters == 3:
  print('\n 🔮 Neo \n Super Power: Cosmic Insight \n Effect: Can see the correct answer once per game before answering. \n Play Style: Strategic; save it for the hardest question.')

  answer = input('What is the center of our solar system? ')
  if answer == 'Sun':
    print('You`ve got it! Let`s move on to next step')
  else:  
    while answer != 'Sun':
      if health < 21:
        print('You lost the game. Try it over')
        break
      else: 
        health -= 20
        answer = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What is the center of our solar system? ') 

  if health > -1:
    answer2 = int(input('How many planets are in our solar system? '))
    if answer2 == 8: 
      print('Not bad let`s see you on the next one!')
    else:
      while answer2 != 8:
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer2 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n How many planets are in our solar system? ') 

  if health > -1:
    answer3 = input('Which planet is known as the Red Planet? ')
    if answer3 == 'Mars': 
      print('Woow buddy, you`re doing great. Don`t give up!')
    else:
      while answer3 != 'Mars':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer3 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is known as the Red Planet?  ') 

  if health > -1:
    answer4 = input('Which planet is the largest in our solar system? ')
    if answer4 == 'Jupiter': 
      print('I can not trust myself, you`re the one came here for the first time! Let`s check the nect one')
    else:
      while answer4 != 'Jupiter':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer4 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n Which planet is the largest in our solar system?  ') 

  if health > -1:
    answer5 = input('What galaxy do we live in? ')
    if answer5 == 'Milky Way': 
      print('Congratulations! You won the game!')
    else:
      while answer5 != 'Milky Way':
        if health < 20:
          print('You lost the game. Try it over')
          break
        else: 
          health -= 20
          answer5 = input(f'Wrong answer, 20 HP is taken from you. \n Your HP is {health} \n What galaxy do we live in?  ') 
  

else:
  print('Please select the available character \n Please restart the game')
  
  