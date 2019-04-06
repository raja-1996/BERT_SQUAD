from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from bert_squad_app.bert_squad.run_squad_class import SquadDataset
from bert_squad_app.bert_squad.config import Config

args = Config()
squad_dataset = SquadDataset(args)


@api_view(['GET', 'POST'])
def squad_answers(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(request.query_params['paragraph'], request.query_params['question'])

    if request.method == 'POST':
        # print(request.data['snippet'])
        paragraph = request.data['paragraph']
        question = request.data['question']
        ll = squad_dataset.predict(args, paragraph, question)
        return Response({'answer':ll})


