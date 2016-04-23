from django.shortcuts import render, redirect
from models import Student
from forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id is None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses__id=course_id)

    return render(request, 'students/list.html', {'students': students})


def detail(request, student_id):
    student_details = Student.objects.get(id__exact=student_id)

    return render(request, 'students/detail.html', {'student': student_details})


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["name"]
            last_name = form.cleaned_data["surname"]
            form.save()
            messages.success(request, "Student %s %s has been successfully added." % (first_name, last_name))
            return redirect("students:list_view")
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {"form": form})


def edit(request, student_id):
    update_record = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=update_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=update_record)

    return render(request, 'students/edit.html', {"form": form})


def remove(request, student_id):
    remove_record = Student.objects.get(id=student_id)
    first_name = remove_record.name
    last_name = remove_record.surname
    if request.method == "POST":
    	remove_record.delete()
        messages.success(request, "Info on %s %s has been sucessfully deleted." % (first_name, last_name))
        return redirect("students:list_view")

    return render(request, 'students/remove.html', {"name": first_name, "surname": last_name})