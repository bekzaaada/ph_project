from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
# from clorder import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.send_gmail, name='about'),
    path('maingallery', views.maingallery, name='maingallery'),
    path('gallery', views.gallery, name='gallery'),
    path('add-file/', views.addFile, name= "add-file"),
    path('edit-file/<str:pk>', views.editFile, name="edit-file"),
    path('delete-file/<str:pk>', views.deleteFile, name="delete-file"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
