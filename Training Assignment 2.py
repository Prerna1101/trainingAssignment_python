# Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included).
answer = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        answer.append(i)
print(answer)


# Question 2
# Write a program which can compute the factorial of a given numbers.
number = int(input("Enter a number to calculate its factorial: "))    
factorial = 1    
if number < 0:    
   print(" Factorial does not exist for negative numbers")    
elif number == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,number + 1):    
       factorial = factorial*i    
   print(factorial)


# Question 3:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an 
# integral number between 1 and n (both included). and then the program should print the dictionary.
# Take User Input of Number
n = int(input("Enter n: "))
squares = {i : i*i for i in range(1, n+1)}
print(squares)


# Question 4:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
# which contains every number.
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('The resulting Tuple is : ',tuple)


# Question 5:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
class StringModifier:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

def test_string_modifier():
    string_modifier = StringModifier()
    string_modifier.getString()
    string_modifier.printString()

if __name__ == "__main__":
    test_string_modifier()


# Question 6:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
import math

def calculate_Q(D):
    C = 50
    H = 30
    Q = int(math.sqrt((2 * C * D) / H))
    return Q

def main():
    input_sequence = input("Enter the values of D (comma-separated sequence): ")
    D_values = input_sequence.split(",")

    try:
        D_values = [float(D) for D in D_values]
        results = [calculate_Q(D) for D in D_values]

        print("Results:")
        for i, D in enumerate(D_values):
            print(f"Q({D}) = {results[i]}")

    except ValueError:
        print("Error: Invalid input. Make sure to enter valid numerical values separated by commas.")

if __name__ == "__main__":
    main()


# Question 7:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
rows = int(input("Enter number of rows: "))
cols= int(input("Enter number of columns: "))
multi_list = [[0 for col in range(cols)] for row in range(rows)]

for row in range(rows):
    for col in range(cols):
        multi_list[row][col]= row*col

print(multi_list)


# Question 8:
# Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.
phrase = input("Enter comma seperated words: ")
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))


# Question 9:
# Write a program that accepts sequence of lines as input and prints the lines after making 
# all characters in the sentence capitalized.
print("Enter lines and press 'Enter'. To stop, type 'exit'.")

def to_upper_case():
    lines = []
    while True:
        line = input("Enter a line (or 'exit' to stop): ")
        if line.lower() == 'exit':
            break
        lines.append(line.upper())
    for line in lines:
        print(line)
to_upper_case()

# Question 10:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after
# removing all duplicate words and sorting them alphanumerically.
# phrase = input("Enter words: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

# Question 11:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
def is_divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number % 5 == 0

def main():
    binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')
    divisible_by_5 = [binary_number for binary_number in binary_numbers if is_divisible_by_5(binary_number.strip())]

    print("The numbers divisible by 5 are:", ', '.join(divisible_by_5))

if __name__ == "__main__":
    main()


# Question 12:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the 
# number is an even number.
def all_even(number):
    num_str = str(number)
    digit_bool = []
    for digit in num_str:
        if int(digit) % 2 == 0:
            digit_bool.append(True)
        else:
            digit_bool.append(False)
    return digit_bool

answer = [i for i in range(1000, 3001) if all(all_even(i))]
print(answer)

# Question 13:
# Write a program that accepts a sentence and calculate the number of letters and digits.
s = input("Input a string: ")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Number of Letters - ", l)
print("Number of Digits - ", d)


# Question 14:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("Number of Upper case characters : ", d["UPPER_CASE"])
    print ("Number of Lower case Characters : ", d["LOWER_CASE"])

string_test('Hello world')


# Question 15:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
value = input("Enter value: ")
n1 = value * 1
n2 = value * 2
n3 = value * 3
n4 = value * 4
total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)


# Question 16:
# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.
values = input("Enter comma seperated numbers: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))