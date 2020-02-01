user_input = int(input("Enter your number"))
def a_number(user_input):
	result = user_input **  2 + 1 
	return result
print(a_number(user_input))


def my_program():
	user_input = str(input("Enter your number"))
	return int(int(user_input) + int(user_input * 2) + int(user_input * 3))
print(my_program())

def max_number():
	first_input = int(input("Enter the first number"))
	second_input = int(input("Enter the second number"))
	third_input = int(input("Enter the third number"))
	if first_input > second_input and first_input > third_input:
		return first_input, "is the biggest"
	elif second_input > first_input and second_input > third_input:
		return second_input, "is the biggest"
	elif third_input > first_input and third_input > second_input:
		return third_input, "is the biggest"
	elif first_input == second_input or first_input == third_input or second_input == third_input:
		return first_input, "is the biggest"

print(max_number())

def fizz_buzz():
	user_input = int(input("Enter your number"))
	if ((user_input % 3) % 5)  == 0:
		return "fizzbuzz"
	elif user_input % 5 == 0:
		return "buzz"
	elif user_input % 3 == 0:
		return "fizz"
	else:
		return user_input 

print(fizz_buzz())

def number_streak():
	limit = int(input("Enter your number"))
	for i in range(0, limit):
		if i % 2 == 0:
			print(i, "even")
		else:
			print(i, "odd")

number_streak()