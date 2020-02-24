# task 17
x = {"key1": 1, "key2": 3, "key3": 2}
y = {"key1": 1, "key2":2}
for k1, v1 in x.items():
	for k2, v2 in y.items():
		if v1 == v2:
			print(k1, v1)

# task16

file = open("Beatles.txt", "r")
user_input = int(input("Enter number of the line you wantto read"))
for i in file:
	if int(i[0:2]) == user_input:
		print(i)
	elif int(i[0]) == user_input:
		print(i)
file.close()

# task 18

text = input("Enter the word you want to turn to Caesar cipher")
cipher_key = int(input("What's  your key buddy?"))
def caesar_cipher(text, key):
	cipher = ""
	for letter in text:
		shifted = ord(letter) + key
		cipher += chr(shifted)
	return cipher

print(caesar_cipher(text, cipher_key))
