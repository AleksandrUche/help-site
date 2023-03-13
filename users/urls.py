from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/', RegisterUser.as_view(), name='signup'),
    # path('users/', include('django.contrib.auth.urls')),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
