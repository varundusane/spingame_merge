from django.contrib import admin
from django.urls import path
from player import views
from django.contrib.auth import views as auth_views
from spingame.views import home, value_blinker, wallet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('dashboard/', views.Dashboard, name='Dashboard'),
    # path('game/', views.Game, name='Game'),
    path('spin/', home),
    path('game/', value_blinker, name='Game'),
    path('wallet/<str:win>/', wallet,name="wallet")
]



