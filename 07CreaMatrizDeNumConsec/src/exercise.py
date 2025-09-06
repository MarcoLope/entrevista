# Escribe tus funciones abajo de esta línea
def lista(n,m):
    if n>=2 and m>=2:
        suma=n
        rango=n*m
        contador=1 
        for i in range(n):
            lista=[]
            if n>=2 and m>=2:
                if m==n :
                    for j in range(contador, rango):
                        lista.append(j)
                        #contador +=1
                    m += suma-1
                elif m>n:
                    for j in range(contador,rango+1):
                        lista.append(j)
                        #contador +=1
                    m += suma
                elif m<n:
                    for j in range(contador, rango):
                        lista.append(j)
                        #contador +=1
                    m += suma-1
        Lista_listas=[lista[i:i + n] for i in range(0, len(lista), n)]
        print(Lista_listas)         
    else:
        print("Error")

            
    
def main():
    # Escribe tu código abajo de esta línea
    m= int(input())
    n= int(input())
    x=lista(n,m)
    
if __name__ == '__main__':
    main()