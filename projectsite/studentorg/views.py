from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = 'organizations'  # Renamed from 'home' for clarity
    template_name = "includes/home.html"
    paginate_by = 10
    ordering = ['name']

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'includes/org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'includes/org_del.html'
    success_url = reverse_lazy('organization-list')