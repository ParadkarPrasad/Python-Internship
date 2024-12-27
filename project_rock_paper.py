import random
while True:
  my_answer = input('Choose: rock, paper or scissor: ')
  myanswer = my_answer.lower()

  if myanswer == 'quit':
    break

  if my_answer != "rock" and my_answer != "paper" and my_answer != "scissor":
    print('Please choose a correct answer')
    continue

  computer_answer = random.choice(['rock', 'paper', 'scissor'])


  print(f"Computer picked: {computer_answer}")
  if my_answer == computer_answer:
    print('You tied')

  elif my_answer == 'paper' and computer_answer == 'rock':
    print('You win')
    break

  elif my_answer == 'rock'and computer_answer == 'scissor':
    print('You win')
    break

  elif my_answer == 'scissor' and computer_answer == 'paper':
    print('You win')
    break

  else:
    print('You lost the game. Try Again 😢')
