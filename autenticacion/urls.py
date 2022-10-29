from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

# enlaces para mostrar las vistas (URLS)
# path(para pasar parametros, llamado a las  views, nombre de la url)

urlpatterns = [
    path('logout/', salir, name='logout'),
    path('login/', entrar, name='login'),
    path('', entrar, name='login2'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recuperar/password_reset_form.html', email_template_name='recuperar/password_reset_email.html',), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='recuperar/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperar/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperar/password_reset_complete.html'), name='password_reset_complete'),
]
