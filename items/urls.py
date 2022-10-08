from django.conf import settings
from django.urls import path
from items import views

urlpatterns = [
    path('', views.general, name='general'),
    path('products/', views.products, name='products'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # noqa
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa