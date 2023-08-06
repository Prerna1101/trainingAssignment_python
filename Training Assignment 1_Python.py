# Python program to print all prime number till 50

def primeNumbers(x, y):
	# result list
	prime_numbers_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				# divisible
				if i % j == 0:
					break
			else:
				prime_numbers_list.append(i)
	return prime_numbers_list

start = 2
end = 50
list = primeNumbers(start, end)
print("The prime numbers in this range are: ", list)


# To print user input Table
number = int(input ("Enter the number to print the multiplication table: "))      
count = 1        
print ("The Multiplication Table of: ", number)    
while count <= 10:     
    print (number, 'x', count, '=', number * count)    
    count += 1    


# To check if a string is palindrome or not
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
s = input("Enter string to be checked:")
ans = isPalindrome(s)
 
if (ans):
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")

# Reverse a string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input("Enter string to be reversed:")
 
print("Original string: ", end="")
print(s)
 
print("Reversed string: ", end="")
print(reverse(s))