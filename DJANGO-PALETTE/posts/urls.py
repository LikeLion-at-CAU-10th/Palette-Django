from django.urls import path
from .views import *

urlpatterns = [
    path('create-post', create_post, name="create-post" ),
    path('get-post-all/<str:get_category>', get_post_all, name='get-post-all'),
    path('get-post_detail/<int:id>', get_post_detail, name='get-post-detail'),
    path('update-post/<int:id>', update_post, name='update-post'),
    path('delete-post/<int:id>', delete_post, name='delete-post'),
    path('get-prev-post/<str:get_category>/<int:id>', get_prev_post, name='get-prev-post'),
    path('get-next-post/<str:get_category>/<int:id>', get_next_post, name='get-next-post'),
]