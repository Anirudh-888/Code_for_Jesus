# Python code: If marks is greater than 90 copy it to other file
with open("prog7b.txt","a+") as prog7b:
    prog7b.seek(0)
    content1=prog7b.read()
with open("prog7a.txt","a+") as prog7a:
    prog7a.seek(0)
    content=prog7a.read()
    no=int(input("Enter the number of students you want to enter the marks"))
    for i in range(no):
        name=input("Enter the name")
        percentage=float(input(f"Enter the percentage of {name}"))
        data=(f"The student {name} has got {percentage} percentage")
        prog7a.write(data)
        prog7b.open()
        if percentage>=90:
            prog7b.write(data)
topperlist=prog7b.read()
print("Topper list")
            

