# Python program to find the sum of natural numbers up to n where n is provided by user

# change this value for a different result


# uncomment to take input from the user
#num = int(input("Enter a number: "))
num = int(input("Enter number for loop: "))
sum = 0
   # use while loop to iterate un till zero
while(num > 0):
   sum += num
   num -= 1
   print("The sum is",sum)