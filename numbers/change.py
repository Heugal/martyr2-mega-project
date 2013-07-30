from math import floor

print("Input amount of change: \n");
target = input(">");

if (isinstance(target, float)):
	target = target*100


q = floor(target/25)
target = target-(q*25)
d = floor(target/10)
target = target-(d*10)
n = floor(target/5)
target = target-(n*5)
p = target

print("Number of quarters: %d\nNumber of dimes: %d\nNumber of nickles: %d\nNumber of pennies: %d\n" % (q, d, n, p))

