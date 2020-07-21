A = input()
B = input()
A = A.split(" ")
B = B.split(" ")

calcA = int(A[1]) * float(A[2])
calcB = int(B[1]) * float(B[2])
calcT = (calcA + calcB)

print('VALOR A PAGAR: R$ {:.2f}'.format(calcT))