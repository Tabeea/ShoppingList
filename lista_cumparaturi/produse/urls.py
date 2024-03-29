from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/' , views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('cumpara/<id>', views.change_status, name='change_status'),
    path('clothes/' , views.clothes, name='clothes'),

    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:id>', views.viewPhoto, name='photo'),
    path('deletePhoto/<str:id>', views.deletePhoto, name='deletePhoto'),
    path('addphoto/', views.addPhotos, name='addphoto')
]


