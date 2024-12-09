from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from car.forms import CarSearchWinForm
from car.models import Car


def index(request):
    return render(request, "car/index.html")


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        win_code = self.request.GET.get("win_code", "")
        context["search_form"] = CarSearchWinForm(
            initial={"win_code": win_code}
        )
        return context

    def get_queryset(self):
        queryset = Car.objects.all()
        form = CarSearchWinForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                win_code=form.cleaned_data["win_code"]
            )
        return queryset


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
