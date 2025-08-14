def combinar_funcoes(f1,f2):
    def combinada(x):
        return f2(f1(x))
    return combinada
dobrar = lambda x: x * 2
adicionar_um = lambda x: x + 1

combinada = combinar_funcoes(dobrar,adicionar_um )

print(combinada(3))