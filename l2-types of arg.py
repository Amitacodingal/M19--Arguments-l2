#act1
def total_cal(bill,tip):
  total=bill*(1+0.01*tip)
  total=round(total,2)
  print(f"Please pay ${total}")

total_cal(150,20)


#act 2
#define function to calculate cube
def cube(number):
    return number*number*number

#calling function
print(cube(3))

#define a function which will execute cube function if the user entered number is divisible by 3
def div_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
#display result
print(div_three(9))
print (div_three(4) )





#act3
# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Input from user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
    
    
#act4
# Program to add and subtract two numbers

# Store the two numbers

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

# Add the two numbers

sum = num1 + num2

# Subtract the two numbers

difference = num1 - num2

# Print the result

print("The sum of the two numbers is:", sum)

print("The difference of the two numbers is:", difference)

#act5

#Program to create a dictionary which stores names of the employee
#and their salary
num = int(input("Enter the number of employees whose data to be stored: "))
count = 1
employee = dict() #create an empty dictionary
while count <= num:
 name = input("Enter the name of the Employee: ")
 salary = int(input("Enter the salary: "))
 employee[name] = salary
 count += 1
print("\n\nEMPLOYEE_NAME\tSALARY")
for k in employee:
 print(k,'\t\t',employee[k])

