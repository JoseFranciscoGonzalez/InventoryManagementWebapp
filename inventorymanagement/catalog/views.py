from django.shortcuts import render, redirect, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import System, Trademark, Material, MaterialHistory
from .forms import EntryModelForm, SearchModelForm
from datetime import datetime
from django.db.models import F
import socket


class LandingPageView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    object_list = MaterialHistory.objects.all()[:10]

    def get_queryset(self):
        return MaterialHistory.objects.all()[:10]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['alarms'] = Material.objects.all().filter(stock__lte=F('safety_stock'))
        return context


class MaterialListView(LoginRequiredMixin, ListView):
    template_name = "materials.html"
    form = SearchModelForm()
    object_list = Material.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.POST)
        object_list = Material.objects.filter(description__contains=request.POST['description']).filter(id__contains=request.POST['id']).filter(position__contains=request.POST['position']).filter(system__name__contains=request.POST['system'])
        context = {'object_list': object_list}
        return super(ListView, self).render_to_response(context)

    def get_queryset(self):
        return Material.objects.all()


class MaterialSearchView(ListView):
    template_name = "search_form.html"
    form = SearchModelForm()

    def get_queryset(self):
        return Material.objects.all()


class MaterialDetailView(LoginRequiredMixin, DetailView):
    template_name = "material_details.html"
    queryset = Material.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            material = Material.objects.get(id=request.POST['id_exit'])
            material.stock = material.stock - int(request.POST['quantity_exit'])
            material.last_entry = datetime.now()
            material.save()
            history = MaterialHistory(material=material, quantity=request.POST['quantity_exit'], operation='s', user=request.user, date=datetime.now())
            history.save()
            return redirect("../{pk}/".format(pk=request.POST['id_exit']))
        except MultiValueDictKeyError:
            material = Material.objects.get(id=request.POST['id'])
            material.stock = material.stock + int(request.POST['quantity'])
            material.last_entry = datetime.now()
            material.save()
            history = MaterialHistory(material=material, quantity=request.POST['quantity'], operation='e', user=request.user, date=datetime.now())
            history.save()
            return redirect("../{pk}/".format(pk=request.POST['id']))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['text'] = "http://{ip}:8000/catalog/materials/{id}".format(id=context['material'].id, ip=socket.gethostbyname(socket.gethostname()))
        return context


class MaterialHistoryView(DetailView):
    template_name = "material_history.html"
    history = MaterialHistory.objects.all()

    def get(self, request, *args, **kwargs):
        print(request.GET['material'])
        object_list = MaterialHistory.objects.filter(material__id__contains=request.GET['material'])
        context = {'object_list': object_list}
        return super(DetailView, self).render_to_response(context)


def MaterialCreateView(request):
    form = EntryModelForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = EntryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../materials/{pk}/".format(pk=form.cleaned_data['id']))
    context = {"form": form}
    return render(request, "entry.html", context)


def MaterialSuccessView(request):
    print(request.POST)
    form = EntryModelForm()
    if request.method == "POST":
        form = EntryModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    context = {"form": form}
    return render(request, "entry_success.html", context)


