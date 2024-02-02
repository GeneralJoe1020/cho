from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
# from django.contrib.auth.models import User as DefaultUser
from uuid import uuid4
import os
from instagram.settings import MEDIA_ROOT
# from user.models import User
from .models import User


class Main(APIView):
  def get(self, request):
    feed_list = Feed.objects.all().order_by('-id')  # select * from content_feed;
    email = request.session.get('email', None)
    # username = request.session.get('username', None)

    if email is None:
      return redirect("/user/login")
    # if username is None:
    #   return redirect("/user/login")
    user = None
    if User.objects.filter(email=email).exists():
      user = User.objects.get(email=email)
      # raise APIException("user not found")

    if user is None:
      return redirect("/user/login")

    return render(request, "instagram/main.html", context=dict(feeds=feed_list, user=user))

    # user = None
    # if DefaultUser.objects.filter(username=username).exists():
    #   user = DefaultUser.objects.get(username=username)
    #   # raise APIException("User not found.")
    #
    # if user is None:
    #   return redirect("/user/login")
    # return render(request, "instagram/main.html", context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
  def post(self, request):
    # 일단 파일 불러와
    file = request.FILES['file']
    uuid_name = uuid4().hex
    save_path = os.path.join(MEDIA_ROOT, uuid_name)
    with open(save_path, 'wb+') as destination:
      for chunk in file.chunks():
        destination.write(chunk)

    # user_id = request.data.get('user_id')
    # user_key = User.objects.get(nickname=user_id)
    image = uuid_name
    content = request.data.get('content')
    user_id = request.data.get('user_id')
    profile_image = request.data.get('profile_image')

    if not User.objects.filter(nickname=user_id).exists():
      raise APIException("User not found.")

    user = User.objects.get(nickname=user_id)

    Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, user_key=user, like_count=0)
    # Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0,
    #                     user_key=user_key)
    # context = {
    #   "image": feed.image,
    #   "content": feed.content,
    #   "user_id": feed.user_id,
    #   "profile_image": feed.profile_image,
    #   "like_count": feed.like_count,
    #   "user_key": feed.user_key
    # }
    return Response(status=200)


class DeleteFeed(APIView):
  def delete(self, request):
    feed_id = request.data.get('feed_id')
    current_username = request.session.get('email', None)
    if current_username is None:
      raise APIException("No logged-in user.")

    if not Feed.objects.filter(pk=feed_id).exists():
      raise APIException("Feed not found.")
    feed = Feed.objects.get(pk=feed_id)
    feed_user = feed.user_key
    feed_username = feed_user.email

    if current_username != feed_username:
      raise APIException("게시글을 작성한 유저가 아니라 지울 수 없습니다.")
    # user_key_cl = User.objects.get(user_key_cl=User.pk)
    # feed_key_cl = Feed.objects.get(feed_key_cl=Feed.user_key)
    #
    # if user_key_cl != feed_key_cl:
    #   return Response(status=400, data=dict(message="게시글을 작성한 유저가 아니라 지울 수 없습니다."))
    feed.delete()
    return Response(status=200)

# class EditFeed(APIView):
#   def edit(self,reqeust):

