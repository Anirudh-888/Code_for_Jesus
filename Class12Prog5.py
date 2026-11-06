count=1
with open ("prog5.txt","a+") as prog5:
    prog5.seek(0)
    content=prog5.read()
    sentence=input("Enter the sentence for the prog5")
    prog5.write(sentence)
    print("The number of sentences in the document is",len(prog5.readline())+1)
    for word in sentence:
        if word==" ":
            count+=1
    print("The number of words in the document is",count)
    print("The number of characters in the document is",len(sentence))