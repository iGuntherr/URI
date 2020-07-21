msg = 1
inter, gremio = 0, 0
empate, grenal = 0, 0

while msg == 1:
    
    x = map(int, input().split())
    gols_i, gols_g = x 

    if gols_g > gols_i:
        gremio += 1 
    elif gols_g < gols_i:
        inter += 1
    else:
        empate += 1    
    
    grenal += 1

    while True:
        print('Novo grenal (1-sim 2-nao)')
        msg = int(input())
        if msg == 1:
            break 
        else:
            print('''{} grenais\nInter:{}\nGremio:{}\nEmpates:{}'''.format(grenal, inter, gremio, empate))
            if inter > gremio:
                print('Inter venceu mais')
            elif gremio > inter:
                print('Gremio venceu mais')
            else:
                print('Nao houve vencedor')
            break