name_of_user=input("Enter your name:")
mood=input("How are you feeling today? happy/sad/tired/stressed/excited:")
if mood=="happy":
    print("Try to be like this")
elif mood=="sad":
    print("Find out the reason why and solve the issue")
elif mood=="tired":
    print("Take a Break")
elif mood=="stressed":
    print("Try to sleep and calm down")
elif mood=="excited":
    print("Do something Productive")
else:
    print("Go ahead with your day")

import datetime
today = datetime.datetime.now()
