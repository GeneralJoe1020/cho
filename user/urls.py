from django.urls import path
from.views import Join, Login, Logout
urlpatterns = [
  path('join', Join.as_view()),
  path('login', Login.as_view(), name='login'),
  path('logout', Logout.as_view(), name='logout')
]
