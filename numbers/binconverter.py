def usage():
	print("---BINARY/DECIMAL CONVERTER---\n\n")
	print("Usage: <num> [bin (for dec->bin) / dec (for bin->dec)]\n")
	print("Converts a number from binary to decimal and the other way around.\n")

usage()
query = raw_input(">")
conv = query.split(" ")
if len(conv) != 2:
	print("ERROR: More than 2 commands are needed.\n")
	usage()
	exit(1)
num = int(conv[0])
op = conv[1]

# dec to binary
if op == "bin":
	ans = ""
	while (num != 0):
		rem = num%2
		ans += str(rem)
		num = num / 2
	ans = ans[::-1]
	print(ans)
	exit(0)
# bin to dec
elif op == "dec":
	test = str(num)
	ans = 0
	for i in range (0,len(test)):
		ans = (ans*2)+1 if int(test[i]) == 1 else ans*2
	print(ans)
	exit(0)
else:
	print("ERROR: must specify either binary or decimal conversion.\n")
	usage()
	exit(1)
