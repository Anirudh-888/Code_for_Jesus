count=0
upp=low=cons=0
with open("vc.txt","a+") as vcfile:
    txt=input("enter the text: ")
    for i in txt:
        if i in ["a","e","i","u","o"] or i in ["A","E","I","O","U"]:
            count+=1
        if i.isupper():
            upp+=1
        if i.islower():
            low+=1
        else:
            print("there is an error in input")
    print("The number of vowels:",count)
    print("The number of upper cases:",upp)
    print("The number of lower cases:",low)
    print("The number of consonants in the sentence:",len(txt)-count)