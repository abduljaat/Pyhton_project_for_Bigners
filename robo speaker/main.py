import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("WELCOME TO ROBO SPEAKER CREATED BY ABDUL RAHMAN")
    
    while True:
        a = input("Enter what you want to speak: ")
        if a.lower() == "exit":
            engine.say("Bye Bye Friend")
            engine.runAndWait()
            print("Bye Bye Friend")
            break
        engine.say(a)
        engine.runAndWait()




       # ****** This code is for os system *******
       
# import os

# if __name__=="__main__":
#     print("WELLCOME TO ROBO SPEAKR CREATED BY ABDUL RAHMAN")
    
#     while True:
#         a=input("Enter what you want to speak: ")
#         if a=="exit":
#             os.system("Bye Bye Friend: ")
#             break
#         command=f"say{a}"
#         os.system(command)