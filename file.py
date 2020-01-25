user_name = input("Enter your name")
user_second_name = input("Enter your second name")
user_surname = input("Enter your surname")
user_age = input("Enter your age")
user_age = int(user_age)
print(type(user_name))
print(type(user_second_name))
print(type(user_surname))
print(type(user_age))


random_question = input("What are you thinking about")
print(" " in random_question)
random_question = bool(" " in random_question)
print("The fact that you have a couple of words in your mind is", random_question)

print("A python program which checks whether a number is devisable by 5 and 11 or not")
x = 5
y = 11
the_number = input("Enter your number")
the_number = int(the_number)
result = bool(((the_number) % (x and y)) == 0 )
print("If you think the number you've entered is devisible by 5 and 11 you are", result)

year = input("Enter the year")
year = int(year)
print((year % 4) == 0 )
