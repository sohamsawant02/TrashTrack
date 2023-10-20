from django.contrib import admin
from django.urls import path, include
from trashapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('recent_data', views.recent_data, name='recent_data'),
    path('update_data', views.update_data, name='update_data'),
    path('show_data', views.show_data, name='show_data'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To store The Images and Media Files