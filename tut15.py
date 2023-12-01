# Good moring sir programme

a = int(input("Enter your time here (in 24hours format) - "))
if (a >= 0 and a <= 5):
    print("Hey User I request you to sleep Its Midnight")
elif (a >= 6 and a<=8 ):
    print("Hey User Its time to wake up Its already morning")
elif (a>=9 and a<=12):
    print("Hey User Its already Late to go for work Wake up get ready ")
elif (a>=13 and a<=17):
    print("Hey User its Afternoon Its time to complete your work")
elif (a>=18 and a<=20 ):
    print("Hey User Its Evening you should go for walk")
elif (a>=21 and a<=22):
    print("Hey user Its time to complete the dinner ")
elif (a>=23 and a<=24):
    print("Hey User Its Time to sleep you should sleep")
else:
    print("Sorry User This is not in 24 hours format please try it again")



