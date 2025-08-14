from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .serializers import AutorSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Post
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers

@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer)

class AutorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers
    
