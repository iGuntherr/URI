A = (float(input('')))
B = (float(input('')))

A = float('{0:1}'.format(A))
B = float('{0:1}'.format(B))

MEDIA = (((A * 35) + (B * 75)) / 110)

if MEDIA >= 10:
    MEDIA = 10
    print("MEDIA = {0:.5f}".format(MEDIA))
else:
    print("MEDIA = {0:.5f}".format(MEDIA))