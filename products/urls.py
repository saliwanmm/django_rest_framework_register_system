from django.urls import include, path, re_path
from rest_framework import routers

from .views import ProductsAPIViewList, ProductsAPIViewUpdate, ProductsAPIViewDestroy


# router = routers.DefaultRouter()
# router.register(r"products", ProductsViewSet, basename="products")


urlpatterns = [
    # path('drf-auth/', include('rest_framework.urls')),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    path("products/", ProductsAPIViewList.as_view(), name="products-list"),
    path("products/<int:pk>/", ProductsAPIViewUpdate.as_view(), name="products-detail"),
    path("productsdelete/<int:pk>/", ProductsAPIViewDestroy.as_view(), name="products-delete"),
    # path("", include(router.urls)),
    # path('productslist/', ProductsViewSet.as_view({"get": "list"}), name="products-list"),
    # path('productslist/<int:pk>/', ProductsViewSet.as_view({"put": "update"}), name="products-detail"),
]