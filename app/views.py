from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from.models import Course
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Login(LoginView):
    template_name = 'registration/login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('login')



@login_required(login_url="login")
def home(request):
    try:
        if request.method == 'POST':
            courses = Course.objects.filter(price__lte = request.POST['to'],price__gte = request.POST['from'])   
        else:
            courses = Course.objects.all()
    except:
        courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})





class CreateCourse(UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'create_course.html'
    fields = ['name', 'description', 'price', 'author']
    success_url= reverse_lazy('home')
    
    def test_func(self):
        return self.request.user.groups.filter(name='Teachers').exists()


