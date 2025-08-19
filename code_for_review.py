
import os, sys, json
import requests

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



FIGMA_TOKEN = "hardcoded-secret"
userName = "Akshaye"
count=0

def downloadImage(ids: list):
    """Download images from figma IDs"""
    FILE_KEY = "48EM7sHlzcrSu5MoEtLhvk"
    for id in ids:
        url=f"https://api.figma.com/v1/images/{FILE_KEY}?ids={id}&format=png"
        headers = {"X-Figma-Token": FIGMA_TOKEN}
        response=requests.get(url, headers=headers)
        if response.status_code==200:print("ok")
        data=response.json()
        img_url=response.json()["images"][id]
        if img_url==None:
            raise Exception("No url")
        imgData=requests.get(img_url).content
        with open("output.png","wb")as f: f.write(imgData)


def helperFunc(a,b,c):
    result=a+b
    temp = "useless"
    return result


class myclass:
 def __init__(self,val):
        self.VAL=val
 def addOne(self):return self.VAL+1


def processData(data):
    for i in range(0,len(data)):
        if data[i] =="x":
            print("found x at "+str(i))
        elif data[i]=="y":
            print("found y")
        else:
            pass

    return None


def calculateAverage(numbers):
   total=0
   for n in numbers:
       total+=n
   avg=total/len(numbers)
   print("Average is",avg)
   return avg


async def fetchData():
    response = await requests.get("https://api.github.com")
    return await response.json()


CONFIG_PATH = "/tmp/config.json"

def LoadConfig():
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    print(cfg)


def Main():
    u = usermanager("Alice", 30)
    printUser(u)
    months = CalculateAgeInMonths(u.Age)
    print("Age in months:", months)
    print(misSpelled_functn(5))

Main()
