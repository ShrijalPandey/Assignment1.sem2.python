'''
1.Create a diagram to show how python works. The diagram should show the components such as input, processing and output.
#Step 1: Input Data
user_input=input("Enter a number:")
#Step 2: Processing(Code)
try:
    number=int(user_input)
    square=number**2
    print("Square of",number, "is",square)
except ValueError:
    print("Error:Invalid input. Please enter a valid number")
#Step 3:Output Result

2.Write a program to input 2 numbers from the users and display the output of below mentioned operations in a proper format.
I.Addition
II.Subtraction
III.Multiplication
IV.Division
V.Modulo division
VI.Floor division

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulo_division = a % b
floor_division = a // b
print("")
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
print(f"Modulo Division: {a} % {b} = {modulo_division}")
print(f"Floor Division: {a} // {b} = {floor_division}")

3.Write a program to take a number input from the user and display whether the number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")

4.Write a program to take a number input from the user and display the result of some mathematical calculations as mentioned below.
I.Square of the number
II.Square root of the number
III.Exponent value with the number
IV.Log Base 10 of the number
V.Calculate the power 3, 4 and 5 of the number.

import math
num = float(input("Enter a number: "))

square = num ** 2
square_root = math.sqrt(num)
exponent = math.exp(num)
log_base_10 = math.log10(num)
power_3 = num ** 3
power_4 = num ** 4
power_5 = num ** 5

print("")
print(f"Square of {num}: {square}")
print(f"Square root of {num}: {square_root}")
print(f"Exponent value with {num}: {exponent}")
print(f"Log Base 10 of {num}: {log_base_10}")
print(f"Power 3 of {num}: {power_3}")
print(f"Power 4 of {num}: {power_4}")
print(f"Power 5 of {num}: {power_5}")

5.Solve the below mentioned expressions in a python program. Feel free to take input of the required variables to solve the expressions. 
I.a2 + 2ab + b2
II.a5 + 2abc + b3 + c4
III.a7 + 5a3b2c6 + b7

a=float(input('Enter the value of a:'))
b=float(input('Enter the value of b:'))
c=float(input('Enter the value of c:'))

ans1= a**2 + 2*a*b + b**2
ans2= a**5 + 2*a*b*c + b**3 + c**4
ans3= a**7 + 5*a**3*b**2*c**6 + b**7

print ('The answer of expression a2 + 2ab + b2 is',ans1)
print ('The answer of expression a5 + 2abc + b3 + c4 is',ans2)
print ('The answer of expression a7 + 5a3b2c6 + b7 is',ans3)

sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
percentage = (total / 500) * 100

if percentage >= 80:
    division = "Distinction"
elif percentage >= 60:
    division = "First Division"
elif percentage >= 50:
    division = "Second Division"
elif percentage >= 45:
    division = "Third Division"
else:
    division = "Fail Division"

print("Results:")
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
print("Division:", division)

6.Write a program to display the prime number between 2 numbers input by the users. Also print the sum of all the prime numbers.
[Hint: Prime numbers are the one which are either divisible by 1 or themselves. 3, 5, 7, 11, etc are some of the examples.]


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_sum = 0

print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            prime_sum += num

print("Sum of all prime numbers:", prime_sum)

7.Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers should be printed on the output screen. Also try the same program by replacing 2000 and 3200 by taking input for them from the users.

print("Numbers between 2000 and 3200 that are divisible by 7 but are not multiple of 5:")
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Numbers between {start} and {end} that are divisible by 7 but are not multiple of 5:")
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
        
8.Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers should be printed on the output screen. Also try the same program by replacing 2000 and 3200 by taking input for them from the users.         

print("Numbers between 2000 and 3200 that are divisible by 7 but are not multiple of 5:")
for num in range(2000,3200):
    if num % 7 == 0 and num % 5 !=0:
        print(num)
        
start =int(input("Enter the starting number:"))       
end =int(input("Enter the ending number:"))       

print(f"Numbers between {start} and {end} that are divisible by 7 but are not multiple of 5:")
for num in range(start,end+1):
    if num % 7 == 0 and num % 5 != 0:
        print(num)




9.Write a program to find the factorial of any number taken as an input from the user. Try to validate the user input whether it is a number or not and then only perform the operation.
In case of other than number as an input, display an error as “Not a number.”. [Hint: few available functions to identify the input is a number or not are ‘isdigit(), isnumeric(), etc.]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number_str = input("Enter a number to find its factorial: ")

    if number_str.isdigit():
        number = int(number_str)
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    else:
        print("Error: Not a number.")
main()

10.Write a program to find the sum of odd and even numbers input from the user. The program should take an input continuously until the user wants to exit the program. 
The program should be menu driven where the user should be asked whether they want to continue with the program or not.

def sum_of_numbers(num):
    #the sum of numbers in the list 
    return sum (num)
def sum_of_even_numbers(num):
    #the sum of the even numbers in the list 
    return sum(n for n in num if n % 2 == 0)
def sum_of_odd_numbers(num):
    return sum(n for n in num if n %2 !=0) 
#initialize empty list to store the numbers
num = []
while True:
    #get user input
    number = input("Enter a number ( or press 'q' to quit):")
    #check user mants to quit or not 
    if number == 'q':
        break 
    try:
        number = int (number)
    #add the numbers to the list num. append (number)
    except ValueError:
        print("not a number")
#sum of all number in display 
print(f"the sum of all the numbers is: {sum_of_numbers(num)}")
#sum of even numbers
print(f"the sum of all even number is: {sum_of_even_numbers(num)}")
#sum of odd numbers
print(f"the sum of all odd numbers is: {sum_of_odd_numbers(num)}")

11.Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
I.The program should generate a random number for the answer.
II.The program should prompt the user for a number input.
III.The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
IV.The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
V.If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.


import random
def number_guessing_game():
    #Generate a random number between 1 and 100
    answer = random. randint(1, 100)
    attempts = 0

    print("Welcone to the Nunber Guessing Game!")
    print("I've picked a randon number betneen 1 and 100. Can you guess it?")

    while attempts < 5:
        try:
            guess = int (input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
    
        if guess == answer:
            print("Congratulations! You guessed the correct number!")
            return
        elif guess < answer:
            print("Too Low. Try again.")
        else:
            print("Too high. Try again.")
        attempts += 1
    print("Sorry, youve run out of attempts. The correct number was {}.".format(answer))
    print("Game Over")
number_guessing_game()
'''