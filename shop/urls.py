from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('products/', views.ProductsView.as_view(), name="products"),
    path('about/', views.AboutView.as_view(), name="about"),
]
