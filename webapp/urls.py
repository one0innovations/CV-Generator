from django.urls import path, re_path

urlpatterns = [
    url('index/', views.index, name = 'index'),
    url('signup/', views.signup, name = 'signup'),
    url('signin/', views.signin, name = 'signin'),
    url('profile/', views.profile, name = 'profile viewer')
]
