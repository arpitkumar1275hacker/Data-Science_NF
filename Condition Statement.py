# Write a program to check whether a year is a leap year or not

year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# Write a program to find the largest among three numbers using nested conditional statements

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b > c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")



# Write a program to check character type

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")



# Write a program to calculate electricity bill using different unit slabs

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)

else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

print("Electricity Bill: ₹", bill)

# Write a program to determine the type of triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")

# Write a program to create a simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not possible")

else:
    print("Invalid operator")

# Write a program to calculate income tax according to salary ranges

salary = float(input("Enter annual salary: "))

if salary <= 250000:
    tax = 0

elif salary <= 500000:
    tax = salary * 0.05

elif salary <= 1000000:
    tax = salary * 0.20

else:
    tax = salary * 0.30

print("Income Tax = ₹", tax)



# Write a program to check login authentication

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")



# Write a program to determine the position of a point

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point lies in First Quadrant")

elif x < 0 and y > 0:
    print("Point lies in Second Quadrant")

elif x < 0 and y < 0:
    print("Point lies in Third Quadrant")

elif x > 0 and y < 0:
    print("Point lies in Fourth Quadrant")

elif x == 0 and y == 0:
    print("Point is at Origin")

else:
    print("Point lies on Axis")



# Write a program to assign grades based on marks

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A+")
    print("Distinction")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F (Fail)")
