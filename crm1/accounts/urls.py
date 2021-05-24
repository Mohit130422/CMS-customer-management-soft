from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user"),
    path('account/', views.accountsettings, name="accounts"),

    path('products/', views.products, name="products"),
    path('customer/', views.customer, name="customer"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('createorder/<int:pk>/', views.createorder, name="create"),

    path('updateorder/<int:pk>/', views.updateorder, name="update"),
    path('delete/<int:pk>/', views.deleteorder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_complete"),

]
