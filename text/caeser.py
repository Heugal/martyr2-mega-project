from sys import argv
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
script, filename = argv

key = 6

target = open(filename, 'r')
output = open('output.txt', 'w')
length = os.path.getsize(filename)
i=0
while (i != (length-1)):
	char = target.read(1)
	if char in letters:
		cipherTextChar = letters[(letters.index(char)+key)%26]
		output.write(cipherTextChar)
	else:
		output.write(char)
	i += 1
