from .views import login_view,RegisterView
from django.urls import path


urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register', RegisterView.as_view(), name='register_view')
]
