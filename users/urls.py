from django.urls import path
from .views.cart import CartsView, CartView
from .views.order import OrdersView, OrderView
from .views.user import UserView, UsersView

urlpatterns = [
    # Cartviews' urls
    path('carts/<int:telegramid>/', CartsView.as_view()),
    path('cart/<int:pk>/', CartView.as_view()),

    # Porductviews' urls
    path('orders/', OrdersView.as_view()),
    path('order/<int:pk>/', OrderView.as_view()),

    # Userviews' urls
    path('users/', UsersView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
]