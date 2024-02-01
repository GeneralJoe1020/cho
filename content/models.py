from django.db import models
from user.models import User
from django.contrib.auth.models import User as DefaultUser

# Create your models here.
class Feed(models.Model):
  content = models.TextField()        # 글내용 표시
  image = models.TextField()          # 피드이미지 표시
  profile_image = models.TextField()  # 프로필 이미지 표시
  user_id = models.TextField()        # 글쓴이 표시
  like_count = models.IntegerField()     # 좋아요 수 표시
  user_key = models.ForeignKey(DefaultUser, on_delete=models.CASCADE)
