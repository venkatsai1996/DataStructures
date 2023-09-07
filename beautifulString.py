def makeBeautiful(str):
	# Write your code here
	leng = len(str)
	temp_0 = ['0']
	init_0 = 0
	init_1 = 1
	temp_1 = ['1']



	for i in range(1,leng):
		if init_0 == 0:
			temp_0.append('1')
			init_0 = 1
		else:
			temp_0.append('0')
			init_0 = 0
		if init_1 == 0:
			temp_1.append('1')
			init_1 = 1
		else:
			temp_1.append('0')
			init_1 = 0
	count_0 = 0
	count_1 = 0
	li = list(str)
	#print(li)
	for i in range(0,len(li)):
		if li[i] == temp_0[i]:
			pass
		else:
			count_0 = count_0 + 1
			#print("It Matched : 0000")
		if li[i] == temp_1[i]:
			pass
		else:
			count_1 = count_1 + 1
			#print("It Matched : 1111")
	
	return min(count_0,count_1)

	
	pass
