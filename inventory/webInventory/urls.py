from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views

#For Static Files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('list/', views.inventoryList, name='inventoryList'),
    path('item-list/<pk>/', views.itemList, name='itemList'),
    path('tag-list/', views.tagList, name='tagList'),
    path('manage-users/', views.manageUsers, name='manageUsers'),
    path('audit-trail/',views.auditTrail, name='auditTrail'),
    path('item-details/<pk>/', views.itemDetails, name='item-details'),
    path('password-setup/', views.passwordSetup, name='password-setup'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),


    #Json Responses and Ajaxes
    path('home/chart-format/', views.loadChart, name='loadChart'),
    path('list/update/', views.updateFolder, name='updateFolder'),
    path('item-list/<pk>/update/', views.updateFolderDesc, name='updateFolderDesc'),
    path('tag-list/update/', views.updateTagName, name='tagUpdate'),
    path('manage-users/profile/', views.profileUpdate, name='viewProfile'),
    path('manage-users/reset/', views.resetPass, name='adminpass-reset'),
    path('manage-users/disable/', views.deactivateUser, name='admin-disable'),
    path('item-list/<pk>/tags/', views.getTags, name='gettags'),
    path('item-details/<pk>/tags/', views.getTags, name='gettagsDetails'),

    #Password Reset

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='webInventory/passReset/passReset.html'), #Get User Email
         name='reset_password'),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='webInventory/passReset/passResetDone.html'
    ),
         name='password_reset_done'), #Success Message After Submit Email

    path('password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='webInventory/passReset/passResetConfirm.html'),
         name='password_reset_confirm'), #Receiving Email to Reset Password

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='webInventory/passReset/passResetComplete.html'),
         name='password_reset_complete'), #Notification Message that the reset is done

]





