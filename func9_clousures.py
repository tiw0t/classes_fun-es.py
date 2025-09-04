def adicionar(valor):
    def clousure(numero):
        return numero + valor
    return clousure

adicionar_cinco = adicionar(5)

print(adicionar_cinco(10))
#
