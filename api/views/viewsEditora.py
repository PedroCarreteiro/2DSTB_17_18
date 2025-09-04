from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Editora
from ..serializers import EditoraSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# #Post
# class EditoraView(ListCreateAPIView):
#     queryset = Editora.objects.all()
#     serializer_class = EditoraSerializers

#GET EDITORAS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_editoras(request):
    filter_backends = [DjangoFilterBackend, SearchFilter]

    queryset = Editora.objects.all()

    for backend in list(filter_backends):
        queryset = backend().filter_queryset(request, queryset, view=get_editoras)

    serializer = EditoraSerializers(queryset, many=True)
    return Response(serializer.data) 

get_editoras.filter_backends = [DjangoFilterBackend, SearchFilter]

#Buscar em específico /?campo=busca
get_editoras.filterset_fields = ['editora', 'cnpj', 'endereco', 'telefone', 'email', 'site']

#Buscar em todos /?search=busca
get_editoras.search_fields = ['editora', 'cnpj', 'endereco', 'telefone', 'email', 'site']

#GET 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_editora(request, pk):
    editora = Editora.objects.get(pk=pk)
    serializer = EditoraSerializers(editora)
    return Response(serializer.data)
    
#POST C/ JSON
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_editora(request):
    if request.method == 'GET':
        queryset = Editora.objects.all()
        serializer = EditoraSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EditoraSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
#PUT C/ JSON
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def put_editora(request, pk):
    if request.method == 'GET':
        editora = Editora.objects.get(pk=pk)
        serializer = EditoraSerializers(editora)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try: 
            editora = Editora.objects.get(pk=pk)
        except Editora.DoesNotExist:
            return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = EditoraSerializers(editora, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
#DELETE C/ JSON
@api_view(['GET','DELETE'])  
@permission_classes([IsAuthenticated])
def delete_editora(request, pk):
    if request.method == 'GET':
        editora = Editora.objects.get(pk=pk)
        serializer = EditoraSerializers(editora)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        try:
            editora = Editora.objects.get(pk=pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_400_BAD_REQUEST)

        editora.delete()
        return Response(status=status.HTTP_200_OK)
    


    
