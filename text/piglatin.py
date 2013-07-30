string = raw_input("Enter a string you want to reverse: \n")
#latin = string[1:len(string)]+string[0]+"ay"
#print(latin)
vowels = 'aeiou'

query = string.split()
for item in query:
	latin = ""
	if item[0] in vowels:
		latin = item+"ay"
	else:
		latin = item[1:len(item)]+item[0]+"ay"
	print("%s " % (latin))
