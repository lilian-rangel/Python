def ordenada(list):
    ordem = True

    for i in range(len(list) - 1): 
        if list[i] > list[i+1]:
            ordem = False
    return ordem
