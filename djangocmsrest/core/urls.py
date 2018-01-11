from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postwrite', views.postwrite, name='postwrite'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('postingcms', views.postingcms, name='postingcms'),

]