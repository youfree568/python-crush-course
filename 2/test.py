

select = input("Select operations form + :")
 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
 

if select == '+':
	print(num1+num2)

if select == '-':
	print(num1-num2)

else:
	print("Please enter your symbol")
