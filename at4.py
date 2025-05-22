def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return "Aprovado com média {:.2f}".format(media)
    else:
        return "Reprovado com média {:.2f}".format(media)
