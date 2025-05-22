def calculadora(n1,n2, comando):

    if comando=='+':
        return n1+n2
    
    elif comando =='-':
        return n1-n2
    
    elif comando=='/':
        return n1/n2
    
    elif comando =='*':
        return n1*n2
    
num=int(input('numero 1: '))
num2=int(input('numero 2: '))
operacao=input('operação: ')
