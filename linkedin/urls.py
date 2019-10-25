from django.urls import path,include
from .views import Login
from linkedin import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='login'),
    #path('loginfirst', views.loginfirst, name='loginfirst'),
    path('call_back/', views.call_back, name='call_back'),
    path('plans', views.plans, name='plans'),
    path('payment', views.payment, name='payment'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('connections', views.connections, name='connections'),
    path('campaigns', views.campaigns, name='campaigns'),
    path('messages', views.messages, name='messages'),
    path('logout', views.logout, name='logout'),
    #path('social-auth/', include('social_django.urls', namespace="social")),
]