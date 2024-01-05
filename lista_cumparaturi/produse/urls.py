from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/' , views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('cumpara/<id>', views.change_status, name='change_status'),
]

# # Code for reading css
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
