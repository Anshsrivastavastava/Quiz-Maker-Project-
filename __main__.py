print()
import time
from Quizer import *
from datetime import datetime
print("Date :-",datetime.now(),
      "\n@aurthor :-","Ansh Srivastav")

demo1 = Quiz()
print("----------------------------------------------------->>>>>>>>Welcome to Python Quizes<<<<<<<<<<----------------------------------------------------\n")

while True:
    print("+="*55)
    print('1. PLAY QUIZ')
    print('2. LOGIN PANEL')
    print('3. CREATE AN ACCOUNT')
    print('4. ADD QUIZ QUESTIONS')
    print('5. LOGOUT PANEL')
    print('6. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
    print('7. EXIT')
    print("+="*55)
    choise = input("Enter Your Choise Here :")

    if choise =="1":
        demo1.Play_Question()
        
    
    if choise =="2":
        email = input("Enter Your Mail Here :")
        passw = input("Enter Your Password Here :")
        demo1.login(email,passw)
    
    if choise =="3":
        demo1.signing()
    
    if choise =="4":
        demo1.Add_Question()
        break
    
    if choise =="5":
        demo1.logout()

    if choise =="6":
        demo1.intruction()
        
    
    if choise=="7":
        print("------------------------>>>>>Thanks For Joining the Quiz <<<<<----------------------\n")
        sys.exit()
    



