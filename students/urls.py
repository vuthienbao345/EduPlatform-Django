from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name  = 'students'

urlpatterns = [
    path(
        'register/',
        views.StudentRegistrationView.as_view(),
        name = 'student_registration'
    ),
    path(
        'enroll-course/',
        views.StudentErollCourse.as_view(),
        name = 'student_enroll_course'
    ),
    path(
        'courses/',
        views.StudentCourseListView.as_view(),
        name = 'student_course_list'
    ),
    path(
        'course/<pk>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name = 'student_course_detail'
    ),
    path(
        'course/<pk>/<module_id>/',
       cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name = 'student_course_detail_module'
    ),

    path(
        'course/<int:pk>/module/<int:module_id>/', views.StudentCourseDetailView.as_view(), name = 'course_detail'
    ),
    path(
        'course/<int:pk>/', views.StudentCourseDetailView.as_view(), name = 'course_detail'
    ),
]