from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_order, name="create_order"),
    path("admin/order/<order_id>", views.admin_order_detail, name="admin_order_detail"),
    path("admin/order/<order_id>/pdf/", views.admin_order_pdf, name="admin_order_pdf"),
]

app_name = "orders"
