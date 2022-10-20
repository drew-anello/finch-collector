from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Finch, Birdhouse
from .forms import FeedingForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    finch = Finch.objects.all()
    return render(request, 'finch/index.html', {'finch': finch})


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()

    finch = Birdhouse.objects.exclude(
        id__in=finch.birdhouse.all().values_list('id'))

    return render(request, 'finch/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'birdhouse': birdhouse_finch_doesnt_have,
    })


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


def assoc_birdhouse(request, finch_id, birdhouse_id):

    Finch.objects.get(id=finch_id).birdhouse.add(birdhouse_id)
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch

    fields = ['breed', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finch'


class BirdhouseCreate(CreateView):
    model = Birdhouse
    fields = ('name', 'color')


class BirdhouseUpdate(UpdateView):
    model = Birdhouse
    fields = ('name', 'color')


class BirdhouseDelete(DeleteView):
    model = Birdhouse
    success_url = '/birdhouse/'


class BirdhouseDetail(DetailView):
    model = Birdhouse
    template_name = 'birdhouse/detail.html'


class BirdhouseList(ListView):
    model = Birdhouse
    template_name = 'birdhouse/index.html'
