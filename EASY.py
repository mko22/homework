list1 = [10, 20, 30, 40, 50]
list2 = []
for i in reversed(list1):
	list2.append(i)

print(list2)
		
a = 0
b = 100
while a < 100:
	while b > 0:
		a = a + 1
		b = b - 1
		print(a, "---", b)

my_list = []
for i in range(0, 10):
	for j in range(0, 10):
		for k in range(0, 10):
			num = str(i) + str(j) + str(k)
			if num not in my_list and int(num) < 1000:
				my_list.append(num)

print(my_list)
