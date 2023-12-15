from.views import *
from django.urls import path

urlpatterns = [
    path('', custom_login, name='login'),
    path('home',home, name='home'),
    path('index',index,name="index"),

    path('property-profile/<int:property_id>/', property_profile, name='property_profile'),
    path('tenant-management', tenant_management, name='tenant_management'),
    path('tenant-profile/<int:tenant_id>/', tenant_profile, name='tenant_profile'),

]
