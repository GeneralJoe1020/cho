from django.urls import path
from .views import UploadFeed
from .views import DeleteFeed

urlpatterns = [
  path('upload', UploadFeed.as_view()),
  path('delete', DeleteFeed.as_view())
]
