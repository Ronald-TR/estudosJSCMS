from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postwrite', views.postwrite, name='postwrite'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('postsave', views.postsave, name='postsave'),
    path('writerlogin', views.writerlogin, name='writerlogin'),
    path('errorlogin', views.errorlogin, name='errorlogin'),
    path('cadwriter', views.cadwriter, name='cadwriter'),
    path('writerlogout', views.writerlogout, name='writerlogout')
]