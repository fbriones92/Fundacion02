# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from voluntarios.models import Voluntario
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from voluntarios.forms import VoluntarioForm
from django.urls.base import reverse

# Create your views here.
@login_required
def home (request):
    templates = 'voluntarios/voluntario_master.html'
    return render(request, templates)

@login_required
def voluntarios(request):
    templates = 'voluntarios/voluntarios.html'
    voluntarios = Voluntario.objects.filter(
                Q(estado = Voluntario.ESTADO_ACTIVO))

    data = {
            'voluntarios': voluntarios,
            
        }
    return render(request, templates, data)

@login_required
def voluntario(request, voluntario_id = None):
    template = 'voluntarios/voluntario_crear.html'
    form = VoluntarioForm()
    voluntario = None
    
    if voluntario_id is not None:
        voluntario = Voluntario.objects.get(id = voluntario_id)
        form = VoluntarioForm(instance = voluntario)
            
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, request.FILES, instance = voluntario)
        (form.data)
        if form.is_valid():
            print(form.cleaned_data)
            voluntario = form.save()
            return HttpResponseRedirect(reverse('voluntarios'))
        
    data = {
            'form':form,
            
        }
    return render(request, template, data)

@login_required
def update(request, voluntario_id = None):
    voluntario = Voluntario.objects.get(id = voluntario_id )
    voluntario.estado = "1"
    voluntario.save()
    return HttpResponseRedirect(reverse('voluntarios'))


