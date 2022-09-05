from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailsView.as_view(), name='post_details'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
