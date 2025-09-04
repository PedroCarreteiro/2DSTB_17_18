from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Autor
from ..serializers import AutorSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

#permission_classes = [IsAuthenticated] na classe generica

##Post
# class AutoresView(ListCreateAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializers

##Faztudo
# class AutorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializers

# @api_view(['GET', 'POST'])
# def listar_autores(request):
#     if request.method == 'GET':
#         queryset = Autor.objects.all()
#         serializer = AutorSerializers(queryset, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = AutorSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

#GET AUTORES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_autores(request):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    queryset = Autor.objects.all()

    for backend in list(filter_backends):
        queryset = backend().filter_queryset(request, queryset, view=get_autores)

    serializer = AutorSerializers(queryset, many=True)
    return Response(serializer.data)
    
get_autores.filter_backends = [DjangoFilterBackend, SearchFilter]

#Buscar em específico /?campo=busca
get_autores.filterset_fields = ['nome', 'sobrenome', 'nacion', 'data_nasc']

#Buscar em todos /?search=busca
get_autores.search_fields = ['nome', 'sobrenome', 'nacion', 'data_nasc']

#GET AUTOR
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    serializer = AutorSerializers(autor)
    return Response(serializer.data)

# #POST AUTOR S/ JSON
# @api_view(['POST'])
# def post_autor(request):
#     serialiazer = AutorSerializers(data = request.data)
#     if serialiazer.is_valid():
#         serialiazer.save()
#         return Response(serialiazer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialiazer.data, status=status.HTTP_400_BAD_REQUEST)
    
#POST AUTOR C/ JSON
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
#PUT AUTOR C/ JSON
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def put_autor(request, pk):
    if request.method == 'GET':
        autor = Autor.objects.get(pk=pk)
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try: 
            autor = Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = AutorSerializers(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
#PATCH AUTOR C/ JSON
@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def patch_autor(request, pk):
    if request.method == 'GET':
        autor = Autor.objects.get(pk=pk)
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        try: 
            autor = Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = AutorSerializers(autor, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
#DELETE AUTOR C/ JSON
@api_view(['GET','DELETE'])  
@permission_classes([IsAuthenticated])
def delete_autor(request, pk):
    if request.method == 'GET':
        autor = Autor.objects.get(pk=pk)
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        try:
            autor = Autor.objects.get(pk=pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_400_BAD_REQUEST)

        autor.delete()
        return Response(status=status.HTTP_200_OK)
    


    
