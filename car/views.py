from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from car.forms import CarSearchWinForm, CompanyCreationForm
from car.models import Car, InfoCar, CheckUpCar, CarOwner, CompanyCheckUp


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


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("car:car_list")


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy("car:car_list")


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("car:car_list")


class CarCheckupDetailView(LoginRequiredMixin, DetailView):
    model = InfoCar
    template_name = "car/checkup_detail.html"
    context_object_name = "checkups"


class CheckUpCreateView(LoginRequiredMixin, CreateView):
    model = CheckUpCar
    fields = "__all__"
    template_name = "car/checkup_form.html"
    # success_url = reverse_lazy("car:car-checkup")


class CheckUpUpdateView(LoginRequiredMixin, UpdateView):
    model = CheckUpCar
    fields = "__all__"
    template_name = "car/checkup_form.html"
    # success_url =


class CheckUpDeleteView(LoginRequiredMixin, DeleteView):
    model = CheckUpCar
    template_name = "car/checkup_confirm_delete.html"


class CarOwnerDetailView(LoginRequiredMixin, DetailView):
    model = InfoCar
    # context_object_name = "carowner"
    template_name = "car/car_owner.html"


class CarOwnerCreateView(LoginRequiredMixin, CreateView):
    model = CarOwner
    fields = "__all__"
    template_name = "car/carowner_form.html"


class CarOwnerUpdateView(LoginRequiredMixin, UpdateView):
    model = CarOwner
    fields = "__all__"
    template_name = "car/carowner_form.html"


class CarOwnerDeleteView(LoginRequiredMixin, DeleteView):
    model = CarOwner
    template_name = "car/carowner_confirm_delete.html"


class CompanyCheckUpDetailView(LoginRequiredMixin, DetailView):
    model = CheckUpCar
    template_name = "car/company_checkup_detail.html"


class CompanyCheckUpCreateView(LoginRequiredMixin, CreateView):
    model = CompanyCheckUp
    form_class = CompanyCreationForm
