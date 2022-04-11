from django.urls import path
from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = []
=======
urlpatterns = [
    path('cadastro/<int:id>', views.cadastrar, nome='cadastrar'),
    path('deletar/<int:id>', views.deletar, nome='deletar'),
    path('visualizar<int:id>', views.visualizar, nome='visualizar'),
    path('atualizar/<int:id>', views.atualizar, nome='atualizar'),
]
>>>>>>> 5e51ac3 (Master 2.3)
