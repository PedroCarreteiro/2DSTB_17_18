from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Autor
from ..serializers import AutorSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
def listar_autores(request):
    queryset = Autor.objects.all()
    serializer = AutorSerializers(queryset, many=True)
    return Response(serializer.data) 

#GET AUTOR
@api_view(['GET'])
def author_list(request, pk):
    autor = Autor.objects.get(pk=pk)
    serializer = AutorSerializers(autor)
    return Response(serializer.data)

#POST AUTOR
@api_view(['POST'])
def author_create(request):
    serialiazer = AutorSerializers(data = request.data)
    if serialiazer.is_valid():
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiazer.data, status=status.HTTP_400_BAD_REQUEST)
    
#PUT AUTOR
@api_view(['PUT'])
def author_update(request, pk):
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
    
#DELETE AUTOR
@api_view(['DELETE'])  
def author_delete(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except:
        return Response({"error": "author not found"}, status=status.HTTP_400_BAD_REQUEST)

    autor.delete()
    return Response(status=status.HTTP_200_OK)
    


    
