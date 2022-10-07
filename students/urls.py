from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='stu_home'),
    path('addstu/', views.add_student, name='stu_add'),
    path('submitted/', views.thanks_submission, name='stu_submit'),

]
