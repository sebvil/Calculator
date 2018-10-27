
def operations(values):
	print "operations=", values
	if  "("  in values:
		i = values.index("(")
		if ")" in values:
			j = values.index(")")
			return operations(values[0:i]+[operations(values[i+1: j])]+values[j+1:])
		else:
			return operations(values[0:i]+[operations(values[i+1:])])
	if len(values) == 3:
		if values[1] == "*":
			return values[0] * values[2]
		elif values[1] == "/":
			return values[0] / values[2]
		elif values[1] == "+":
			return values[0] + values[2]
		elif values[1] == "-":
			return values[0] - values[2]


	else:
		i = -1
		j = -1
		if "*"  in values:
			i = values.index("*")
		if "/"  in values:
			j = values.index("/")
		print j
		if (i < j and i != -1) or (i> j and j == -1):
			return operations(values[0:i-1]+[operations(values[i-1: i+2])]+values[i+2:])
		if j != -1:
			print j
			return operations(values[0:j-1]+[operations(values[j-1: j+2])]+values[j+2:])


		sum = values[0]
		for i in range(1, len(values), 2):
			if values[i] == "+":
				sum += values[i+1]
			else:
				sum -= values[i+1]


		return sum
"""
operation = "3 - ( 5 + 78 ) * 2 + 7 / 5".split()
for i in range(0, len(operation)):
	
	if operation[i] not in ["+", "-", "*", "/", "(", ")"]:

		operation[i] = float(operation[i])
#print operation
#print operations([8, "*", 3, "/", 2])
#print operations([8, "/", 2, "*", 3])
print operations(operation)
"""


