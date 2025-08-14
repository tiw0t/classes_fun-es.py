def criar_perfil_usuario(nome,idade,profissão=None,cidade=None,interesses=None):
    perfil = {
        "nome":nome,
        "idade":idade
    }
    if profissão:
        perfil["profissão"] =  profissão
    if cidade:
        perfil["cidade"] = cidade
    if interesses:
        perfil["interesses"] = interesses

    return perfil
    
    #Usando argumentos nomeados
perfil1 = criar_perfil_usuario(
    nome= "Timóteo",
    idade= 17,
    cidade= "Crato",
    interesses= ["Violino", "basquete"]
    )
print(perfil1)