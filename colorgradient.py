input_gradient = []
step = []
for i in range(7):
	input_gradient.append(int(input("Enter the number: ")))

for i in range(1,4):
	step.append((input_gradient[3+i]-input_gradient[i])/(input_gradient[0]-1))
	
for i in range(0, int(input_gradient[0])):
	if i == 0:
		r = input_gradient[1]
		g = input_gradient[2]
		b = input_gradient[3]
	else:
		r += step[0]
		g += step[1]
		b += step[2]
	print('rgb({0},{1},{2})'.format(round(r),round(g),round(b)))