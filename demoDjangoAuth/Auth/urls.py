from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path
from .views import LoginUser, profile_view, SignupUser, AuthPasswordChangeView

app_name = 'user_account'

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', profile_view, name="profile"),
    path('signup/', SignupUser.as_view(), name='signup'),
    path('password-change/', AuthPasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
