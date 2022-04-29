from email import message
import imp
from rest_framework import status
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from comics.services import get_data, get_id, get_character_comics

# Create your views here.
class ComicsView(APIView):
    def get(self, request, format=None):
        characters={
            'data':get_data()
        }
        return Response(characters)
    
@api_view(['GET'])
def get_object(request,search):
    comics={
        'comics-character':get_character_comics(search)
    }
    return Response(comics)

def get_param(request,id):
    print(id)
    comics={
        'filter-id':get_id(id)
    }
    print(comics)
    return Response(status=status.HTTP_200_OK)
    # # comics={
    # #     'filter_id':get_id(id)
    # # }
    # message={"mesage":"buen_intento"}
    # return Response(message)
    




    

    