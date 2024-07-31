from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'studentapp/student_list.html'
    context_object_name = 'student'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'studentapp/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'studentapp/student_form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Student'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'studentapp/student_form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'studentapp/student_delete.html'
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'