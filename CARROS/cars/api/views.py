from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cars.models import Car
from cars.api.serializers import CarSerializer

"""
@api_view(['GET'])
def getData(request):
    cars = Car.objects.select_related('brand')
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
"""   
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    
    def list(self, request):
        queryset = self.get_queryset().values('model', 'brand__name', 'factory_year', 'value', 'photo')
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Car.objects.all()

class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer