from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.product_list, name='product_list'),
                  path('list/<slug:slug>/', views.product_list,
                       name='product_list_by_category'),
                  path('<int:id>/<slug:slug>/', views.product_detail,
                       name='product_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'shop'
