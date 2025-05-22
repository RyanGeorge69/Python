import random
from colorama import *
import time
player1_pos = 0
player2_pos = 0
turn = 0
snake={39:3,46:11,52:31,73:58,80:40,87:32,93:70,96:79,98:6}
ladder={8:18,14:29,25:47,43:62,71:91,74:95}
while player1_pos<100 or player2_pos<100:
    #
    time.sleep(1)
    print()
    a=random.randint(1, 6)
    print(f"Player 1 rolled={a}")
    player1_pos += a
    for k,v in ladder.items():
        if k==a:
            print(f"{Fore.BLUE}Player 1  got ladder{Style.RESET_ALL}")
            player1_pos = v
    for k,v in snake.items():
        if k==a:
            print(f"{Fore.RED}Player 1 got Snake{Style.RESET_ALL}")
            player1_pos = v
    b = random.randint(1, 6)
    print(f"Player 2 rolled={b}")
    player2_pos += b
    for k,v in ladder.items():
        if k==b:
            print(f"{Fore.BLUE}Player 2 got ladder{Style.RESET_ALL}")
            player2_pos=v
    for k,v in snake.items():
        if k==b:
            print(f"{Fore.RED}Player 2 got Snake{Style.RESET_ALL}")
            player2_pos=v

    turn+=1
    print(f"The turn is {turn}")
    print(f"player1={player1_pos}")
    print(f"player2={player2_pos}")
