# Escribe tus funciones abajo de esta línea
def llena_lista():
    lista=[]
    while True:
        num= input()
        if num == "*":
            break
        num=int(num)
        lista.append(num)
    return lista

def listas(l1, l2):
    l= l1 + l2
    l.sort()
    return l
    

def main():
 
    l1= llena_lista()
    l2 = llena_lista()
    res=listas(l1, l2)
    print("L1=")
    print(l1)
    print("L2=")
    print(l2)
    print("LORDENADA=")
    print(res)
if __name__ == '__main__':
    main()