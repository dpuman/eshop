from django.urls import path
from . import views
from store.views import login, signup, index

app_name = 'store'
urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
]
