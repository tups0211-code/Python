# Rulebased AI Chatboat

import datetime
import time

currentHour = datetime.datetime.now().hour

name = input(" enter your name ")
if 5 <= currentHour <= 11:
    print("good morning ",name)
elif 11 <= currentHour <= 17:
    print("good afternoon",name)
elif 17<= currentHour <= 20 : 
    print("good eveninig ",name)
else:
    print("good night ",name)


print(" Welcome to your rule based chatbot")
print("you can ask basic questions, Type bye to exit")

responses = {
    "hello" : "Hi, How can i help you ? ",
    "how are you":"i am fine , what about you",
    "motivate me" :"keep going, every bug of your life makes you a better developer..!",
    "happy" : "Great to hear that ",
    "what is functions" : " In simple , Its a block of code"
}  

def getResponse(userQue):
     userQue = userQue.lower()

     for eachkey in responses : 
          if eachkey in userQue:
             return responses[eachkey]
    
     return " I am not able to tell that yet ask me later"
 
while True:
     UserInput = input("Ask your questions : ")
     reply = getResponse(UserInput)
     print(" Response : ", reply)

     if "bye" in UserInput.lower():
        break
