from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import VendorRegistrationView, ShopListCreateView, ShopRetrieveUpdateDeleteView, nearby_shops

urlpatterns = [
    path('register/', VendorRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('shops/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('shops/<int:pk>/', ShopRetrieveUpdateDeleteView.as_view(), name='shop-detail'),
    path('nearby-shops/', nearby_shops, name='nearby-shops'),
]
