# Program to find sum of first 10 natural numbers

sum = 0

for i in range(1, 11):
    sum += i

print("Sum =", sum)

# Program to find factorial of a number

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

# Program to print Fibonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Program to find largest among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number =", a)

elif b >= a and b >= c:
    print("Largest number =", b)

else:
    print("Largest number =", c)

# Student Result System

# Input student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")

# Input marks
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
