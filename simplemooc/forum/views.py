from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView

from .models import Thread

#class ForumView(TemplateView):
#    template_name = 'forum/index.html'
#index = ForumView.as_view()

#index = TemplateView.as_view(template_name=template_name)

class ForumView(ListView):

    model = Thread
    paginate_by = 10
    template_name = 'forum/index.html'

index = ForumView.as_view()