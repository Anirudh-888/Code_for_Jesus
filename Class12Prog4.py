vow=0
cons=0
upp=0
low=0
with open("prog4.txt","a+") as prog4:
    sentence=input("Enter the sentence for prog4")
    prog4.write(sentence)#One of the common mistakes done
    content=prog4.read()
    for i in sentence:
        if i in ["a","e","i","o","u"] or i in ["A","E","I","O","U"]:
            vow+=1
        if i.isupper() is True:
            upp+=1
        if i.islower() is True:
            low+=1
        #Don't use elif loop as these are three sepearate 
print("The number of vowels in the file is",vow)
print("The number of consonants in the file is",len(sentence)-vow)
print("The number of uppper case letters",upp)
print("The number of lower case letters ",low)
#Don't use content in the len function since the file is not created it will give the lenght as 0
#Don't use range in the for loop

        
        
