from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvapp.models import Student  # Assuming your app is named 'cbvapp'

# Create your views here
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'  # optional
    context_object_name = 'students'  # optional

class StudentDetailView(DetailView):
    model = Student  # Corrected "modes Meene" to "model = Student"
    template_name = 'student_details.html'
    # The default template name is 'student_detail.html' (based on model name)
    # The default context object name is 'student'

class StudentCreateView(CreateView):
    model = Student  # The model should start with an uppercase 'S' for 'Student'
    fields = ('firstName', 'lastName', 'testScore')  # Corrected the quotes and commas
    template_name = 'student_form.html'  # This is the default template, can be customized


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)  # Corrected tuple syntax with a comma
    template_name = 'student_form.html'  # You can use the same form template as the CreateView


class StudentDeleteView(DeleteView):
    model = Student  # Corrected the typo 'modere suoent' to 'model = Student'
    template_name = 'student_confirm_delete.html'  # Default template for confirming deletion
    success_url = reverse_lazy('student-list')  # Redirect after successful deletion