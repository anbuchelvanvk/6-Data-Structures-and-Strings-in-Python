student={'Ram':90,'Sam':80,'Alice':85}
name=input("Enter the student's name : ")
a=student.get(name)
if a==None:
    print("Student not found")
else:
    print(name,"'s Mark is : ",student[name])
