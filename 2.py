def fibbonaci(a: int, b: int = 0, c:int = 1):
    if b < a:
        fibbonaci(a, c, b+c)
    elif b == a:
        print(a, 'está dentro do Fibbonaci!')
    else:
        print(a, 'NÃO está dentro do Fibbonaci!')
        
num: int = input('Digite um valor: ')
fibbonaci(int(num))