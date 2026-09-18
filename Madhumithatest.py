str1="Jesus, Madhu,STC,dancing team"
print(str1[0:5])
print(str1[7:12])
print(str1[13:16])
print(str1[17:29])

#11/9/26
str="DEeKsha"
capital=str.upper()
lower=capital.lower()
title=lower.title()
print(str)
print(capital)
print(lower)
print(title)

#17/9/26
str="abcdefghijklmnopqrstuvwsyz"
print(str.upper())
def voweltostar (name):
    for i in name:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            i="*"
        print(i,end="")    
voweltostar("abcdefghijklmnopqrstuvwsyz")   