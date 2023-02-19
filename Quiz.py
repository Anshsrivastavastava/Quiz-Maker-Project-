import json
import sys

class Quiz:

    def __init__(self):
        self.user = {}
        self.Easy_Question = {}
        self.Medium_Question = {}
        self.Hard_Question = {}
        self.len_easy = len(self.Easy_Question)+1
        self.len_medi = len(self.Medium_Question)+1
        self.len_hard = len(self.Hard_Question)+1
    
    def singin(self):
        print("===================================Create an Account=====================================")
        Name = input("Enter Your Name :")
        Email = input("Enter Your Mail ID :")
        Password = input("Enter Your Password :")
        self.user["Name"] = Name
        self.user["Email"] = Email
        self.user["Password"] = Password

        with open("user_details.json","w") as f:
            json.dump(self.user,f,indent=4)
        print("Your Sign Got Create")
    
    def login(self):
        with open("user_details.json","r") as f:
            temp = json.load(f)        
        Email = input("Enter Your Mail ID:")
        if Email != temp["Email"]:
            print("Your Are not Our Existing Coustoms")
        else:
            while True:
                password = input("Enter Your Password :")
                if password != temp["Password"]:
                    print("Incorrect Password Login Again")
                    
                else:
                    print("Login Sucessfully")
                    break
    
    def add_question(self):
        with open("user_details.json","r") as f:
            temp = json.load(f)
        if temp["Email"] == "":
            print("+="*55)
            return "You are not Admin Coustomer You Have to Login First"
        else:
            while True:
                print("+="*55)
                print("Press E for Easy Question")
                print("Press M for Medium Question")
                print("Press H for Hard Question")
                print("+="*55)
                level = input("Enter Your Level :")
                
                if level == "E" or level =="e":
                    while True:
                        print("Press 0 for Exit")
                        print("Enter Any Key")
                        key = input("-->>")
                        
                        if key != "0":
                            Ques = input("Enter Your Question :")
                            opion1 = input("Enter Your First Options :")
                            option2 = input("Enter Your Second Options :")
                            option3 = input("Enter Your Third Option")
                            option4 = input("Enter Your Fourth Options :")
                            correct_option = input("Enter Your Correct Option :")
                            self.d = {"Question":Ques,"a":opion1,"b":option2,"c":option3,"d":option4,"Correct Option":correct_option}
                            self.Easy_Question[self.len_easy] = self.d
                            self.len_easy = len(self.Easy_Question)+1
                            with open('Easy_Question.json','w') as f:
                                json.dump(self.Easy_Question,f,indent=4)
                        
                        else:
                            print("Your Question Got Create")
                            break
                
                if level == "M" or level =="m":
                    while True:
                        print("Press 0 for Exit")
                        print("Enter Any Key")
                        key = input("-->>")
                        
                        if key != "0":
                            Ques = input("Enter Your Question :")
                            opion1 = input("Enter Your First Options :")
                            option2 = input("Enter Your Second Options :")
                            option3 = input("Enter Your Third Option :")
                            option4 = input("Enter Your Fourth Options :")
                            correct_option = input("Enter Your Correct Options :")
                            self.d = {"Question":Ques,"a":opion1,"b":option2,"c":option3,"d":option4,"Correct Option":correct_option}
                            self.Medium_Question[self.len_medi] = self.d
                            self.len_medi = len(self.Medium_Question)+1
                            with open('Medium_Question.json','w') as f:
                                json.dump(self.Medium_Question,f,indent=4)
                        
                        else:
                            print("Your Question Got Create")
                            break

                if level == "H" or level =="h":
                    while True:
                        print("Press 0 for Exit")
                        print("Enter Any Key")
                        key = input("-->>")
                        
                        if key != "0":
                            Ques = input("Enter Your Question :")
                            opion1 = input("Enter Your First Options :")
                            option2 = input("Enter Your Second Options :")
                            option3 = input("Enter Your Third Option")
                            option4 = input("Enter Your Fourth Options :")
                            correct_option = input("Enter Your Correct Options :")
                            self.d = {"Question":Ques,"a":opion1,"b":option2,"c":option3,"d":option4,"Correct Option":correct_option}
                            self.Hard_Question[self.len_hard] = self.d
                            self.len_medium = len(self.Hard_Question)+1
                            with open('Medium_Question.json','w') as f:
                                json.dump(self.Hard_Question,f,indent=4)
                        
                        else:
                            print("Your Question Got Create")
                            break
                sys.exit()

    def test_taker(self):
        while True:
            print("*"*55)
            print("Press E for Easy Level Question")
            print("Press M For Medium Level Question")
            print("Press H for Hard Level Question")
            print("*"*55)
            diff_level = input("Please Select Your Level :")
            if diff_level == "E" or diff_level == "e":
                with open('Easy_Question.json',"r") as f:
                    temp = json.load(f)
                score = 0
                for i in temp.keys():
                    while temp.keys()!= None:
                        print("========================================================Let's Play ==================================================\n")
                        print(temp[i]["Question"])
                        print(1,temp[i]["a"],"                                                          " ,2,temp[i]["b"])
                        print(3,temp[i]["c"],"                                                          " ,4,temp[i]["d"])
                        print()
                        option = input("Choose Your Option :-")
                        if option == temp[i]["Correct Option"]:
                            print("--------->>>>>You Are Correct<<<<<---------------")
                            score +=1
                        else:
                            print("You Are Wrong")
                            print("Correct Answer is :-",temp[i]["Correct Option"])
                        break    
                print("Your Final Score is ",score)
                return ""
            
            if diff_level == "M" or diff_level == "m":
                with open('Medium_Question.json',"r") as f:
                    temp = json.load(f)
                score = 0
                for i in temp.keys():
                    while temp.keys()!= None:
                        print("========================================================Let's Play ==================================================\n")
                        print(temp[i]["Question"])
                        print(1,temp[i]["a"],"                                                          " ,2,temp[i]["b"])
                        print(3,temp[i]["c"],"                                                          " ,4,temp[i]["d"])
                        print()
                        option = input("Choose Your Option :-")
                        if option == temp[i]["Correct Option"]:
                            print("--------->>>>>You Are Correct<<<<<---------------")
                            score +=1
                        else:
                            print("You Are Wrong")
                            print("Correct Answer is :-",temp[i]["Correct Option"])
                        break
                print("Your Final Score is ",score)
                return ""
                              
            if diff_level == "M" or diff_level == "m":
                with open('Hard_Question.json',"r") as f:
                    temp = json.load(f)
                score = 0
                for i in temp.keys():
                    while temp.keys()!= None:
                        print("========================================================Let's Play ==================================================\n")
                        print(temp[i]["Question"])
                        print(1,temp[i]["a"],"                                                          " ,2,temp[i]["b"])
                        print(3,temp[i]["c"],"                                                          " ,4,temp[i]["d"])
                        print()
                        option = input("Choose Your Option :-")
                        if option == temp[i]["Correct Option"]:
                            print("--------->>>>>You Are Correct<<<<<---------------")
                            score +=1
                        else:
                            print("You Are Wrong")
                            print("Correct Answer is :-",temp[i]["Correct Option"])
                    break

                print("Your Final Score is ",score)
                return ""

    def log_out(self):
        with open("user_details.json","r") as f:
            self.l = json.load(f)
        self.l["Name"]=""
        self.l["Email"]=""
        self.l["Password"]=""
        with open("user_details.json","w") as f:
            json.dump(self.l,f)
        print("Logout Sucessfully")

demo1 = Quiz()


while True:
    print("=+"*60)
    print("                            Welcome to Quiz Play                                ")
    print("=+"*60)
    print("---------------------------------------------------------")
    print('1. PLAY QUIZ')
    print('2. ADD QUIZ QUESTIONS')
    print('3. CREATE AN ACCOUNT')
    print('4. LOGIN PANEL')
    print('5. LOGOUT PANEL')
    print('6. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
    print('7. EXIT')
    print("---------------------------------------------------------")
    choice = int(input('ENTER YOUR CHOICE: '))
    if choice == 1:
        demo1.test_taker()
    
    if choice ==2:
        demo1.add_question()
    
    if choice ==3:
        demo1.singin()
    
    if choice ==4:
        demo1.login()
    
    if choice ==5:
        demo1.logout()
    
    if choice ==7:
        sys.exit()
            










