def usage():
	print("---BASIC CALCULATOR---\n\n")
	print("Usage: n1 <operation> n2\n")
	print("Supports the operations: +, -, *, /\n")
	print("To exit, type exit or ^C.\n")

usage()
while(1):
	calc = raw_input("Enter calculation: \n")
	query = calc.split()
	if calc == "exit":
		exit(0)
	elif len(query) != 3:
		print("ERROR: Must input 3 arguments.\n");
		usage()
	else:
		num1 = int(query[0])
		op = query[1]
		num2 = int(query[2])
		if (((isinstance(num1, int)) == False) or ((isinstance(num2, int)) == False) or ((isinstance(op, str)) == False)):
			usage()
		else:
			total = 0
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
			print("%d\n" % (total))
