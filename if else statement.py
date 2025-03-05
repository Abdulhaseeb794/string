a = 33
b = 200
if b > a:
    print("b is greater than a")

#If statement, without indentation (will raise an error):
a = 33
b = 200


if b > a:
    print("b is greater than a") # you will get an error

# elif    
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")    

# else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")      
else:
    print("a is greater than b")    

# another example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
     print("b is not greater than a")       

# Short Hand If
a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and  
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")

# or 
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
    print("at least one of the conditions is true")    

# not
# Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
    print("a is not greater than b")    

# Nested if
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20,")
    else:
        print("but not above 20.")    

# the pass statement
a = 33
b = 200
if b > a:
    pass   