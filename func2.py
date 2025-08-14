def soma(a,b):
    return a + b 

def calculadora(a , b):
    return a + b, a - b, a * b, a / b if b != 0 else "erro"

def principal():
    a = float(input("Digite um número: "))
    b = float(input("Digite um número: "))
    print(f"Soma : {soma(a,b)}")
    print(f"calculadora: {calculadora(a,b)}")

principal()
