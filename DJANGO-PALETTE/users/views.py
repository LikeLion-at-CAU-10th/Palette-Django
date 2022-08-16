from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
import json
# Create your views here.

@require_http_methods(['POST', 'GET'])

def create_user(request):
    if(request.method == 'POST'):
        body =  json.loads(request.body.decode('utf-8', "ignore"))

        new_user = User.objects.create(
            userId = body['userId'],
            nickname = body['nickname'],
            password = body['password']
        )

        new_user_json={
            "useIid"  : new_user.userId,
            "nickname" : new_user.nickname,
            "password" : new_user.password,
        }

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': "회원가입 성공",
                'data': new_user_json
            })

    return JsonResponse({
                'status': 403,
                'success': False,
                'message': "회원가입 실패",
                'data': None
        })

def user_login(request):
    if request.method == 'POST':
        body =  json.loads(request.body.decode('utf-8'))
        
        userId = request.POST['userId']
        password = request.POST['password']
        user = auth.authenticate(request, userId=userId, password=password)
        
        login_json={
            "userId"   : request.POST['userId'],
            "nickname" : request.POST['nickname'],
            "password" : request.POST['password'],
        }
        
        if user is not None:
            auth.login(request, user)
            return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'login 성공',
                'data': login_json
            })
        else:
            return JsonResponse({
                'status': 403,
                'success': False,
                'message': 'login 실패',
                'data': None
        })

def user_logout(request):
    auth.logout(request)
    return JsonResponse({
        'status': 200,
        'success': True,
        'message': 'logout 성공',
        'data': None
    })

