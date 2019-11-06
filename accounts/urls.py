from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts', views.accounts, name='accounts'),
    path('accounts/import', views.import_data, name='import_data')
]