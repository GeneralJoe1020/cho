from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.models import User as DefaultUser
from django.contrib.auth.hashers import make_password
from instagram.settings import MEDIA_ROOT
# Create your views here.

class Join(APIView):
  def get(self, request):
    return render(request, "user/join.html")

  def post(self, request):
    # todo 회원가입
    email = request.data.get('email', None)
    nickname = request.data.get('nickname', None)
    name = request.data.get('name', None)
    password = request.data.get('password', None)

    User.objects.create(email=email,
                        nickname=nickname,
                        password=make_password(password),
                        name=name,
                        profile_image="default_profile.png"
                        )

    return Response(status=200)


class Login(APIView):
  def get(self, request):
    return render(request, "user/login.html")

  def post(self, request):
    # todo 로그인
    # email = request.data.get('email', None)
    username = request.data.get('username', None)
    password = request.data.get('password', None)

    # user = User.objects.filter(email=email).first()
    if not DefaultUser.objects.filter(username=username).exists():
      raise APIException("User not found.")

    user = DefaultUser.objects.get(username=username)

    if user is None:
      return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

    if user.check_password(password):
      request.session['username'] = username
      return Response(status=200)
    else:
      return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


class Logout(APIView):
  def get(self, request):
    request.session.flush()
    return render(request, "user/login.html")

# class UploadProfile(APIView):
#   def post(self,request):
#     file = request.F
