from datetime import datetime as dt


def diz_oi():
    agora = dt.now().hour
    if agora > 5 and agora < 12:
        print("Oi zé! Bom dia!")
    elif agora >= 12 and agora <= 17:
        print("Oi zé! Boa tarde!")
    else:
        print("Oi zé! Boa noite")


diz_oi()

oi = diz_oi

oi()
