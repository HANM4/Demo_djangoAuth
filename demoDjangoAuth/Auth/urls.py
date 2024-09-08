from django.urls import path
from .views import login_view, logout_view, profile_view, signup_view

app_name = 'user_account'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', profile_view, name="profile"),
    path('signup/', signup_view, name='signup'),
]