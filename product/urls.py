from django.urls import path
from .views.category import CategorysView, CategoryView
from .views.product import ProductsView, ProductView

urlpatterns = [
    # Categoryviews' urls
    path('categorys/', CategorysView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),

    # Productviews' urls
    path('products/', ProductsView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
]