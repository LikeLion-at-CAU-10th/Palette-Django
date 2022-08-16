from signal import raise_signal
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
import json
# Create your views here.



def create_user(request):
    if(request.method == 'POST'):
        body = json.loads(request.body.decode('utf-8', "ignore"))

        new_user = User.objects.create(
            username = body['username'],
            nickname = body['nickname'],
            password = body['password'],
            category = body['category']
        )

        new_user_json={
            "id"      : new_user.id,
            "username"  : new_user.username,
            "nickname" : new_user.nickname,
            "password" : new_user.password,
            "category" : new_user.category,
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
    if request.method == 'POST' :
        body = json.loads(request.body.decode('utf-8'))

        username = body['username']
        password = body['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            user_info = User.objects.filter(username=username)

            login_json={
                "id"       : user_info.id,
                "username"   : user_info.username,
                "nickname" : user_info.nickname,
                "category" : user_info.category,
            }

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

def update_category(request, id):
    if request.method == "PATCH":
        body =  json.loads(request.body.decode('utf-8'))
        update_category = get_object_or_404(User, pk = id)

        update_category.category = body['category']
        update_category.save()

        update_category_json={
            "category"  : update_category.category,
        }

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': 'update_category 성공',
            'data': update_category_json
        })

    return JsonResponse({
        'status': 405,
        'success': False,
        'message': 'update_category 실패',
        'data': None
    })