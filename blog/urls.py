from django.urls import path, include
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchPostListView,
)
from candidates.views import CandidateCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    #path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:post_id>/', include('candidates.urls')),
    #path('post/<int:pk>/candidate/', CandidateCreateView.as_view(), name = 'candidate-create'),
    #path('post/<int:pk>/candidate/update', CandidateUpdateView.as_view(), name = 'candidate-update'),
    path('posts', SearchPostListView.as_view(), name='search_posts'),
    path('posts/tag=<str:input>', SearchPostListView.as_view(), name='search_posts_tag'), 
]