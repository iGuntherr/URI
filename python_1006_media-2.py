A = (float(input('')))
B = (float(input('')))
C = (float(input('')))

A = float('{0:1}'.format(A))
B = float('{0:1}'.format(B))
C = float('{0:1}'.format(C))

MEDIA = ((A * 0.2) + (B * 0.3) + (C * 0.5))
print("MEDIA = {0:.1f}".format(MEDIA))