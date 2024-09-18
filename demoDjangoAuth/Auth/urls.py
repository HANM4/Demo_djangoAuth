from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
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
    path('password-reset/',
         PasswordResetView.as_view(
             template_name="Auth/password_reset_form.html",
             email_template_name="Auth/password_reset_email.html",
             success_url=reverse_lazy("user_account:password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name="Auth/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="Auth/password_reset_confirm.html",
        success_url=reverse_lazy("user_account:password_reset_complete")
    ),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="Auth/password_reset_complete.html"),
         name='password_reset_complete'),
]
