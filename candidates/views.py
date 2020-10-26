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

class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'age', 'gender', 'mobile', 'email', 'city', 'expected_salary', 'will_relocate']

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Ipsum` instance exists
        before going any further.
        """
        self.apply_to = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.apply_to = self.apply_to
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class CandidateUpdateView(UpdateView):
	model = Candidate
	fields = ['status']


	def get_absolute_url(self):
		return reverse('blog/about.html', kwargs = {'pk': self.apply_to})