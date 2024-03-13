#grading system
maths = float(input("Enter your maths score: "))
eng = float(input("Enter your english score: "))
chem = float(input("Enter your chemistry score: "))
grade = (maths + eng +chem)/3

if grade >=70 and grade <=100:
    print("Your grade is A of marks: ", grade)

elif grade >=60 and grade <=69:
    print("Your grade is B of marks: ", grade)

elif grade >=50 and grade <=59:
    print("Your grade is C of marks: ", grade)    

elif grade >=40 and grade <=49:
    print("Your grade is D of marks: ", grade)

elif grade >=0 and grade <=39:
    print("Fail!!: ", grade)    

else:
    print("Invalid marks!!")    