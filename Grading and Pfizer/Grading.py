student_name=input("Enter student name:")
score=float(input("Enter your score:"))

if (score>=80 and score<=100 ):
    print("Your score is A", "which mean Excellent!")
elif (score>=75 and score<=79):
    print("Your score is B+", "which mean Very Good!" )
elif (score>=70 and score<=74):
    print("Your score is B", "which mean Good!")
elif (score>=65 and score<=69):
    print("Your score is C+", "which mean Faily Good!")
elif (score>=60 and score<=64):
    print("Your score is C", "which mean Fair!")
elif (score>=55 and score<=59):
    print("Your score is D+", "which mean Poor!")
elif (score>=50 and score<=54):
    print("Your score is D", "which mean Very Poor!")
elif (score>=0 and score<=49):
    print("Your score is F", "which mean you Fail!", "PLease try hard next time")
else:
    print("Please contact registry office")