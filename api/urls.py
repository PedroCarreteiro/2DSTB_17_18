from django.urls import path
from .views.viewsAutor import *
from .views.viewsEditora import *
from .views.viewsLivro import *

#adicionado para jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('autores/', AutoresView.as_view()),
    # path('autores/<int:pk>', AutorRetrieveUpdateDestroy.as_view()),
    
    # path('autores/listar', listar_autores)
    path('autor/getautores', get_autores),
    path('autor/getautor/<int:pk>', get_autor),
    path('autor/postautor', post_autor),
    path('autor/putautor/<int:pk>', put_autor),
    path('autor/deleteautor/<int:pk>', delete_autor),

    #path('editora/', EditoraView.as_view()),
    path('editora/geteditoras', get_editoras),
    path('editora/geteditora/<int:pk>', get_editora),
    path('editora/posteditora', post_editora),
    path('editora/puteditora/<int:pk>', put_editora),
    path('editora/deleteeditora/<int:pk>', delete_editora),

    #path('livro/', LivroView.as_view()),    
    path('livro/getlivros', get_livros),
    path('livro/getlivro/<int:pk>', get_livro),
    path('livro/postlivro', post_livro),
    path('livro/putlivro/<int:pk>', put_livro),
    path('livro/deletelivro/<int:pk>', delete_livro),

    #Adicionado para o JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
