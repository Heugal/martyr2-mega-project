print "Enter the number of fibonacci numbers you want generated: \n"
target = input(">");
num1 = 0;
num2 = 1;
sum = 0;
if target < 3:
	if target == 1:
		print("%d\n" % (num1))
		exit(0)
	elif target == 2:
		print("%d\n%d\n" % (num1, num2))
		exit(0)
	else:
		exit(0)

print("\n%d\n%d\n" % (num1, num2))
while (target > 2):
	sum = num1 + num2
	print("%d\n" % (sum))
	num1 = num2
	num2 = sum
	target = target-1
