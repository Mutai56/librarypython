# python script that checks if a number is even or old

num: int=int(input("enter number"))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num}is odd number")

5

# create a statement that prints the largest for three numbers
num2=int(input("Enter the first number"))
num3=int(input("Enter the second number"))
num4=int(input("Enter the third  number"))

if num2 >= num3 and num2 >= num4:
    largest = num3
elif num2 >= num2 and num3 >= num4:
    largest = num3
else:

    largest = num4

print("The largest number is:", largest)

