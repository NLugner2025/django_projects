from django.contrib import admin
from django.urls import path, include
from my_project.hello_world import views as index_views
from about import views as about_views
urlpatterns = [
    path('hello', index_views.index, name='index'),
     path('about/', about_views.about_me, name='about'),
    path('admin/', admin.site.urls),
    # Include other app URLs here
]