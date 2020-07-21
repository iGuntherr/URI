cont = 0
total = 0 
for i in range(6):
	n = float(input())
	if n >= 0:
		total += n 
		cont +=1
print('{} valores positivos\n{:.1f}'.format(cont, (total/cont)))