# user_input = input("What are you thinking about")
# def spasces():
# 	initial = 0
# 	for i in user_input:
# 		if i == " ":
# 			initial += 1 
# 	return "You have used", initial + 1, "words"
# print(spasces())


# user_input1 = str(input("Enter your phone number"))
# if user_input1[1:3] == str(77) or user_input1[1:3] == str(94) or user_input1[1:3] == str(98) or user_input1[1:3] == str(99):
# 	print("You are using VicaCell")
# elif user_input1[1:3] == str(91) or user_input1[1:3] == str(96):
# 	print("You are using Beeline")
# elif user_input1[1:3] == str(55) or user_input1[1:3] == str(95) or user_input1[1:3] == str(44):
# 	print("You ar using UCOM")
# else:
# 	print("You are using unknown operator or you don't know your own number")

# user_input = input("input")
# print(user_input[0] + user_input[1:].replace(user_input[0],'$'))

# user_input = input("input")
# first_ending = "ly"
# second_ending= "ing"
# if user_input.endswith("ing") == True: 
# 	print(user_input + first_ending)
# elif len(user_input) <= 3:
# 	print(user_input + second_ending)
# else:
# 	print(user_input)

# user_input = input("Input")
# user_not_input = user_input.find("not")
# user_poor_input = user_input.find("poor")
# if user_poor_input and user_not_input:
# 	print(user_input[0:user_not_input] + user_input[user_not_input:].replace(user_input[user_not_input:], "good"))