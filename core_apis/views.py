from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MyAPI
from .models import MyDemo


# Create your views here.
class MyAPIView(APIView):
    def get(self, request):
        queryset = MyDemo.objects.all()
        serializer = MyAPI(queryset, many=True)
        return Response(serializer.data)