from math import *

def usage():
	print("---BASIC CALCULATOR---\n\n")
	print("Usage: <n1> <operation> <n2>\n")
	print("Supports the operations: +, -, *, /, !, ^, ~(square root)\n")
	print("To exit, type exit or ^C.\n")
ans = 0
usage()
while(1):
	total = 0
	calc = raw_input("Enter calculation: \n")
	query = calc.split()
	if calc == "exit":
		exit(0)
	if (len(query) == 3):
		num1 = int(query[0])
		op = query[1]
		num2 = int(query[2])
		if (((isinstance(num1, int)) == False) or ((isinstance(num2, int)) == False) or ((isinstance(op, str)) == False)):
			usage()
		else:
			if op == "+":
				total = num1+num2
			elif op == "-":
				total = num1-num2
			elif op == "*":
				total = num1*num2
			elif op == "/":
				if num2 != 0:
					total = num1/num2
				else:
					print("ERROR: Cannot divide by zero.\n")
					total = 0
			elif op == "^":
				total = pow(num1, num2)
	elif len(query) == 2:
		if query[1] == "ans":
			num1 = ans
			op = query[0]
		else:
			num1 = int(query[0])
			op = query[1]

		if op == "!":
			total = factorial(num1)
		elif op == "~":
			if num1 < 0:
				print("ERROR: Cannot square root a negative number.\n");
				total = 0
			else:
				total = sqrt(num1)
	
	print("%d\n" % (total))
	ans = total
