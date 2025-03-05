# Check if a number is positive, negative, or zero
num = float(input("enter a number:"))
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("zero")        

# another example
age = int(input("enter your age:"))
if age >= 18:
    print("you are eligible to cast a vote")
else:
    print("you are not eligible to cast a vote")     

# another example
marks = int(input("enter your marks:"))
if marks >= 90:
    print("grade A")
elif marks >= 80:
    print("grade B")        
elif marks >=70:
    print("grade c")
elif marks >= 60:
    print("grade D")
else:
    print("fail")           

