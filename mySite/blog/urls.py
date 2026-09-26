
from django.urls import path
from . import views # imports all views associated with the blog

urlpatterns = [
    path('', views.post_list, name='post_list')
]
