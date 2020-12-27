from django.urls import path
from strings_app import views

urlpatterns = [
    path('projetos/strings', views.manip_strings, name='manip_strings'),
    path('projetos/chatbot', views.chatbot, name='chatbot'),
    path('projetos/image_converter', views.image_converter, name='image_converter'),
    #path('contato', views.contact, name='contact'),
    #path('projetos', views.projects, name='projects'),
    path('', views.index, name='index'),
]
