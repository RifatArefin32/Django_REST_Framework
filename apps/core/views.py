from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.core.models import Product
from apps.core.serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
