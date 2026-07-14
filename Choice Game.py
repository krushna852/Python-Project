import random 

def Choice_game(rand):
    user=None
    while True:
        user=input("Enter Any Number or Quiet: ")
        if user == "Quiet":
            break
        elif int(user) == rand:
            print("You Won...")
            break
        elif int(user) < rand:
            print("Your Number is less than Our Number")
        elif int(user) > rand:
            print("Your Number is Greater than Our number")
    
rand=random.randint(1,100)
Choice_game(rand)
print("....Game Over....")
