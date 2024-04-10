from questions import ques
import random
import os

print("\t\t\tWelcome to Python Quiz Master")

qlist = []
score = 0
name = input("Enter your name ::")

for n in range(1,8):
    os.system("cls")

    while True:
     qno = random.randint(1,10)
     if qno not in qlist:
         qlist.append(qno)
         break

    print("="*30)
    print()
    print("Question",n,')',ques[qno]['que'])
    print("\ta.",ques[qno]['a'])
    print("\tb.",ques[qno]['b'])
    print("\tc.",ques[qno]['c'])
    print("\td.",ques[qno]['d'])
    print()
    choice = input("Enter your answer (a/b/c/d) :: ")

    if choice == ques[qno]['ans']:
        score = score + 1
        print("\t\t\t Wrong Answer! Good Keep It up.")
    else:
        print("\t\t\t Wrong Answer!")
        print("\n\n Correct Answer is =>",ques[qno]['ans'])

    input("Press enter key to continue...")

os.system("cls")
print("\n\t\t\t QUIZ OVER")
print("------------------------------------------")

print("\n\t\t\t\t", name.upper(),", Your score is ", score)

if score <= 2:
    print("\t\t\t BETTER LUCK NEXT TIME")
elif score >= 3 and score <= 4:
    print("\t\t\t GOOD, NEED TO DO SOME MORE STUDY")
else:
 print("\t\t\t IT WAS OUTSTANDING. YOU ARE EXCELLENT")
 print("---------------------------------------------")
 print("\n\t\t\t\t Thanks")

 print("press enter key to exit")
