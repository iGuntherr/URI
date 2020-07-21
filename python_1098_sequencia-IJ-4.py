i, j, h = 0, 1, 1

while (i < 2):
    for x in range(3):
        if (round(h, 1) - round(h, 0)) == 0:            
            print('I={:.0f} J={:.0f}'.format(i, h))
        else:
            print('I={:.1f} J={:.1f}'.format(i, h))
        h += 1
    i += 0.2
    j += 0.2
    h = j