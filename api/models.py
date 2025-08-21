from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nasc = models.DateField(null=True, blank=True)
    nacion = models.CharField(max_length=30, null=True, blank=True)
    biogra = models.TextField(null=True, blank=True)

    #Visualizar no admin com os nomes bunitin
    def __str__(self):
        #return super(self.nome).__str__(self.sobrenome)
        #return super().__str__()
        return f"{self.nome} {self.sobrenome}"
    
class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.editora}"
    
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=255, default="Portugês")
    ano_publicacao = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=10, decimal_places=2) 
    #FKs
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"






