def check_error(input_list, n):
	"""
	Check type errors in the input
	"""
	for i in input_list:
		if type(i) is str:
			raise Exception("List items must be int or float values")
	try:
		n = int(n)
	except:
		raise Exception("n must be integer")
	if n < 1 or n > len(input_list):
		raise Exception("n must be between 1 and length of list")

def maxn(input_list, n):
	"""
	To find the nth max number in the provided list
	"""
	check_error(input_list, n)
	if n == 1:
		m = input_list[0]	# Arbitrary max value from list
		for i in input_list:
			if m < i:
				m = i
		return m
	for i in range(len(input_list)-1):
		for j in range(i+1,len(input_list)):
			if input_list[i] < input_list[j]:
				temp = input_list[i]
				input_list[i] = input_list[j]
				input_list[j] = temp
	return input_list[n-1]


def minn(input_list, n):
	"""
	To find the nth min number in the provided list
	"""
	check_error(input_list, n)
	if n == 1:
		m = input_list[0]	# Arbitrary min value from list
		for i in input_list:
			if m > i:
				m = i
		return m
	for i in range(len(input_list)-1):
		for j in range(i+1,len(input_list)):
			if input_list[i] > input_list[j]:
				temp = input_list[i]
				input_list[i] = input_list[j]
				input_list[j] = temp
	return input_list[n-1]
