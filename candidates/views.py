from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Candidate
from blog.models import Post
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class CandidateCreateView(SuccessMessageMixin, CreateView):
    model = Candidate
    
    fields = ['name', 'age', 'gender', 'mobile', 'email', 'city', 'expected_salary', 'will_relocate']
    #fields = ['name', 'age', 'gender', 'mobile', 'email', 'state', 'city', 'expected_salary', 'will_relocate']
    
    success_url = '/'
    success_message = 'You have successfully applied to the position! The company will contect you soon!'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Ipsum` instance exists
        before going any further.
        """
        self.apply_to = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.user = self.request.user
        
        form.instance.apply_to = self.apply_to
        return super().form_valid(form)


class CandidateUpdateView(UpdateView):
	model = Candidate
	fields = ['status']