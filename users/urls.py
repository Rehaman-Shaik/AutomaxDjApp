from .views import login_view,RegisterView, logout_view,ProfileView
from django.urls import path


urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register', RegisterView.as_view(), name='register_view'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
