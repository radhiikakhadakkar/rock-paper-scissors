import random #get access to random module

def choose_option_for_user():
    print("inside select_option... ") #check the execution
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock" , "rock"]:
        user_choice = "Rock"
    elif user_choice in ["Paper" , "paper"]:
        user_choice = "Paper"
    elif user_choice in ["Scissors" , "scissors"]:
        user_choice = "Scissors"

    else:
        print("Sorryy! Try Again!")
        choose_option()

    return user_choice #return value to the function
       
def computer_select():
    print("inside computer_option... ") #check the execution
    computer_choice = random.randint(1,3)#random.randint selects the value between the given range 
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    elif computer_choice == 3:
        computer_choice= "Scissors"

    return computer_choice

# initializinng the score of both the players to 0
user_wins= 0
cpu_wins =0


while True:  
    user_choice = choose_option_for_user()
    print("user choise is"+user_choice)#check the execution
    computer_choice= computer_select()
    print("computer choise is"+computer_choice)
    

    if user_choice== "Rock":
        print("inside 1st if... ")#check the execution
        if computer_choice == "Rock":
            print("")
            print( " **Its a Tie!  Both chose Rock**")
            print("")
            user_wins +=1
            cpu_wins +=1 #both will get a point

        elif computer_choice == "Scissors":
            print(" **Hurrayy you win ! Computer chose scissors**")
            print("")
            user_wins +=1
        elif computer_choice == "Paper":
            print( " **Oops! Computer wins You lose Computer chose paper**")
            priny("")
            cpu_wins +=1

    elif user_choice == "Paper":
        print("inside 2nd if... ")#check the execution
        if computer_choice == "Rock":
            print("")
            print(" **Hurrayy you win ! Computer chose rock**")
            print("")
            user_wins +=1
        elif computer_choice =="Paper":
            print("**Its a Tie!**")
        elif computer_choice == "Scissors":
            print( " **Oops! Computer wins You lose computer chose scissors**")
            cpu_wins +=1

    elif user_choice =="Scissors":
        print("inside 3rd if... ")#check the execution
        if computer_choice == "Rock":
            print("")
            print(" **Oops! Computer wins You lose computer chose rock**")
            cpu_wins +=1
        elif computer_choice== "Paper":
            print(" **Hurrayy you win ! Computer chose paper**")
            user_wins +=1
        elif computer_choice =="Scissors":
            print("**Its a Tie!**")


    print("User wins : " + str(user_wins))
    print("Cpu wins : " + str(cpu_wins))

    user_choice = input(" Want to Play Again? (yes/no)")
    if user_choice in ["yes" , "Yes"]:
        pass
    elif user_choice in ["No" ," no"]:
        break
    else:
        break
