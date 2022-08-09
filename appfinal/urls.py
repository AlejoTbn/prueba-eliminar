from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('motox', views.motox, name='motox'),
    path('conductores', views.conductores, name='conductores'),
    path('conductores/crear', views.crear, name='crear'),
    path('conductores/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('conductores/editar/<int:id>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)