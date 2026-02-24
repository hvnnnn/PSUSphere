from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from .models import College
from .forms import CollegeForm
from .models import OrgMember
from .forms import OrgMemberForm
from .models import Student
from .forms import StudentForm
from .models import Program
from .forms import ProgramForm
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

# College Views
class CollegeList(ListView):
    model = College
    content_object_name = 'college'
    template_name = 'includes/college_list.html'
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'includes/college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'includes/college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'includes/college_del.html'
    success_url = reverse_lazy('college-list')

#Org Member Views
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'includes/org_member_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'includes/org_form.html' # Reuse the same form layout
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'includes/org_del.html' # Reuse the delete confirmation layout
    success_url = reverse_lazy('orgmember-list')

#Student Views
class StudentList(ListView):
    model = Student
    content_object_name = 'student'
    template_name = 'includes/student_list.html'
    paginate_by = 10  # Students lists are usually longer, so we show 10

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'includes/org_del.html'
    success_url = reverse_lazy('student-list')

#Program Views
class ProgramList(ListView):
    model = Program
    content_object_name = 'program'
    template_name = 'includes/program_list.html'
    paginate_by = 10

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'includes/org_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'includes/org_del.html'
    success_url = reverse_lazy('program-list')