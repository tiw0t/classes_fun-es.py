def chave_valor(**kwargs):
    x = kwargs.get('nome')
    print(x)

chave_valor(nome = "Timóteo", idade = 17, altura=1.78)
