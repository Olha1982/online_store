from django.urls import path
from django.contrib import admin

from online_shop.views import Login, Logout, Registration

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('admin/', admin.site.urls),
 ]
