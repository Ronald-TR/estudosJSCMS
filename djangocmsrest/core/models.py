from django.db import models
from django.contrib.auth.models import User

class Writer(models.Model):
    nome_publico = models.CharField(max_length=20, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)

    def init_from_request(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username ', username)
        print('password ', password)

        self.nome_publico = request.POST.get('displayname')
        self.user = User.objects.create_user(username=username, password=password)