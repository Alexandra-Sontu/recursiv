def recursiv_putere(x,p):
    if(p==1):
        return x
    else:
        return x*recursiv_putere(x,p-1)
n1=int(input("Baza= "))
n2=int(input("Puterea= "))
print(recursiv_putere(n1,n2))
def putere_it(x,putere):
    produs=1
    for i in range(putere):
        produs*=x
    return produs
print(putere_it(n1,n2))