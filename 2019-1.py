def bubble(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j+1]:
                return False
    return True


def tb(s,l):
    def ToBinary(s,liste):
        if s >= 1:
            ToBinary(s // 2 , liste)
        liste.append(s % 2)
    ToBinary(s,l)
    return l
 

def xor(lsb , lsi):
    for i in range(0,len(lsb)):
        if lsb[i] == lsi[i]:
            print(0)
        else:
            print(1)

ls = [12,8,245,4842,3]
lis= []
def x(liste):
    l=liste
    for i in range(len(liste)):
        blis = []
        liste[i] = tb(liste[i],blis)
    print(liste)

x(ls)
