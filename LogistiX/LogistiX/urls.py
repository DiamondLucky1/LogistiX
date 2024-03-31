from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from warehouse_management import views
from LogistiX import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('main/', views.main, name='main'),
    path('modal/', views.modal, name='modal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


