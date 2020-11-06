''' This is a simple game called Mad lip , it ask a user for inputs then it arranges it into a story   '''
import time

#intializing game
print("What do you want your story to be about ")
time.sleep(1)

print(" Choose one \n 1. Hero  \n 2. Flower \n  ")

option =input("1 or 2  : ")
option = int(option)

if option==1:
    print("Wow you choose a Hero😄")
    time.sleep(1)
    print("Now tell us the name of your Hero")
    

elif option==2:
    print("Wow you choose a Flower🌻")
    print("Now tell us the name of your Flower")
else :
    print("Sorry choose the right Answer")
    


