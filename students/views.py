import redis

from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import CourseEnrollForm
from courses.models import Course

# r = redis.Redis(
#     host = settings.REDIS_HOST,
#     port = settings.REDIS_PORT,
#     db = settings.REDIS_DB,
# )

# Create your views here.


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(
            username = cd['username'], password = cd['password1']
        )
        if user is not None:
            login(self.request, user)
        return result
class StudentErollCourse(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm


    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse_lazy(
            'student_course_detail', args = [self.course.id]
        )
    
class StudentCourseListView(LoginRequiredMixin, ListView):
    model =Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in = [self.request.user])


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in = [self.request.user])

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()

        # to store the last accessed module
        redis_key = f"student:{self.request.user.id}:course:{course.id}:last_module"

        if 'module_id' in self.kwargs:
            
            # get current module
            module = course.modules.get(
                id = self.kwargs['module_id']
            )

            # r.set(redis_key, module.id)

            context['module'] = module


        else:

            # check redis for last accessed module id
            # last_module_id = r.get(redis_key)

            # if last_module_id:
            #     # redirect to the last accessed module
            #     return redirect(
            #         'studets:course_detail',
            #         pk = course.id,
            #         module_id = int(last_module_id)
            #     )
            
            # else:
                # default to the first module
                # get first module
                context['module_id'] = course.modules.all()[0]

        return context
        
    
    