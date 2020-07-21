cont_par, cont_impar, cont_positivo, cont_negativo = 0,0,0,0
for i in range(5):
	n = float(input())
	if (n % 2) == 0:
		cont_par +=1
	else:
		cont_impar +=1
	if n > 0:
		cont_positivo +=1
	if n < 0:
		cont_negativo +=1
print('''{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)'''.format(cont_par, cont_impar, cont_positivo, cont_negativo))