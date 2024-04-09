from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django_filters.views import FilterView
from django.utils.decorators import method_decorator
from django.views import View

from .models import Cruise
from .filters import CruiseFilter
from comment.forms import CommentForm
from comment.models import Comment
from users.utils import login_required


class CruiseListView(FilterView):
    model = Cruise
    context_object_name = 'cruise_list'
    template_name = 'cruise_list/cruise-list.html'
    filterset_class = CruiseFilter


def cruise_detail_view(request, pk):
    cruise = get_object_or_404(Cruise, pk=pk)
    if request.user.is_authenticated:
        initial_data = {'name': request.user.get_full_name()}
        form = CommentForm(initial=initial_data)
    else:
        form = None
    comments = cruise.comments.all()
    return render(request, "cruise_list/cruise-detail.html", {'form': form,  'cruise': cruise})


class AddCommentView(View):
    @method_decorator(login_required)
    def post(self, request, pk):
        cruise = get_object_or_404(Cruise, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user if request.user.is_authenticated else None
            new_comment = Comment(text=text, cruise=cruise, user=user)
            new_comment.save()
            return redirect('cruise:cruise-detail', pk=pk)
        return render(request, "cruise_list/cruise-detail.html", {'form': form, 'cruise': cruise})
