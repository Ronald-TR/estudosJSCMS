# serializa o modelo de acordo com um dict
# caso o titulo e o conteudo permanecam vazios
# apos a serializacao, retorna false 
def safeSerialization(AClass, Aarguments = {}):
    omodel = AClass()
    for k, v in Aarguments.items():
        try:
            omodel.__setattr__(k, v)
        except:
            pass
    return omodel
    