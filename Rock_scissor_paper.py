import random

while True:
    user_guess=input("""Choose your option 
          1.Press 1 for Rock
          2.Press 2 for Paper 
          3.Press 3 for Scissor """)
    sys_guess=str(random.randint(1,3))
    if user_guess==sys_guess:
        print("Draw \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="1" and sys_guess=="2":
        print("You loss \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="1" and sys_guess=="3":
        print("You Win \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="2" and sys_guess=="1":
        print("You Win \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="2" and sys_guess=="3":
        print("You loss \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="3" and sys_guess=="1":
        print("You loss \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    elif user_guess=="3" and sys_guess=="2":    
        print("You Win \n You Choose {} and System Choose {}".format(user_guess,sys_guess))
    else:
        print("You choose wrong option ")

