from django.urls import path
from .views.viewsAutor import *
from .views.viewsEditora import *
from .views.viewsLivro import *

urlpatterns = [
    # path('autores/', AutoresView.as_view()),
    # path('autores/<int:pk>', AutorRetrieveUpdateDestroy.as_view()),
    # path('autores/listar', listar_autores)
    path('autor/getautores', get_autores),
    path('autor/getautor/<int:pk>', get_autor),
    path('autor/postautor', post_autor),
    path('autor/putautor/<int:pk>', put_autor),
    path('autor/deleteautor/<int:pk>', delete_autor)
]
