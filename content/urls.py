from django.urls import path
from .views import UploadFeed
from .views import DeleteFeed
from .views import EditFeed
from .views import Profile
urlpatterns = [
  path('upload', UploadFeed.as_view()),
  path('delete', DeleteFeed.as_view()),
  path('edit', EditFeed.as_view()),
  path('profile', Profile.as_view())
]
