from . import views
from django.urls import path
from app.views import index, orderCreate, orderDetail, statusOrder, listOrders, NewOrder


urlpatterns = [
    path('',views.index, name="Index"),
    path('new/', views.orderCreate, name='create_order'),
    path('<int:id>/', views.orderDetail, name='detail_order'),
    path('status/<id>/', views.statusOrder, name='status_order'),
    path('orders/', views.listOrders, name='list_order'),
    path('create/', views.NewOrder),
]

