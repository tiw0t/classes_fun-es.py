def criar_relatorio(titulo, autor, data, conteudo, formato="PDF", confidencial=False, version=1.0):
    return{
        "titulo":titulo,
        "autor":data,
        "conteudo":conteudo,
        "formato":formato,
        "confidencial":confidencial,
        "version":version
    }
relatorio = criar_relatorio(
    "Análise de Mercado",
    "Timóteo Bastos",
    "2025-04-30",
    "texto detalhado da análise...",
    confidencial=True,
    version=2.1
)
print(relatorio)