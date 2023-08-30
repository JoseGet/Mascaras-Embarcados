numero = int(input())
mascara = int(input())

def and_mascara(num, mascara):
    return num & mascara

numero_and_mascara = and_mascara(numero, mascara)
print(bin(numero_and_mascara))

def or_mascara(num, mascara):
    return num | mascara

numero_or_mascara = or_mascara(numero, mascara)
print(bin(numero_or_mascara)) 

def xor_mascara(num, mascara):
    return num ^ mascara

numero_xor_mascara = xor_mascara(numero, mascara)
print(bin(numero_xor_mascara))