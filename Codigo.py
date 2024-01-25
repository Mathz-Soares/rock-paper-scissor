import random

def play():
    choice = input("what's your choice? use 'r' to rock, 'p' to paper or 's' to scissors \n")
    cpu = random.choice(['r', 'p', 's'])
    print("the cpu has chosen: ", cpu)
    
    if choice == cpu:
        return "it's a tie"
    elif is_win(choice, cpu):
        return "you won"
    else:
        return 'you lost'
def is_win(choice, cpu):
    if (choice == 'r' and cpu == 's') or (choice == 's' and cpu == 'r') or (choice == 'p' and cpu == 'r'):
        return True
print(play())
