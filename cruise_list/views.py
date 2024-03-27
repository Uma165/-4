from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView

from cruise_list.models import Сruise

from comment.forms import CommentForm

from comment.models import Comment


class СruiseListView(ListView):
    model = Сruise
    context_object_name = 'cruise_list'
    template_name = 'one.html'


def cruise_detail_view(request, pk):
    object_list = Сruise.objects.filter(pk=pk)
    pk = get_object_or_404(Сruise, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_comment = Comment(text=text)
            new_comment.save()
            return redirect(reverse('cruise:too', kwargs={'pk': pk.pk}))

    else:
        form = CommentForm()
    return render(request, "too.html", {'form': form, 'object_list': object_list, 'pk': pk})