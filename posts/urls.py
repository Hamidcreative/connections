from django.urls import path,include
from posts import views
from django.conf import settings

urlpatterns = [

    path('updates', views.updates, name='updates'),
    path('updates/import', views.import_posts, name='import_posts')

]