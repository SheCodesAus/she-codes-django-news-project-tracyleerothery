from unicodedata import name
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('<int:pk>/edit-story', views.StoryUpdateView.as_view(), name='editStory'),
    path('category/<str:slug>/', views.CategoryView.as_view(), name = 'category'), 
]


