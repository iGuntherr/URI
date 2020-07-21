i, j = 1, 7

while (i < 10):
    for x in range(3):
        print('I={} J={}'.format( i, j))
        j -= 1
    i += 2 
    j = 7