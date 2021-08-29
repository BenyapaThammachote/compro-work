def SV(SV):
    return (SV)
def AZ(AZ):
    return (AZ)
def SP(SP):
    return (SP)
def PZ(PZ):
    return (PZ)
def NN(NN):
    return (NN)
def ND(ND):
    return (ND)
def N(N):
    return (N)

First_Dose = input("First Dose:SV,AZ,SP,PZ,N:")
Second_Dose = input("Second Dose:SV,AZ,SP,PZ,N:")
Third_Dose = input("Third Dose:SV,AZ,SP,PZ,N:")

if (First_Dose == 'SV' and Second_Dose == 'SV' and Third_Dose == 'N'):
    print("You will get only 1 dose of Pfizer for 4th dose")
elif (First_Dose == 'SP' and Second_Dose == 'SP' and Third_Dose == 'N'):
    print("You will get only 1 dose of Pfizer for 4th dose")
elif (First_Dose == 'SV' and Second_Dose == 'N' and Third_Dose == 'N'):
    print("You will get only 1 dose of Pfizer for 4th dose")
elif (First_Dose == 'AZ' and Second_Dose == 'N' and Third_Dose == 'N'):
    print("You will get only 1 dose of Pfizer for 4th dose")
elif (First_Dose == 'SP' and Second_Dose == 'N' and Third_Dose == 'N'):
    print("You will get only 1 dose of Pfizer for 4th dose")
elif (First_Dose == 'SV' and Second_Dose == 'SV' and Third_Dose == 'AZ'):
    print("You can't get Pfizer for 4th dose")
elif (First_Dose == 'SV' and Second_Dose == 'AZ' and Third_Dose == 'N'):
    print("You can't get Pfizer for 4th dose")
elif (First_Dose == 'AZ' and Second_Dose == 'AZ' and Third_Dose == 'N'):
    print("You can't get Pfizer for 4th dose")
else:
    print("Please Enter more information below:")

Detected = input("Have you ever been detected in COVID-19?(YES/NO):")
if (Detected == "YES"):
        print("You will get only 1 dose of Pfizer")
elif (Detected == "NO"):
        print("You will get 2 doses of Pfizer")
else:
        print("Please contact Hospital")