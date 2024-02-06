from django.db import models
from user.models import User
from django.contrib.auth.models import User as DefaultUser

# Create your models here.
class Feed(models.Model):
  content = models.TextField()        # 글내용 표시
  image = models.TextField()          # 피드이미지 표시
  email = models.EmailField(default='')
  like_count = models.IntegerField(default=0)
  user_key = models.ForeignKey(User, on_delete=models.CASCADE) #글쓴 사람의 id 키 저장
