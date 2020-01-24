print("A python program which checks whether a number is devisable by 5 and 11 or not")
x = 5
y = 11
the_number = input("Enter your number")
the_number = int(the_number)
result = bool(((the_number) % (x and y)) == 0 )
print("If you think the number you've entered is devisible by 5 and 11 you are", result)