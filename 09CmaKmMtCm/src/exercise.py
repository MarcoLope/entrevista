# De Centímetros a Kilómetros, Metros y Centímetros
def Conversion():
    cm = int(input('Introduce los cm: '))
    km= cm//100000
    m= (cm%100000)//100
    cm= (cm%100) #3 km
    if km > 0 and m<1 and cm<1:
        print(f'{km} km')
    elif km<1 and m> 0 and cm<1:
        print(f'{m} m')
    elif km < 1 and m< 1 and cm> 0:
        print(f'{cm} cm')
    elif km>0 and m> 0 and cm<1:
        print(f'{km} km')
        print(f'{m} m')
    elif km>0 and m< 1 and cm>0:
        print(f'{km} km')
        print(f'{cm} cm')
    elif km<1 and m>0 and cm>0:
        print(f'{m} m')
        print(f'{cm} cm')
    elif km>1 and m> 0 and cm>0:
        print(f'{km} km')
        print(f'{m} m')
        print(f'{cm} cm')


def main():
    # 09CmaKmMtCm
    #print(f'{"*"*50}\nTarea 02_Decisiones:Conversion\n{"*"*50}')

    # cm = int(input('Introduce los cm: '))
    # m=cm/100
    # km=m/1000
    # print(f'{cm} cm')
    # if m>=1:
    #     m=int(m)
    #     print(f'{m} m')
    # if km>=1:
    #     km=int(km)
    #     print(f'{km} km')
    Conversion()

if __name__ == '__main__':
    main()

