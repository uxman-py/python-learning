import random

def main():
    while True:
            try:
                level = int(input("Level: "))
                if level > 0:
                     break
            except ValueError:
                 pass
        
    random_num = random.randint(1,level)
    
    while True:
         try:   
            user_guess = int(input("Guess: "))
            if user_guess<=0:
                 continue
            elif user_guess < random_num:
                print("Too small")
                continue
            elif user_guess > random_num:
                print("Too big")
                continue
            else:
                user_guess == random_num
                print("Just Right")
                break
         except ValueError:
              continue
main()