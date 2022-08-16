from email import contentmanager
from turtle import title
from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
#from django.core.serializers import register_serializer
from django.views.decorators.http import require_http_methods
import json
from django.http.response import HttpResponseForbidden


# Create your views here.
@require_http_methods(['POST'])
def create_post(request):
    if _writer_permission(new_post.writer.id, request.user):
        body =  json.loads(request.body.decode('utf-8'))
        
        new_post = Post.objects.create(
            category    = body['category'],
            writer      =  body['writer'],
            color       =  body['color'],
            title       =  body['title'],
            content     =  body['content']
        )

        new_post_json={
            "id"        : new_post.id,
            "category"  : new_post.category,
            "writer"    : new_post.writer,
            "color"     : new_post.color,
            "title"     : new_post.title,
            "content"   : new_post.content,
            "pup_date"  : new_post.pup_date,
        }

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'create_post 성공',
                'data': new_post_json
            })


@require_http_methods(["GET"])
def get_post_all(request, get_category):
    if _writer_permission(post.writer.id, request.user):
        category_post = Post.objects.filter(category=get_category)
        
        category_post_json=[] 
        for post in category_post:
            post_json_set={
                "id"        : post.id,
                "category"  : post.category,
                "writer"    : post.writer,
                "color"     : post.color,
                "title"     : post.title,
                "content"   : post.content,
                "pup_date"  : post.pup_date,
            }
            category_post_json.append(post_json_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'get_post_all 성공',
                'data': category_post_json
            })

@require_http_methods(["GET"])
def get_post_detail(request, id):
        
    post = get_object_or_404(Post,pk = id)
    if _writer_permission(post.writer.id, request.user):
        post_json={
            "id"        : post.id,
            "category"  : post.category,
            "writer"    : post.writer,
            "color"     : post.color,
            "title"     : post.title,
            "content"   : post.content,
            "pup_date"  : post.pup_date,
        }
    
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': 'get_post 성공',
            'data': post_json
        })


@require_http_methods(["PATCH"])
def update_post(request, id):
    if _writer_permission(update_post.writer.id, request.user):
        body =  json.loads(request.body.decode('utf-8'))
        update_post = get_object_or_404(Post, pk = id)

        update_post.category = body['category']
        update_post.color = body['color']
        update_post.writer = body['writer']
        update_post.title = body['title']
        update_post.content = body['content']
        update_post.save()

        update_post_json={
            "id"        : update_post.id,
            "category"  : update_post.category,
            "writer"    : update_post.writer,
            "color"     : update_post.color,
            "title"     : update_post.title,
            "content"   : update_post.content,
            "pup_date"  : update_post.pup_date,
        }

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': 'update_post 성공',
            'data': update_post_json
        })


@require_http_methods(["DELETE"])
def delete_post(request, id):
    if _writer_permission(delete_post.writer.id, request.user):
        delete_post = get_object_or_404(Post, pk = id)
        delete_post.delete()

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'delete_post 성공',
                'data': None
            })



@require_http_methods(["GET"])
def get_prev_post(request, get_category, id):
    if _writer_permission(prev_post.writer.id, request.user):
        category_post = Post.objects.filter(category=get_category)

        # id_set = Post.objects.filter(id__lt=id) # 특정값보다 작은 데이터만 조회
        # id_list = list(id_set)
        # id_list.sort()
        # prev_id = id_list[-1]
        id_set = category_post.values_list('id', flat=True)
        id_list = list(id_set)
        id_list.sort()
        prev_id = id_list[id_list.index(id)-1] # 리스트 범위를 벗어나는 경우에는 어떻게 해결??
        prev_post = get_object_or_404(Post, pk=prev_id)

        prev_post_json={
            "id"        : prev_post.id,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'get_prev_post 성공',
                'data': prev_post_json
            })


def get_next_post(request, get_category, id):
    if _writer_permission(next_post.writer.id, request.user):
        category_post = Post.objects.filter(category=get_category)

        id_set = category_post.values_list('id', flat=True)
        id_list = list(id_set)
        id_list.sort()
        next_id = id_list[id_list.index(id)+1]
        next_post = get_object_or_404(Post, pk=next_id)

        next_post_json={
            "id"        : next_post.id,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'get_next_post 성공',
                'data': next_post_json
            })


def _writer_permission(user, request_user):
    if user.id == request_user.id:
        return True
    else:
        return HttpResponseForbidden("접근 권한이 없습니다.")