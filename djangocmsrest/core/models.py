from django.db import models

# Create your models here.
class Postagem(models.Model):
    title = models.CharField(max_length=122)
    content = models.TextField()
    datapostagem = models.DateTimeField(auto_now_add=True)

    # serializa o modelo de acordo com um dict
    # caso o titulo e o conteudo permanecam vazios
    # apos a serializacao, retorna false 
    def safeSerialization(self, arguments = {}):
        bresult = True
        for k, v in arguments.items():
            try:
                self.__setattr__(k, v)
            except:
                pass
        if (self.title == '') and (self.content == ''):
            bresult = False
        return bresult
                
