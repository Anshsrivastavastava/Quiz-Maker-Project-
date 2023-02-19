import time
import json
import sys

class Quiz:
    def __init__(self):
        self.Easy_Question = {}
        self.Medium_Question = {}
        self.Hard_Question = {}
        self.Easy_len = len(self.Easy_Question)+1
        self.Medium_len = len(self.Medium_Question)+1
        self.Hard_len = len(self.Hard_Question)+1
        self.Login_details = {}

    def login(self,Email,Password):
        with open("Login_Details.json","r") as f:
            temp = json.load(f)
        if Email != temp["Email"]:
            return "Don't Have an Account\nSignin First"
        if Password != temp["Password"]:
            print("Invalid Password ")
        else:
            print("Login Successfully")
        return ""
    
    
    def signing(self):
        name = input("Enter Your Name Here :")
        age = input("Enter Your Age Here :")
        gender = input("Enter Your Gender Here :")
        email = input("Enter Your Email Id Here :")
        password = input("Enter Your Password Here :")
        self.Login_details ={"Name":name,"Age":age,
                            "Gender":gender,"Email":email,
                            "Password":password }
        with open("Login_Details.json","w") as f:
            json.dump(self.Login_details,f,indent=4)
        print()
        print("Your Email Id and Password is \n Your Login ID and Password")
        time.sleep(2)
        return "Your Sign Got Create"
    
    def Add_Question(self):
        email = input("Enter Your Login ID here :")
        with open("Login_Details.json","r") as f:
            temp = json.load(f)
        if email != temp["Email"]:
            print("For Adding Question Your Need To Login First")
            return ""
        else:
            while True:
                print("---------------------------->>>>>>>Add New Quiz<<<<------------------------------\n")
                print("Prsee E for Easy Level Question ")
                print("Press M for Medium level Question")
                print("Press H for Hard Level Question ")
                level = input("Enter Which Question You Want to Add :")
                if level == "E" or level =="e":
                    nos_of_quiz = int(input("Enter How Many Quiz You Want to Add :"))
                    for i in range(nos_of_quiz):
                        qustion = input("Enter Your Question Here :")
                        option1 = input("Enter Your First Option :")
                        option2 = input("Enter Your Second Option :")
                        option3 = input("Enter Your Third Option Here :")
                        option4 = input("Enter Your Fourth Option :")
                        correct_option = input("Enter Your Correct Option Here :")
                        print()
                        d = {"Question":qustion,"A":option1,"B":option2,"C":option3,"D":option4,"Correct Option":correct_option}
                        self.Easy_Question[self.Easy_len]=d
                        self.Easy_len = len(self.Easy_Question)+1
                    with open("Easy_Level_Question.json",'w') as f:
                        json.dump(self.Easy_Question,f,indent=4)
                    return "Your Question Got Create"
                
                if level == "M" or level =="m":
                    nos_of_quiz = int(input("Enter How Many Quiz You Want to Add :"))
                    for i in range(nos_of_quiz):
                        qustion = input("Enter Your Question Here :")
                        option1 = input("Enter Your First Option :")
                        option2 = input("Enter Your Second Option :")
                        option3 = input("Enter Your Third Option Here :")
                        option4 = input("Enter Your Fourth Option :")
                        correct_option = input("Enter Your Correct Option Here :")
                        print()
                        d = {"Question":qustion,"A":option1,"B":option2,"C":option3,"D":option4,"Correct Option":correct_option}
                        self.Medium_Question[self.Medium_len]=d
                        self.Medium_len = len(self.Medium_Question)+1
                    with open("Medium_Level_Question.json",'w') as f:
                        json.dump(self.Medium_Question,f,indent=4)
                    return "Your Question Got Create"
                
                if level == "H" or level =="h":
                    nos_of_quiz = int(input("Enter How Many Quiz You Want to Add :"))
                    for i in range(nos_of_quiz):
                        qustion = input("Enter Your Question Here :")
                        option1 = input("Enter Your First Option :")
                        option2 = input("Enter Your Second Option :")
                        option3 = input("Enter Your Third Option Here :")
                        option4 = input("Enter Your Fourth Option :")
                        correct_option = input("Enter Your Correct Option Here :")
                        print()
                        d = {"Question":qustion,"A":option1,"B":option2,"C":option3,"D":option4,"Correct Option":correct_option}
                        self.Hard_Question[self.Hard_len]=d
                        self.Hard_len = len(self.Hard_Question)+1
                    with open("Medium_Level_Question.json",'w') as f:
                        json.dump(self.Hard_Question,f,indent=4)
                    return "Your Question Got Create"


    def Play_Question(self):
        score = 0
        while True:
            print("==============================================Play==================================\n")
            print('*'*55)
            print("Press E for Easy Question ")
            print("Press M for Medium Question")
            print("Press H for Hard Question")
            print('*'*55)
            inp = input("Choose Diffculty Level :")
            if inp =="e" or inp =="E":
                with open("Easy_Level_Question.json","r") as f:
                    temp = json.load(f)
                for i in temp.keys():
                    print([i],temp[i]["Question"],"\n")
                    print("(1)",temp[i]["A"],"                                                   ",'(2)',temp[i]['B'])
                    print("(3)",temp[i]["C"],"                                                   ",'(4)',temp[i]['D'])
                    ans = input("Choose Your Correct Option :")
                    print()
                    if ans ==temp[i]["Correct Option"]:
                        score +=1
                    else:
                        print()
                        print("Wrong Answer")
                        print("Correct Answer is :",temp[i]["Correct Option"])
                print("*******************************************")
                print(f"You Have Scored {score}")
                return ""
        
            elif inp=="m" or inp =="M":
                with open("Medium_Level_Question.json","r") as f:
                    temp = json.load(f)
                for i in temp.keys():
                    print([i],temp[i]["Question"],"\n")
                    print("(1)",temp[i]["A"],"                                                   ",'(2)',temp[i]['B'])
                    print("(3)",temp[i]["C"],"                                                   ",'(4)',temp[i]['D'])
                    ans = input("Choose Your Correct Option :")
                    print()
                    if ans ==temp[i]["Correct Option"]:
                        score +=1
                    else:
                        print()
                        print("Wrong Answer")
                        print("Correct Answer is :",temp[i]["Correct Option"])
                print("*******************************************")
                print(f"You Have Scored {score}")
                return ""

            elif inp=="h" or inp =="H":
                with open("Hard_Level_Question.json","r") as f:
                    temp = json.load(f)
                for i in temp.keys():
                    print([i],temp[i]["Question"],"\n")
                    print("(1)",temp[i]["A"],"                                                   ",'(2)',temp[i]['B'])
                    print("(3)",temp[i]["C"],"                                                   ",'(4)',temp[i]['D'])
                    ans = input("Choose Your Correct Option :")
                    print()
                    if ans ==temp[i]["Correct Option"]:
                        score +=1
                    else:
                        print()
                        print("Wrong Answer")
                        print("Correct Answer is :",temp[i]["Correct Option"])
                print("*******************************************")
                print(f"You Have Scored {score}")
                return ""

    def logout(self):
        sys.exit()

    def intruction(self):
        print("------------------------>>>>INSTRUCTIONS \n")
        time.sleep(2)
        print(" {1}click on 'Play Quiz' button\n","{2}For each of the questions you have four possible answers")
        print(" {3}fill your correct option you think is right\n","{4}Continue until you have answered all of the questions")  
        print(" {5}Press 1 , 2 ,3 or 4 in your correct options ")

            
