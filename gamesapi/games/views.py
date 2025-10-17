from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from games.models import Games
from games.serializers import GameSerializer



@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        # 데이터베이스에 저장된 모든 게임 객체를 얻음
        games = Games.objects.all()
        # GameSerializer를 사용하여 모두 직렬화
        # many=True : 여러 객체를 직렬화할 때 사용 (True일 시 기본적으로 ListSerializer 사용)
        games_serializer = GameSerializer(games, many=True)

        # GameSerializer에서 생성한 데이터로 작성된 JSONResponse 객체 반환
        return Response(games_serializer.data)
    
    elif request.method == 'POST':
        # 요청 속에 들어 있는 JSON으로 된 게임 데이터를 파싱함.
        # 결과를 game_data 로컬 변수에 저장
        # game_data = JSONParser().parse(request)

        # game_data를 사용하여 GameSerializer 인스턴스 생성
        # games_serializer = GameSerializer(data = game_data)
        games_serializer = GameSerializer(data=request.data)

        # is_valid() method를 호출하여 데이터 유효성 검사
        if games_serializer.is_valid():
            # 유효할 경우, save() method를 호출해 객체를 데이터베이스에 저장함.
            games_serializer.save()

            # 저장된 데이터와 함께 201 Created 상태 코드를 JSON 형태로 반환
            return Response(games_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(games_serializer.errors,  status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    """
    기존 게임을 검색, 업데이트, 삭제하는 기능

    - request : HttpRequest instance
    - pk : primary key -> 검색, 업데이트, 삭제할 게임의 기본 키 또는 식별자
    """
    try:
        game = Games.objects.get(pk=pk)
    
    except Games.DoesNotExist:
        # 데이터베이스 내에 없을 경우, 404 Not Found가 들어간 HttpResponse를 반환
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        # game을 인자로 해서 GameSerializer 인스턴스를 생성함
        game_serializer = GameSerializer(game)

        # 기본적인 200 OK 상태가 들어간 JSONResponse를 통해 serialized된 게임 데이터를 반환
        return Response(game_serializer.data)
    
    elif request.method == 'PUT':
        # request에 포함된 JSON 데이터를 파싱함
        # game_data 로컬 변수에 저장
        game_data = JSONParser().parse(request)
        
        # 데이터베이스로부터 얻은 Games 객체(game)와 기존 데이터(game_data)를 대체할 검색된 데이터로
        # GameSerializer 인스턴스를 생성
        game_serializer = GameSerializer(game, data=game_data)

        # is_valid() method를 호출하여 데이터 유효성 검사
        if game_serializer.is_valid():
            # 유효할 경우 save() method를 호출해 데이터베이스에 바뀐 값으로 저장
            game_serializer.save()

            # 저장된 데이터가 있는 본문과 함께 200 OK 상태 코드를 JSON 형태로 반환
            return Response(game_serializer.data)
        
        # 유효한 인스턴스가 생성되지 않으면 400 Bad Request 상태 코드를 JSON 형태로 반환
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # 데이터베이스로부터 얻은 game instance에서 delete method를 호출
        # 이를 호출할 경우 테이블 내 기본 행이 지워지므로 해당 게임을 더 이상 이용할 수 없게 됨
        game.delete()

        # 더 이상 이용할 수 없다는 의미로 204 No Content 상태 코드를 반환
        return Response(status=status.HTTP_204_NO_CONTENT)