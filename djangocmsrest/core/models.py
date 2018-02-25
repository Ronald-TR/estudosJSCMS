from django.db import models
from django.contrib.auth import get_user
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

class PostWritten(models.Model):
    writter = models.ForeignKey(Writer, on_delete=models.CASCADE, default=None, null=False)
    textdata = models.CharField(max_length=1000)
    postdata = models.DateTimeField(auto_now_add=True, null=False)

    def init_from_request(self, request):
        writter = Writer.objects.get(id=get_user(request).id)
        self.writter = writter
        self.textdata = str(request.POST.get('text'))