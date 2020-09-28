from django.urls import path
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
    path('list/update/', views.updateFolder, name='updateFolder'),
    path('item-list/<pk>/', views.itemList, name='itemList'),

    #Json Responses
    path('home/chart-format/', views.loadChart, name='loadChart')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



