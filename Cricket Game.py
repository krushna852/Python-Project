import random


def innings(a,b,target=500):

    print(a,"team coming for batting")
    a_r=0
    a_w=0
    i=0
    runs=[0,1,2,3,4,6,"wicket"]
    while i < 2:
        j=1
        while j < 7:
                print(f"{i}.{j}")
                m=random.choice(runs)
                if m == "wicket":
                     print("Its wicket")
                     a_w += 1
                elif m in range(0,7):
                        print("Its",m,"runs")
                        a_r = a_r + m
                if a_w == 3:
                      print("Match Over all out")
                      return a_r
                if a_r >= target + 1:
                    print("Total runs of",a,"is",a_r)
                    print("Total Wicket of",a,"is",a_w)
                    return a_r
                j=j+1
        i = i+1
    print("Total runs of",a,"is",a_r)
    print("Total Wicket of",a,"is",a_w)
    return a_r

def check(a,b,target,result):
    if target > result:
        print(a,"team won the match")
    elif target == result:
        print("Tie...")
    else:
        print(b,"team Won")




while True:
    user = input("Play or Exit: ")
    choice=['bat','bowl']
    toss=['head','tail']
    if user.lower() == 'play':
        print("Welcome To Alpha Cricket NO pain Only Gain...")
        print("Choose Your Team:-")
        country=['india','australia','england','finland','pakisthan','afganisthan','west indies','usa','bangladesh','sri lanka','south africa']
        print(country)


        while True:
            user_c=input()
            if user_c.lower() in country:
                break
            else:
                print("Enter A countery Name From above list")

        country.remove(user_c)
        system_c=random.choice(country)
        print("Finding match for you")
        print(user_c,'vs',system_c)
        print("Staring The Game...")

        while True:
            user_choice = input("Enter Head or Tail:- ")
            if user_choice in toss:
                break
            else:
                print("You Enter Wrong Choice")
                
        if user_choice == random.choice(toss):
            print("You Won")
            print("Select Bat or Bowl...")
            while True:
                user_w= input()
                if user_w.lower() == "bat":
                    target=innings(user_c,system_c)
                    print("The target is",target+1)
                    result=innings(system_c,user_c,target=target+1)
                    check(user_c,system_c,target,result)
                    print("Game Finished...")
                    break

                elif user_w.lower() == "bowl":
                    target = innings(system_c,user_c)
                    print("The target is",target+1)
                    result = innings(user_c,system_c,target=target+1)
                    check(system_c,user_c,target,result)
                    print("Game Finished...")
                    break
                else:
                    print("Invalid Decison")
        else:
            print("You Lost")
            system_w=random.choice(choice)
            print(system_c,"choose to",system_w)
            if system_w == 'bat':
                target = innings(system_c,user_c)
                print("The target is",target+1)
                result = innings(user_c,system_c,target=target+1)
                check(system_c,user_c,target,result)
                print("Game Finished...")
                break
            else:
                target=innings(user_c,system_c)
                print("The target is",target+1)
                result=innings(system_c,user_c,target=target+1)
                check(user_c,system_c,target,result)
                print("Game Finished...")
                break
        
    elif user.lower() == 'exit':
        print("Game Ended")
        break
    else:
        print("Enter Play or Exit")