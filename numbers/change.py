from math import floor

cost = input("Input cost: \n");
target = input("Input amount of money given: \n")

if (isinstance(target, float)):
	target = target*100
if (isinstance(cost, float)):
	cost = cost*100

if cost-target > 0:
	print("You need to pay more money to cover the cost.\n")
	exit(0)
target = target-cost
q = floor(target/25)
target = target-(q*25)
d = floor(target/10)
target = target-(d*10)
n = floor(target/5)
target = target-(n*5)
p = target

print("Number of quarters: %d\nNumber of dimes: %d\nNumber of nickles: %d\nNumber of pennies: %d\n" % (q, d, n, p))

