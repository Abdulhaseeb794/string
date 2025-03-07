# Print each fruit in a fruit list:
fruits = ["aaple", "banana", "cherry"]
for x in fruits:
    print(x)

print()

# print each letter in the word "banana":
for x in "banana":
    print(x)    

print()

# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break    

print()

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
     if x == "banana":
      break  
     print(x)

print()

# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
     if x == "banana":
         continue
     print(x)     

print()

# using the range() funtion
for x in range (6):
    print(x)

print()

# using the start parameter
for x in range (2,6):
    print(x)

print()

# increment the sequence with 3 (default is 1)
for x in range (2, 30, 3):
    print(x)    

print()

# else in for loop
for x in range (6):
    print(x)
else:
    print("Finally finished!")    

print()

# another example
for x in range (6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")    

print()

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)