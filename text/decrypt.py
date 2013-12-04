from sys import argv
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
script, filename = argv

key = 1

target = open(filename, 'r')
output = open('decrypt.txt', 'w')
length = os.path.getsize(filename)
i=0

print "\n\nCaesar cipher crack"
print """
Function will loop through the cipher
Type "yes" when prompted when the code looks readable
to find the key
"""

while (key < 26):
	target.seek(0)
	sentence = target.read(30)
	newSentence = ""
	for char in sentence:
		if char in letters:
			plainTextChar = letters[(letters.index(char)-key)%26]
			newSentence += plainTextChar
		else:
			newSentence += char
	print newSentence
	print "Type 'yes' if the cipher was readable"
	question = raw_input("> ")
	if (question == "yes"):
		print "key is: %d\n" % key
		target.seek(0)
		while (i != (length-1)):
			char = target.read(1)
			if char in letters:
				plainTextChar = letters[(letters.index(char)-key)%26]
				output.write(plainTextChar)
			else:
				output.write(char)
			i += 1
		break;
	i=0
	key += 1
