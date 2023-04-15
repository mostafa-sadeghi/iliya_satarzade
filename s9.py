# for i in range(5):
#     print("i want to learn pygame")
#     print(i)
# print("outside")


# for i in range(1,11):
#     print(i, end=' ')

# print()
# for i in range(1,11,2):
#     print(i, end=' ')

# print()
# for i in range(2,11,2):
#     print(i, end=' ')

# for j in range(10,0,-1):
#     print(j, end=' ')
# print()
# for s in 'iliya':
#     print(s, end=' ')
# print()
# for n in [1,2,3,4,5]:
#     print(n*2)
# for i in range(3):
#     print("a")
# for j in range(3):
#     print("b")

# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

# for i in range(3):
#     print("hello")
# i = 0
# while i<3:
#     print("hello")
#     i += 1



# done = False
# while not done:
#     quit = input('Do you want to quit? ')
#     if quit == 'y':
#         done = True


import random

# for i in range(10):
#     print(random.randrange(100,201))
player_score = 0
computer_score = 0
ACTIONS = ("rock","paper","scissors")
while True:
    print("game started...")
    computer_hand = random.choice(ACTIONS)
    print("Enter '0' => 'rock', '1' => 'paper', '2' => 'scissors' ...")
    user_selection = input('> ')
    player_hand = ACTIONS[int(user_selection)]

    if player_hand == 'rock' and computer_hand == 'scissors':
        player_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("player is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    elif player_hand == 'scissors' and computer_hand == 'paper':
        player_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("player is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    elif player_hand == 'paper' and computer_hand == 'rock':
        player_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("player is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    ##################################################################
    elif player_hand == 'scissors' and computer_hand == 'rock':
        computer_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("computer is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    elif player_hand == 'paper' and computer_hand == 'scissors':
        computer_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("computer is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    elif player_hand == 'rock' and computer_hand == 'paper':
        computer_score += 1
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("computer is the winner")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    ###################################################################
    else:
        print("player's hand: ", player_hand)
        print("computer's hand: ", computer_hand)
        print("BOTH EQUAL")
        print(f'{"PLAYER":<10}{"SCORE":>9}')
        print(f'{"ME":<10}{player_score:>9}')
        print(f'{"COMPUTER":<10}{computer_score:>9}')
    print("Do you want to continue? (Y)ES or (N)O")
    if input('> ').lower().startswith('n'):
        print("Thank you for joining us...")
        break
        

        