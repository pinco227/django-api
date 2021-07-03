from django.urls import path
# ProductDetailView, ProductListView
from .views import product_detail, product_list

urlpatterns = [
    # path("", ProductListView.as_view(), name="product-list"),
    # path("<int:pk>/", ProductDetailView.as_view(), name="product-detail")
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-list")
]
