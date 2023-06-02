v1 = [1,3,5,8,9,10,11,12,13,15,16,17,18,19,20]
v2 = [5,9,10,1,0,1,5,5,8,1,3,5,7,4,9,4,2,5,2,10]



def main():

    v3 = []

    for i in v1:
        for j in v2:
            if(j == i):
                v3.append(j)
                break
        #percorreu toda a lista 2
    #percorre mais um da lista 1

    print(v3)

main()