from re import template

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm

from news.models import NewsStory

USER_MODEL = get_user_model()

class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['user_story'] = NewsStory.objects.filter(author=self.kwargs['pk'])
            print(context['user_story'])
            return context

    
class CreateAccountView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "users/createAccount.html"
