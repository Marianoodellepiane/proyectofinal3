from django.urls import path, include

urlpatterns = [
    # ... Otras URLs de tu proyecto ...
    path('clase1/', include('nombre_aplicacion.urls')),
    path('clase2/', include('nombre_aplicacion.urls')),
    path('clase3/', include('nombre_aplicacion.urls')),
]