str= "sanjana"
print(str[0:5])
print(str[1:4])
print(str[2:3])
# slicing of strings
#The date of the test is 10/09/2026

str="sAnJaNa"
capital=str.upper()
title=capital.title()
lower=title.lower()
print(str)
print(capital)
print(title)
print(lower)
#stringfunctions
#The date of the test is 11/09/2026 
# It is correct from Anirudh mentor 3p

def star(name):
    for i in name:
        if i=="a"or i=="e"or i=="i"or i=="o"or i=="u":
            i="..•"
        print(i,end=" ")    
star("sanjana")
def ulta():
    str=input("enter your name")
    for i in range(-1,-len(str)-1,-1):
        print(str[i],end="")
ulta()
str="sanjana"
u=str.upper()
l=str.lower()
isu=str.isupper()
isl=str.islower()
print(u)
print(l)
print(isu)
print(isl)
#the date of test is 17/09/26

str=input("enter your sentence")
char=input("enter the character you want to count")
print(str.count(char))

def reverse():
    str=input("enter your name")
    for i in range(-1,-len(str)-1,-1):
        print(str[i],end=" ")
reverse()
def hypen(str):
    for i in str:
        if i==" ":
            i="-"
        print(i,end="")    
hypen("Jesus is lord")

str=input("enter the sentence")
count=0
for i in str:
    if i in "aeiouAEIOU":
        count+=1
    else:
        count+=0    
print(count)    

#date of test 18/9/2026