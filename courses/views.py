from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView 

from .models import Course, Subject
from .forms import ModuleFormSet

# Create your views here.


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
class OwnerCourseMixin(
    OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin
):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerEditMixin, OwnerCourseMixin):
    template_name = 'courses/manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'
    

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None


    def get_formset(self, data = None):
        return ModuleFormSet(instance = self.course, data = data)


    def dispatch(self, request, pk):
        self.course = get_object_or_404(
            Course, id = pk, owner = request.user
        )

        return super().dispatch(request, pk)
    

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response(
            {
                'course': self.course,
                'formset': formset,
            }
        )
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data = request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response(
            {
                'course': self.course,
                'formset': formset,
            }
        )

class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'courses/course/list.html'

    def get(self, request, subject = None):
        subjects = Subject.objects.annotate(
            total_courses =Count('courses')
        )
        courses = Course.objects.annotate(
            total_modules =Count('modules')
        )


        if subject:
            subject = get_object_or_404(subject = subject)
            courses = courses.filter(subject = subject)
        return self.render_to_response(
            {
                'subjects': subjects,
                'subject': subject,
                'courses': courses,
            }
        )
        

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course/detail.html'


