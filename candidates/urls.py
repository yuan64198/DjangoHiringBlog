from django.urls import path, include
from .views import (
    CandidateCreateView,
    CandidateUpdateView,
)
from candidates.views import CandidateCreateView, CandidateUpdateView
from . import views

urlpatterns = [
    path('candidate/', CandidateCreateView.as_view(), name = 'candidate-create'),
    path('candidate/<int:pk>/new/', CandidateUpdateView.as_view(), name = 'candidate-update'),
    #path('post/<int:pk>/candidate/', CandidateCreateView.as_view(), name = 'candidate-create'),
    #path('post/<int:pk>/candidate/update', CandidateUpdateView.as_view(), name = 'candidate-update'),
]