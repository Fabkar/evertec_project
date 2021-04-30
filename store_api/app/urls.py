from . import views
from django.urls import path
from app.views import orderCreate, orderDetail, statusOrder, listOrders


urlpatterns = [
    path('', views.orderCreate, name='create_order'),
    path('<int:id>/', views.orderDetail, name='detail_order'),
    path('status/<id>/', views.statusOrder, name='status_order'),
    path('orders/', views.listOrders, name='list_order'),
]

