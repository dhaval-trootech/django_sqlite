from django.shortcuts import render
from engine.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def student(request):
    stud = Student.objects.all()
    context = {'stud': stud}
    return render(request, 'students/students.html', context)


def add_student(request):
    if request.method == 'POST':
        post = Student()
        post.stud_id = request.POST['sid']
        post.stud_name = request.POST['sname']
        post.stud_role = request.POST['srole']
        post.stud_phone = request.POST['sphone']
        post.stud_address = request.POST['saddress']
        post.save()
        return HttpResponseRedirect(reverse('stu_submit'))

    else:
        return render(request, 'students/add_students.html')


def thanks_submission(request):
    return render(request, 'students/thanks_submit.html')
