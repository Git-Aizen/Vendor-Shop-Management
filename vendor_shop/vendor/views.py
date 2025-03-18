from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from geopy.distance import geodesic

from .models import Shop
from .serializers import VendorSerializer, ShopSerializer
from .permissions import IsVendorOwner

User = get_user_model()

# Vendor Registration
class VendorRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]

# Shop CRUD Operations
class ShopListCreateView(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Shop.objects.filter(vendor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class ShopRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated, IsVendorOwner]
    queryset = Shop.objects.all()

# Nearby Shop Search API
@api_view(['GET'])
def nearby_shops(request):
    lat = request.query_params.get('lat')
    lon = request.query_params.get('lon')
    radius = float(request.query_params.get('radius', 5))  # Default radius 5km

    if not lat or not lon:
        return Response({"error": "Latitude and longitude are required"}, status=400)

    try:
        lat, lon = float(lat), float(lon)
    except ValueError:
        return Response({"error": "Invalid latitude or longitude"}, status=400)

    user_location = (lat, lon)
    shops = Shop.objects.all()
    nearby = []

    for shop in shops:
        shop_location = (shop.latitude, shop.longitude)
        if geodesic(user_location, shop_location).km <= radius:
            nearby.append(shop)

    serializer = ShopSerializer(nearby, many=True)
    return Response(serializer.data)
