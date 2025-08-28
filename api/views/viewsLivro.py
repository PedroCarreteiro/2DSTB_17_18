from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Livro
from ..serializers import LivroSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# #Post
# class LivroView(ListCreateAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializers

#GET LIVROS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_livros(request):
    queryset = Livro.objects.all()
    serializer = LivroSerializers(queryset, many=True)
    return Response(serializer.data) 

#GET 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    serializer = LivroSerializers(livro)
    return Response(serializer.data)
    
#POST C/ JSON
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_livro(request):
    if request.method == 'GET':
        queryset = Livro.objects.all()
        serializer = LivroSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LivroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
#PUT C/ JSON
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def put_livro(request, pk):
    if request.method == 'GET':
        livro = Livro.objects.get(pk=pk)
        serializer = LivroSerializers(livro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try: 
            livro = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = LivroSerializers(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
#DELETE C/ JSON
@api_view(['GET','DELETE'])  
@permission_classes([IsAuthenticated])
def delete_livro(request, pk):
    if request.method == 'GET':
        livro = Livro.objects.get(pk=pk)
        serializer = LivroSerializers(livro)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        try:
            livro = Livro.objects.get(pk=pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_400_BAD_REQUEST)

        livro.delete()
        return Response(status=status.HTTP_200_OK)
    


    
