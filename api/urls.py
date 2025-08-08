from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AutoresView.as_view()),
    path('autores/<int:pk>', AutorRetrieveUpdateDestroy.as_view())
]
