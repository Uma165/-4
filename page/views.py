from django.shortcuts import render
from django.views.generic import ListView

from page.models import Page


class PageListView(ListView):
    model = Page
    context_object_name = 'page'
    template_name = 'main.html'