import os,sys

class usermanager:
    def __init__(self, NAME, Age):
        self.NAME = NAME
        self.Age=Age
    
    def getname(self):
        return self.NAME
    
    def getage(self):
        return self.Age

def CalculateAgeInMonths(age_years):
        months = age_years*12
        return months

def printUser(user):
    print("User name is " + user.getname())
    print("User Age is " + str(user.getage()))

def UnusedFunction(x,y,z):
    result=x+y+z

def misSpelled_functn(x):
    return x*2

def Main():
    u = usermanager("Alice", 30)
    printUser(u)
    months = CalculateAgeInMonths(u.Age)
    print("Age in months:", months)
    print(misSpelled_functn(5))

Main()
