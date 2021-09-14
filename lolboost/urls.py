from django.urls import path
from lolboost import views

urlpatterns = [
    path('orders/',views.OrderList.as_view()),
    path('orders/<int:pk>/',views.OrderDetail.as_view()),
]
