from django.views.generic import ListView

from cruise_list.models import Сruise


class СruiseListView(ListView):
    model = Сruise
    context_object_name = 'cruise_list'
    template_name = 'one.html'