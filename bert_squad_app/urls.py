from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bert_squad_app import views

urlpatterns = [
    path('squad/', views.squad_answers),
]

urlpatterns = format_suffix_patterns(urlpatterns)