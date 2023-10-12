# Python is case sensitive!
# Indentation is really damn important, do NOT miss it, EVER!

# a= input('Enter first no.')
# b= input('Enter second no.')

# a= int(a)
# b= int(b)

# By default, quoted variables are defined by str or string.

# avg = (a + b) / 2
# print(avg)

# x = input('Please input your no.')
# x = float(x)

# print('The square of the given no. is', x**2)

# \ commands are - \n for new line, \t for tab, \\ 
# A tuple is a list that cannot be altered

# Dicrionary has keys and values, it can be altered too.
# It can have sub dicts also, which also can be altered!

a = float(input('Marks of the first subject:'))

if (a>= 0 and a<=100):
	print('The percentage in the first subject is:', (a),"%")
else:
	print('please enter valid marks')
	a = float(input('Marks of the first subject:'))

b = float(input('Marks of the second subject:'))

if (b>= 0 and b<=100):
	print('The percentage in the first subject is:', (b),"%")
else:
	print('please enter valid marks')
	b = float(input('Marks of the first subject:'))

c = float(input('Marks of the third subject:'))

if (c>= 0 and c<=100):
	print('The percentage in the first subject is:', (c),"%")
else:
	print('please enter valid marks')
	c = float(input('Marks of the first subject:'))

if ((a) >= 33):
	print('the student is pass in the first subject')
else:
	print('The student has failed the first subject')

if ((b) >= 33):
	print('the student is pass in the second subject')
else:
	print('The student has failed the second subject')

if ((c) >= 33):
	print('the student is pass in the third subject')
else:
	print('The student has failed the third subject')

if (((a+b+c)/3) >= 40):
	print('The student has passed the event exams')
else:
	print('The student has failed the event exams')

x = input('Press enter to continue')
