from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUser, profile_view, SignupUser

app_name = 'user_account'

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', profile_view, name="profile"),
    path('signup/', SignupUser.as_view(), name='signup'),
]