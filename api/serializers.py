#Serializers serve para transformar nossa tabela em um arquivo que o python consegue ler, nesse caso, JSON

from rest_framework import serializers
from .models import Autor

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'