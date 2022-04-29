from datetime import date
from email.mime import image
from queue import Empty
from unittest import result
from xmlrpc.client import ResponseError
from django.http import request, response
import requests
import json, random, time 
from pprint import pprint
# from comics.models import Comic, Character

# # url=f"https://gateway.marvel.com/v1/public/characters?offset=1&ts={ts}&apikey={public}&hash={hashed}"
ts='l'
public="2862b63a5d742b3c93f5f1440b808282"
hashed = "36665c9bcf88780dfcf1c00433bbc151"
url=f"https://gateway.marvel.com/v1/public/characters?offset=0&limit=20&ts={ts}&apikey={public}&hash={hashed}"


def get_data():
    lista=[]
    response=requests.get(url)
    response_json=json.loads(response.text)
    data= response_json['data']['results']
    for element in data:
        id=element["id"]
        name=element["name"]
        image={"path":element["thumbnail"]["path"],
                "extension":element["thumbnail"]["extension"]}
        apperances=element["comics"]["available"]
        dic={"id":id,"name":name,"image":image,"apperances":apperances}
        lista.append(dic)
    return lista 

def get_id(pk):
    lista=[]
    print("entro")
    url1=f"https://gateway.marvel.com/v1/public/characters/{pk}?ts={ts}&apikey={public}&hash={hashed}"
    url2=f"https://gateway.marvel.com/v1/public/comics/{pk}?ts={ts}&apikey={public}&hash={hashed}"
    urls=[url1,url2]
    for url in urls:
        response=requests.get(url)
        if response.status_code==200:
            if urls[1]==url:
                print("comics")
                response_json=json.loads(response.text)
                data= response_json["data"]["results"]
                for comic in data:
                    id_comic=comic["id"]
                    title=comic["title"]
                    image_comic={"path":comic["thumbnail"]["path"],
                                "extension":comic["thumbnail"]["extension"]}
                    onsaleDate=comic["dates"][1]
                    dicts={"id":id_comic,"title":title,"image":image_comic,"onsaleDate":onsaleDate}
                    lista.append(dicts)
                # print(lista)
            else:
                # print("personajes")
                response_json=json.loads(response.text)
                data= response_json["data"]["results"]
                for chart in data:
                    id=chart["id"]
                    name=chart["name"]
                    image={"path":chart["thumbnail"]["path"],
                            "extension":chart["thumbnail"]["extension"]}
                    apperances=chart["comics"]["available"]
                    dic={"id":id,"name":name,"image":image,"apperances":apperances}
                    lista.append(dic)
                # print(lista)
            return lista
# get_id(82967)

def get_character_comics(name):
    lista=[]
    print(name)
    url1=f"https://gateway.marvel.com/v1/public/characters?nameStartsWith={name}&ts={ts}&apikey={public}&hash={hashed}"
    url2=f"https://gateway.marvel.com/v1/public/comics?titleStartsWith={name}&ts={ts}&apikey={public}&hash={hashed}"
    
    character=requests.get(url1)
    character_json=json.loads(character.text)
    data_char=character_json["data"]["results"]
    comics=requests.get(url2)
    comics_json=json.loads(comics.text)
    data_comic=comics_json["data"]["results"]
    if data_char !=[] and data_comic !=[]:
        for char in data_char:
            for comic in data_comic:
                id_char=char["id"]
                name=char["name"]
                image={"path":char["thumbnail"]["path"],
                        "extension":char["thumbnail"]["extension"]}
                apperances=char["comics"]["available"]
                id_comic=comic["id"]
                title=comic["title"]
                image_comic={"path":comic["thumbnail"]["path"],
                            "extension":comic["thumbnail"]["extension"]}
                onsaleDate=comic["dates"][1]
                dic_comics_char={"id":id_char,"name":name,"image":image,"apperances":apperances, "comics":{"id":id_comic,"title":title,"image":image_comic,"onsaleDate":onsaleDate}}
                lista.append(dic_comics_char)
            # pprint(lista)
        return lista
        
    else:
        data={"message":"Empty Service"}
        return data
