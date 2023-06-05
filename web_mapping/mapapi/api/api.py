from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from mapapi.api.serializers import FarmerSerializer
from mapapi.models import Farmer

class FarmerAPIViewSet(viewsets.GenericViewSet):
    """
    Create Farmer API view set
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
 
    @action(
        detail=False, methods=['GET'], serializer_class=FarmerSerializer,
        permission_classes=[AllowAny], url_path='farmers'
    )
    def list_farmer(self, request):
        farmers = Farmer.objects.all()
        if farmers:
            return Response({'farmers':FarmerSerializer(instance=farmers, many=True).data}, status=status.HTTP_200_OK)
        return Response(data={'message': "Data Not Found"}, status=status.HTTP_200_OK)

    @action(
        detail=False, methods=['POST'], serializer_class=FarmerSerializer,
        permission_classes=[AllowAny], url_path='farmer/create', url_name='farmer-create'
    )
    def create_farmer(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(FarmerSerializer(instance=data).data, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(
        detail=False, methods=['DELETE'], serializer_class=FarmerSerializer,
        permission_classes=[AllowAny], url_path='farmer/delete/(?P<farmer_pk>[^/.]+)'
    )
    def delete_farmer(self, request, pk=None, farmer_pk=None):
        farmer = Farmer.objects.filter(id=farmer_pk)
        if farmer:
            farmer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'message': "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)