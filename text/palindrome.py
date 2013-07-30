string = raw_input("Enter a string to check if it is a palindrome: \n")
newstr = string.replace(" ", "")
if newstr == newstr[::-1]:
	print "\n%s is a palindrome.\n" % (string)
else:
	print "\n%s is not a palindrome.\n" % (string)
